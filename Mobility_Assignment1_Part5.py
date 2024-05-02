import pandas as pd
from tabulate import tabulate

# Read the CSV files
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# filtered_df_base = df_base[df_base['Actnr'] == 1]
# filtered_df_old = df_old[df_old['Actnr'] == 1]
filtered_df_base = df_base
filtered_df_old = df_old

# Calculate the frequency of each 'Atype'
frequency_base = filtered_df_base['Atype'].value_counts()
frequency_old = filtered_df_old['Atype'].value_counts()

# Calculate the percentage of population in each 'Atype' category
percentage_base = frequency_base / len(filtered_df_base) * 100
percentage_old = frequency_old / len(filtered_df_old) * 100

# Create tables with 'Atype', 'Frequency', and 'Percentage' columns
result_table_base = pd.DataFrame({'Atype': frequency_base.index, 'Frequency': frequency_base, 'Percentage': percentage_base})
result_table_old = pd.DataFrame({'Atype': frequency_old.index, 'Frequency': frequency_old, 'Percentage': percentage_old})

# Round the values
# result_table_base['Percentage'] = result_table_base['Percentage'].round(1)
# result_table_old['Percentage'] = result_table_old['Percentage'].round(1)

# Sort the tables by index (Atype) in ascending order
result_table_base.sort_index(inplace=True)
result_table_old.sort_index(inplace=True)

# Calculate and add the total row
result_table_base_total = result_table_base.copy()
result_table_base_total.loc['Total'] = result_table_base_total.sum()
result_table_base_total.at['Total', 'Atype'] = 'Total'

result_table_old_total = result_table_old.copy()
result_table_old_total.loc['Total'] = result_table_old_total.sum()
result_table_old_total.at['Total', 'Atype'] = 'Total'

# Set 'Atype' as index again
result_table_base_total.set_index('Atype', inplace=True)
result_table_old_total.set_index('Atype', inplace=True)

result_table_base_total = result_table_base_total.round(1)
result_table_old_total = result_table_old_total.round(1)

# Print the result
print("Frequency and percentage of population in each Atype category:")
print("------------------------- Base data -------------------------")
print(tabulate(result_table_base_total, headers='keys', tablefmt='pretty'))
print("===================================================================")
print("------------------------- Old data -------------------------")
print(tabulate(result_table_old_total, headers='keys', tablefmt='pretty'))
