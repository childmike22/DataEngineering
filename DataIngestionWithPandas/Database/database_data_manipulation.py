# import libraries: pandas for data manipulation, sqlalchemy to connect to a database
import pandas as pd
from sqlalchemy import create_engine

# create a db engine
engine = create_engine('sqlite:///data.db')

# see all tables that exist
print(engine.table_names())

# load the weather table by table name
weather = pd.read_sql('weather', engine)

# now explore our newly created weather DataFrame!
print(weather.info())
print(weather.head(15))
print(weather.describe())
print(weather.columns)

# create a dataframe from our hpd311calls table
calls = pd.read_sql('hpd311calls', engine)

# lets see which boroughs have the most calls
num_calls_per_borough = calls.groupby('borough')['borough'].value_counts()
print(num_calls_per_borough.sort_values(ascending=False))

# number of 'PLUMBING' calls per borough
plumbing_query = '''SELECT borough, count(*)
FROM hpd311calls
WHERE complaint_type = 'PLUMBING'
GROUP BY 1
ORDER BY 2 desc'''

plumbing_stats = pd.read_sql(plumbing_query, engine)
print(plumbing_stats)


# TODO 1: Combine weather data with our 311 columns to see if specific weather is related to certain calls types
combo_query = """
SELECT c.*,
w.*
FROM hpd311calls c
LEFT JOIN weather w
ON c.created_date = w.date"""

weather_and_calls = pd.read_sql(combo_query, engine)
print(weather_and_calls.head())

mean_temp_by_call_type = weather_and_calls.groupby('complaint_type')['tmin'].mean().sort_values(ascending=False)
print(mean_temp_by_call_type)

water_leak_investigation = weather_and_calls.groupby('complaint_type')['prcp'].mean().sort_values(ascending=False)
print(water_leak_investigation)
