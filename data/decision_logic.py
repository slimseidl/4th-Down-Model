# Decision Function
def decide_ev_based(ydstogo, yardline_100, table):
    for _, row in table.iterrows():
        if row["yard_bin"].left <= yardline_100 < row["yard_bin"].right and \
           row["distance_bin"].left <= ydstogo < row["distance_bin"].right:
            return row["decision"]
    return "No Go"