from nfl_data_py import import_pbp_data
import pandas as pd
from datetime import datetime

current_year = datetime.now().year

df_list = []

# Loop over play by play data for last 14 years and append to a csv file
for year in range(current_year - 15, current_year - 1):
    print(f"Loading {year} data")
    data = import_pbp_data([year])
    df_list.append(data)


full_df = pd.concat(df_list, ignore_index=True)

# Converting the data frame to a csv file for later use
full_df.to_csv(f"data/playbyplay_{current_year - 15}_{current_year - 1}.csv", index=False)