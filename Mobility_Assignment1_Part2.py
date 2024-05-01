import pandas as pd
from tabulate import tabulate

# Read the CSV file
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# Filter the data for actnr == 1 (assuming Actnr is the column name)
filtered_df_base = df_base[df_base['Actnr'] == 1]
filtered_df_old = df_old[df_old['Actnr'] == 1]

# Group by age category and gender, and calculate the percentage of population
# result_SEC = filtered_df_base.groupby(['Age', 'Gend']).size() / filtered_df_base.groupby('Gend').size() * 100
# result_old_SEC = filtered_df_old.groupby(['Age', 'Gend']).size() / filtered_df_old.groupby('Gend').size() * 100
result_SEC = filtered_df_base.groupby(['Age', 'SEC']).size() / len(filtered_df_base) * 100
result_old_SEC = filtered_df_old.groupby(['Age', 'SEC']).size() / len(filtered_df_old) * 100

result_COMP = filtered_df_base.groupby(['Age', 'Comp']).size() / len(filtered_df_base) * 100
result_old_COMP = filtered_df_old.groupby(['Age', 'Comp']).size() / len(filtered_df_base) * 100

# Unstack to create a nice table, fill NaN values with 0, and add total column and row
result_table = result_SEC.unstack().fillna(0)
result_table_old = result_old_SEC.unstack().fillna(0)

result_table_COMP = result_COMP.unstack().fillna(0)
result_table_old_COMP = result_old_COMP.unstack().fillna(0)

result_table['Total'] = result_table.sum(axis=1)
result_table.loc['Total'] = result_table.sum()
result_table_COMP['Total'] = result_table_COMP.sum(axis=1)
result_table_COMP.loc['Total'] = result_table_COMP.sum()

result_table_old['Total'] = result_table_old.sum(axis=1)
result_table_old.loc['Total'] = result_table_old.sum()
result_table_old_COMP['Total'] = result_table_old_COMP.sum(axis=1)
result_table_old_COMP.loc['Total'] = result_table_old_COMP.sum()

result_table = result_table.round(2)
result_table_COMP = result_table_COMP.round(2)
result_table_old = result_table_old.round(2)
result_table_old_COMP = result_table_old_COMP.round(2)

# Print the result_SEC
print("Percentage of population in each age category for male and female:")
print("=================================== SEC data =====================================")
print("------------------------- Base data -------------------------")
print(tabulate(result_table, headers='keys', tablefmt='pretty'))
print("===================================================================")
print("------------------------- Old data -------------------------")
print(tabulate(result_table_old, headers='keys', tablefmt='pretty'))
print("=================================== Comp data =====================================")
print("------------------------- Base data -------------------------")
print(tabulate(result_table_COMP, headers='keys', tablefmt='pretty'))
print("===================================================================")
print("------------------------- Old data -------------------------")
print(tabulate(result_table_old_COMP, headers='keys', tablefmt='pretty'))
