import pandas as pd
from tabulate import tabulate

# Read the CSV files
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# filtered_df_base = df_base[df_base['Actnr'] == 1]
# filtered_df_old = df_old[df_old['Actnr'] == 1]
filtered_df_base = df_base
filtered_df_old = df_old

# Initialize dictionaries to store frequency, percentage, and total travel time for each hour
hourly_stats_base = {'Hour': [], 'Frequency': [], 'Percentage': [], 'Total TravTime': []}
hourly_stats_old = {'Hour': [], 'Frequency': [], 'Percentage': [], 'Total TravTime': []}

# Iterate through each hour of the day
for hour in range(24):
    # Calculate the start and end time for the current hour
    start_time = hour * 100
    end_time = (hour + 1) * 100

    # Filter the data for trips within the current hour
    trips_within_hour_base = filtered_df_base[
        (filtered_df_base['BT'] >= start_time) & (filtered_df_base['BT'] < end_time)]
    trips_within_hour_old = filtered_df_old[(filtered_df_old['BT'] >= start_time) & (filtered_df_old['BT'] < end_time)]

    # Count the frequency of trips within the current hour
    frequency_base = len(trips_within_hour_base)
    frequency_old = len(trips_within_hour_old)

    # Calculate the percentage of trips within the current hour
    total_trips_base = len(filtered_df_base)
    total_trips_old = len(filtered_df_old)
    percentage_base = (frequency_base / total_trips_base) * 100
    percentage_old = (frequency_old / total_trips_old) * 100

    # Calculate the total travel time within the current hour
    total_travtime_base = trips_within_hour_base['TravTime'].sum()
    total_travtime_old = trips_within_hour_old['TravTime'].sum()

    # Append the statistics to the dictionaries
    hourly_stats_base['Hour'].append(hour)
    hourly_stats_base['Frequency'].append(frequency_base)
    hourly_stats_base['Percentage'].append(percentage_base)
    hourly_stats_base['Total TravTime'].append(total_travtime_base)

    hourly_stats_old['Hour'].append(hour)
    hourly_stats_old['Frequency'].append(frequency_old)
    hourly_stats_old['Percentage'].append(percentage_old)
    hourly_stats_old['Total TravTime'].append(total_travtime_old)

# Create DataFrames from the dictionaries
hourly_stats_df_base = pd.DataFrame(hourly_stats_base)
hourly_stats_df_old = pd.DataFrame(hourly_stats_old)

# Round the percentage values
hourly_stats_df_base['Percentage'] = hourly_stats_df_base['Percentage'].round(2)
hourly_stats_df_old['Percentage'] = hourly_stats_df_old['Percentage'].round(2)

result_table_base_total = hourly_stats_df_base.copy()
result_table_base_total.loc['Total'] = result_table_base_total.round(0).sum()
result_table_base_total.at['Total', 'Hour'] = 'Total'

result_table_old_total = hourly_stats_df_old.copy()
result_table_old_total.loc['Total'] = result_table_old_total.round(0).sum()
result_table_old_total.at['Total', 'Hour'] = 'Total'

# Print the results
print("Distribution of trips within each hour of the day:")
print("------------------------- Base data -------------------------")
print(tabulate(result_table_base_total, headers='keys', tablefmt='pretty', showindex=False))
print("===================================================================")
print("------------------------- Old data -------------------------")
print(tabulate(result_table_old_total, headers='keys', tablefmt='pretty', showindex=False))


# Save the tables to LaTeX format
result_table_latex = result_table_base_total.to_latex(index=True, escape=False, float_format="%.2f")
result_table_old_latex = result_table_old_total.to_latex(index=True, escape=False, float_format="%.2f")

# Modify LaTeX code to include lines and remove {lrrr} formatting
result_table_latex = result_table_latex.replace('\\begin{tabular}{llrrr}', '\\begin{table}[htbp]\n\\centering\n\\caption{Base Data}\n\\label{tab:base_data}\n\\begin{tabular}{|c|' + '|'.join(['c']*len(result_table_base_total.columns)) + '|}\n')
result_table_old_latex = result_table_old_latex.replace('\\begin{tabular}{llrrr}', '\\begin{table}[htbp]\n\\centering\n\\caption{Old Data}\n\\label{tab:old_data}\n\\begin{tabular}{|c|' + '|'.join(['c']*len(result_table_old_total.columns)) + '|}\n')
result_table_latex = result_table_latex.replace('\\toprule', '\hline')
result_table_latex = result_table_latex.replace('\\midrule', '\hline')
result_table_latex = result_table_latex.replace('\\bottomrule', '\hline\n\\end{tabular}\n\\end{table}\n')

result_table_old_latex = result_table_old_latex.replace('\\toprule', '\hline')
result_table_old_latex = result_table_old_latex.replace('\\midrule', '\hline')
result_table_old_latex = result_table_old_latex.replace('\\bottomrule', '\hline\n\\end{tabular}\n\\end{table}\n')

# Write the modified LaTeX code to files with the desired names
with open('Assignment6_base.tex', 'w') as f:
    f.write(result_table_latex)

with open('Assignment6_old.tex', 'w') as f:
    f.write(result_table_old_latex)

print("Tables saved as Assignment1_base.tex and Assignment1_old.tex")
