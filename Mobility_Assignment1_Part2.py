import pandas as pd
from tabulate import tabulate

# Read the CSV files
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# Filter the data for actnr == 1
filtered_df_base = df_base[df_base['Actnr'] == 1]
filtered_df_old = df_old[df_old['Actnr'] == 1]

# Explore by age group
sec_age_base = filtered_df_base.groupby(['Age', 'SEC']).size().unstack(fill_value=0)
sec_age_old = filtered_df_old.groupby(['Age', 'SEC']).size().unstack(fill_value=0)

comp_age_base = filtered_df_base.groupby(['Age', 'Comp']).size().unstack(fill_value=0)
comp_age_old = filtered_df_old.groupby(['Age', 'Comp']).size().unstack(fill_value=0)

# Calculate totals
sec_age_base['Total'] = sec_age_base.sum(axis=1)
sec_age_base.loc['Total'] = sec_age_base.sum()
sec_age_old['Total'] = sec_age_old.sum(axis=1)
sec_age_old.loc['Total'] = sec_age_old.sum()

comp_age_base['Total'] = comp_age_base.sum(axis=1)
comp_age_base.loc['Total'] = comp_age_base.sum()
comp_age_old['Total'] = comp_age_old.sum(axis=1)
comp_age_old.loc['Total'] = comp_age_old.sum()

# Convert to percentages
sec_age_base_perc = sec_age_base.div(sec_age_base.loc['Total']) * 100
sec_age_old_perc = sec_age_old.div(sec_age_old.loc['Total']) * 100

comp_age_base_perc = comp_age_base.div(comp_age_base.loc['Total']) * 100
comp_age_old_perc = comp_age_old.div(comp_age_old.loc['Total']) * 100

# Display SEC table
print("=================================== SEC: ===================================")
print("Base data:")
print(tabulate(sec_age_base_perc, headers='keys', tablefmt='pretty'))
print("----------------------------------------")
print("Old data:")
print(tabulate(sec_age_old_perc, headers='keys', tablefmt='pretty'))

# Display Comp table
print("=================================== Comp: ===================================")
print("Base data:")
print(tabulate(comp_age_base_perc, headers='keys', tablefmt='pretty'))
print("----------------------------------------")
print("Old data:")
print(tabulate(comp_age_old_perc, headers='keys', tablefmt='pretty'))
