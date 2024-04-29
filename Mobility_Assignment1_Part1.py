import pandas as pd
from tabulate import tabulate

# Read the CSV file
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# Filter the data for actnr == 1 (assuming Actnr is the column name)
filtered_df_base = df_base[df_base['Actnr'] == 1]
filtered_df_old = df_old[df_old['Actnr'] == 1]

# Group by age category and gender, and calculate the percentage of population
result = filtered_df_base.groupby(['Age', 'Gend']).size() / filtered_df_base.groupby('Gend').size() * 100
result_old = filtered_df_old.groupby(['Age', 'Gend']).size() / filtered_df_old.groupby('Gend').size() * 100

# Unstack to create a nice table, fill NaN values with 0, and add total column and row
result_table = result.unstack().fillna(0)
result_table_old = result_old.unstack().fillna(0)

result_table['Total gend'] = result_table.sum(axis=1)
result_table.loc['Total fun'] = result_table.sum()

result_table_old['Total gend'] = result_table_old.sum(axis=1)
result_table_old.loc['Total fun'] = result_table_old.sum()

# This a header that joeri has to learn

# Print the result
print("Percentage of population in each age category for male and female:")
print("------------------------- Base data -------------------------")
print(tabulate(result_table, headers='keys', tablefmt='pretty'))
print("===================================================================")
print("------------------------- Old data -------------------------")
print(tabulate(result_table_old, headers='keys', tablefmt='pretty'))
