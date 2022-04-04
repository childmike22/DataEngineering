import pandas as pd

datetime_cols = ['Part1StartTime', 'Part1EndTime', 'Part2StartTime', 'Part2EndTime']

# create a DF of only 2017 data
df_2017 = pd.read_excel('fcc-new-coder-survey (2).xlsx', sheet_name='2017', skiprows=2, parse_dates=datetime_cols)

# create new columns for start_date and end_date
df_2017['StartDate'] = df_2017['Part1StartTime'].dt.strftime('%m-%d-%Y')
print(df_2017['StartDate'].head())
# print(df_2017.head())
print(df_2017.columns)

cityPopulationInfo = df_2017.groupby('CityPopulation')['CityPopulation'].value_counts()
print(cityPopulationInfo.sort_values(ascending=False))

# Lot of boolean columns, lets see the total of each
print(df_2017.sum())


# Missing data
print("MISSING DATA BELOW\n")
print(df_2017.isna().sum())

print(df_2017.info())
