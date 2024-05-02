import pandas as pd
from tabulate import tabulate

# Read the CSV files
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# Convert 'TravDist' and 'TravTime' columns to numeric type, coercing errors to NaN
df_base['TravDist'] = pd.to_numeric(df_base['TravDist'], errors='coerce')
df_base['TravTime'] = pd.to_numeric(df_base['TravTime'], errors='coerce')

df_old['TravDist'] = pd.to_numeric(df_old['TravDist'], errors='coerce')
df_old['TravTime'] = pd.to_numeric(df_old['TravTime'], errors='coerce')

# Filter the data for travdist != 0 and travtime > 0
filtered_df_base = df_base[(df_base['TravDist'] != 0) & (df_base['TravTime'] > 0)]
filtered_df_old = df_old[(df_old['TravDist'] != 0) & (df_old['TravTime'] > 0)]

# Calculate the sum of total distance, total travel time, and number of trips
total_distance_base = filtered_df_base['TravDist'].sum()
total_distance_old = filtered_df_old['TravDist'].sum()

total_time_base = filtered_df_base['TravTime'].sum()
total_time_old = filtered_df_old['TravTime'].sum()

num_trips_base = len(filtered_df_base)
num_trips_old = len(filtered_df_old)

# Calculate the differences
diff_distance = total_distance_base - total_distance_old
diff_time = total_time_base - total_time_old
diff_trips = num_trips_base - num_trips_old

# Create a table to display the differences
difference_table = pd.DataFrame({
    'Total Distance': [total_distance_base, total_distance_old, diff_distance],
    'Total Travel Time': [total_time_base, total_time_old, diff_time],
    'Number of Trips': [num_trips_base, num_trips_old, diff_trips]
}, index=['Base data', 'Old data', 'Difference'])

# Print the result
print("Difference in total distance, total travel time, and number of trips between scenarios:")
print(tabulate(difference_table, headers='keys', tablefmt='pretty'))
