import pandas as pd
import sys
import os

# Modifying sustem path to import decision logic

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.logic.decision_logic import decide_ev_based, load_decision_table


# Loading Data
df = pd.read_csv("C:/Users/jseidl/NFL-4th-Down/data/processed/cleaned_4th_down.csv")

# Loading decision table
decision_table = load_decision_table("C:/Users/jseidl/NFL-4th-Down/data/processed/decision_table.csv")

# Applying decision to each row
df['recommended'] = df.apply(lambda row: decide_ev_based(
    row['ydstogo'],
    row['yardline_100'],
    decision_table
), axis=1)

# Defining what the coach actually did with function below

def actual_choice(row):
    if row['play_type'] in ['run', 'pass']:
        return "Go"
    elif row['play_type'] in ['punt', 'field_goal']:
        return "No Go"
    return "Other"

df['actual'] = df.apply(actual_choice, axis=1)
df['matched'] = df['recommended'] == df['actual']

# Implementing accuracy metrics to compare coach to model 
# See Image of accuracy
match_rate = df['matched'].mean()
success_when_matched = df[df['matched']]['success'].mean()
actual_success = df['success'].mean()

# Print Summary
print(f"Tool Match Accuracy: {match_rate:.2%}")
print(f"Success When Tool Followed: {success_when_matched:.2%}")
print(f"Overall Success Rate: {actual_success:.2%}")

# Saving full dataset to CSV for future use
df.to_csv("C:/Users/jseidl/NFL-4th-Down/data/processed/eval_results.csv", index=False)