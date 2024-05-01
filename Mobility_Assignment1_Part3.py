import pandas as pd
from tabulate import tabulate

# Read the CSV files
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# Filter the data for travdist == 0 and travtime > 0
filtered_df_base = df_base[(df_base['travdist'] == 0) & (df_base['travtime'] > 0)]
filtered_df_old = df_old[(df_old['travdist'] == 0) & (df_old['travtime'] > 0)]

# Calculate the sum of total distance, total travel time, and number of trips
total_distance_base = filtered_df_base['travdist'].sum()
total_distance_old = filtered_df_old['travdist'].sum()

total_time_base = filtered_df_base['travtime'].sum()
total_time_old = filtered_df_old['travtime'].sum()

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
