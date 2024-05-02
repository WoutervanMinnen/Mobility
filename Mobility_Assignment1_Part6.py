import pandas as pd
from tabulate import tabulate

# Read the CSV files
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# filtered_df_base = df_base[df_base['Actnr'] == 1]
# filtered_df_old = df_old[df_old['Actnr'] == 1]
filtered_df_base = df_base
filtered_df_old = df_old