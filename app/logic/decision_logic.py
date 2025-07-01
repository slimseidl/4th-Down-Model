import pandas as pd
import re

def parse_interval(s):
    match = re.match(r'[\[\(](\d+),\s*(\d+)[\]\)]', s)
    if match:
        left = int(match.group(1))
        right = int(match.group(2))
        closed = "both" if "[" in s and "]" in s else \
                 "left" if "[" in s else \
                 "right" if "]" in s else "neither"
        return pd.Interval(left=left, right=right, closed=closed)
    return None


def decide_ev_based(ydstogo, yardline_100, table):
    for _, row in table.iterrows():
        if row["yard_bin"].left <= yardline_100 < row["yard_bin"].right and \
           row["distance_bin"].left <= ydstogo < row["distance_bin"].right:
            return row["decision"]
    return "No Go"

def load_decision_table(path):
    df = pd.read_csv(path)
    df["yard_bin"] = df["yard_bin"].apply(parse_interval)
    df["distance_bin"] = df["distance_bin"].apply(parse_interval)
    return df