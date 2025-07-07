# nfl data from nflverse GitHub Repo gives access to historical play by play data
from nfl_data_py import import_pbp_data
import pandas as pd
from datetime import datetime

# Setting the range based on current year
# for future proofing
current_year = datetime.now().year

df_list = []

# Loop over play by play data for last 14 years and append to a csv file
# Dynamic loop with future proofing
for year in range(current_year - 15, current_year - 1):
    print(f"Loading {year} data")
    data = import_pbp_data([year])
    df_list.append(data)

# Each season combined into list and then into one dataframe
full_df = pd.concat(df_list, ignore_index=True)

# Converting the data frame to a csv file for later use
full_df.to_csv(f"data/raw/playbyplay_last_14_years.csv", index=False)