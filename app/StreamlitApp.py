import streamlit as st
import pandas as pd
import joblib
from decision import decide_ev_based
import ast

# parsing from CSV
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

decision_table = pd.read_csv("C:/Users/jseidl/NFL-4th-Down/data/decision_table.csv")

decision_table["yard_bin"] = decision_table["yard_bin"].apply(parse_interval)
decision_table["distance_bin"] = decision_table["distance_bin"].apply(parse_interval)

st.title("NFL 4th Down Decision Maker")

ydstogo = st.number_input("Yards to Go", min_value=1, max_value=40, value=4)
yardline_100 = st.number_input("Field Position (distance from opposing end zone)", min_value=1, max_value=99, value=45)

if st.button("Should You go for it?"):
    recommendation = decide_ev_based(ydstogo, yardline_100, decision_table)
    st.markdown(f"### Recommendation: ** {recommendation.upper()}**")

st.metric(label="Recommended Action", value=recommendation.upper())