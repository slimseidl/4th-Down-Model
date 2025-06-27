import streamlit as st
import pandas as pd
import joblib
from decision import decide_ev_based
import ast

# Parse interval strings from CSV
def parse_interval(interval_str):
    left_bracket = interval_str[0]
    right_bracket = interval_str[-1]
    left_closed = left_bracket == "["
    right_closed = right_bracket == "]"
    bounds = ast.literal_eval(interval_str[1:-1])
    return pd.Interval(bounds[0], bounds[1], 
                       closed=('both' if left_closed and right_closed else 
                               'left' if left_closed else 
                               'right' if right_closed else 
                               'neither'))

# Loading decision table
decision_table = pd.read_csv("data/decision_table.csv")
decision_table["yard_bin"] = decision_table["yard_bin"].apply(parse_interval)
decision_table["distance_bin"] = decision_table["distance_bin"].apply(parse_interval)

# Loading trained model
model = joblib.load("data/tree_model.pkl")

# Define prediction function
def predict_tree_decision(ydstogo, yardline_100, score_diff, game_sec_remain, qtr, posteam_timeouts, defteam_timeouts):
    input_df = pd.DataFrame([{
        "ydstogo": ydstogo,
        "yardline_100": yardline_100,
        "score_differential": score_diff,
        "game_seconds_remaining": game_sec_remain,
        "qtr": qtr,
        "posteam_timeouts_remaining": posteam_timeouts,
        "defteam_timeouts_remaining": defteam_timeouts
    }])
    return model.predict(input_df)[0]

# App UI
st.title("NFL 4th Down Decision: Coach vs. Model")

# Inputs
ydstogo = st.number_input("Yards to Go", min_value=1, max_value=40, value=4)
yardline_100 = st.number_input("Field Position (yards from opponent's end zone)", min_value=1, max_value=99, value=45)
score_diff = st.number_input("Score Differential (your team - opponent)", value=0)

# Option for minutes and seconds or total seconds
st.markdown("### Game Time Remaining")
col_min, col_sec = st.columns(2)
with col_min:
    minutes = st.number_input("Minutes", min_value=0, max_value=15, value=15, step=1)
with col_sec:
    seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0, step=1)
game_sec_remain = int(minutes * 60 + seconds)

# Max time limits
if game_sec_remain > 900:
    st.warning("Game time can't exceed 15 minutes per quarter. Capping to 900 seconds.")
    game_sec_remain = 900
st.caption(f"Total Time Remaining: {game_sec_remain} seconds")

quarter = st.selectbox("Quarter", options=[1, 2, 3, 4], index=3)
posteam_timeouts = st.selectbox("Offensive Team Timeouts Remaining", options=[0, 1, 2, 3], index=3)
defteam_timeouts = st.selectbox("Defensive Team Timeouts Remaining", options=[0, 1, 2, 3], index=3)


# Button to compare
if st.button("Compare Coach vs. Model"):
    coach_decision = decide_ev_based(ydstogo, yardline_100, decision_table)
    model_decision = predict_tree_decision(ydstogo, yardline_100, score_diff, game_sec_remain, quarter, posteam_timeouts, defteam_timeouts)

    col1, col2 = st.columns(2)
    col1.metric("Coach Decision", coach_decision.upper())
    col2.metric("Model Decision", "GO" if model_decision == 1 else "PUNT")
