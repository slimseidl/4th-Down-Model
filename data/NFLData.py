from nfl_data_py import import_pbp_data
import pandas as pd

df_list = []

for year in range(2010, 2026):
    print(f"Loading {year} data")
    data = import_pbp_data([year])
    df_list.append(data)

full_df = pd.concat(df_list, ignore_index=True)

full_df.to_csv("data/playbyplay_2010_2025")