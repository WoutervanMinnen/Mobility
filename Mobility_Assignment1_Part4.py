import pandas as pd
from tabulate import tabulate

# Read the CSV files
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# Filter rows where 'Mode' column has a specified mode (0, 1, 2, or 3) or is not an empty string
specified_modes = ['0', '1', '2', '3']
filtered_df_base = df_base[df_base['Mode'].isin(specified_modes) | (df_base['Mode'] != ' ')]
filtered_df_old = df_old[df_old['Mode'].isin(specified_modes) | (df_old['Mode'] != ' ')]

# Convert 'Mode' column to numeric type (optional)
filtered_df_base['Mode'] = pd.to_numeric(filtered_df_base['Mode'])
filtered_df_old['Mode'] = pd.to_numeric(filtered_df_old['Mode'])

# Calculate the frequency of each 'Mode'
frequency_base = filtered_df_base['Mode'].value_counts()
frequency_old = filtered_df_old['Mode'].value_counts()

# Calculate the percentage of population in each 'Mode' category
total_base = len(filtered_df_base)
total_old = len(filtered_df_old)

# Calculate percentage only for specified modes
percentage_base = (frequency_base / total_base) * 100
percentage_old = (frequency_old / total_old) * 100

# Create tables with 'Mode', 'Frequency', and 'Percentage' columns
result_table_base = pd.DataFrame({'Mode': frequency_base.index, 'Frequency': frequency_base, 'Percentage': percentage_base})
result_table_old = pd.DataFrame({'Mode': frequency_old.index, 'Frequency': frequency_old, 'Percentage': percentage_old})

# Round the values
result_table_base = result_table_base.round(1)
result_table_old = result_table_old.round(1)

# Sort the tables by index (Mode) in ascending order
result_table_base.sort_index(inplace=True)
result_table_old.sort_index(inplace=True)

# Calculate and add the total row
result_table_base.loc['Total'] = result_table_base.sum()
result_table_base.at['Total', 'Mode'] = 'Total'

result_table_old.loc['Total'] = result_table_old.sum()
result_table_old.at['Total', 'Mode'] = 'Total'

# Convert DataFrames to lists for tabulate
result_table_base_list = result_table_base.values.tolist()
result_table_old_list = result_table_old.values.tolist()

# Print the result using tabulate
print("Frequency and percentage of population in each Mode category:")
print("------------------------- Base data -------------------------")
print(tabulate(result_table_base_list, headers=result_table_base.columns, tablefmt='grid'))
print("\n------------------------- Old data -------------------------")
print(tabulate(result_table_old_list, headers=result_table_old.columns, tablefmt='grid'))


# Save the tables to LaTeX format
result_table_latex = result_table_base_list.to_latex(index=True, escape=False, float_format="%.2f")
result_table_old_latex = result_table_old_list.to_latex(index=True, escape=False, float_format="%.2f")

# Modify LaTeX code to include lines and remove {lrrr} formatting
result_table_latex = result_table_latex.replace('\\begin{tabular}{llrrr}', '\\begin{table}[htbp]\n\\centering\n\\caption{Base Data}\n\\label{tab:base_data}\n\\begin{tabular}{|c|' + '|'.join(['c']*len(result_table_base_list.columns)) + '|}\n')
result_table_old_latex = result_table_old_latex.replace('\\begin{tabular}{llrrr}', '\\begin{table}[htbp]\n\\centering\n\\caption{Old Data}\n\\label{tab:old_data}\n\\begin{tabular}{|c|' + '|'.join(['c']*len(result_table_old_list.columns)) + '|}\n')
result_table_latex = result_table_latex.replace('\\toprule', '\hline')
result_table_latex = result_table_latex.replace('\\midrule', '\hline')
result_table_latex = result_table_latex.replace('\\bottomrule', '\hline\n\\end{tabular}\n\\end{table}\n')

result_table_old_latex = result_table_old_latex.replace('\\toprule', '\hline')
result_table_old_latex = result_table_old_latex.replace('\\midrule', '\hline')
result_table_old_latex = result_table_old_latex.replace('\\bottomrule', '\hline\n\\end{tabular}\n\\end{table}\n')

# Write the modified LaTeX code to files with the desired names
with open('Assignment4_base.tex', 'w') as f:
    f.write(result_table_latex)

with open('Assignment4_old.tex', 'w') as f:
    f.write(result_table_old_latex)

print("Tables saved as Assignment4_base.tex and Assignment4_old.tex")
