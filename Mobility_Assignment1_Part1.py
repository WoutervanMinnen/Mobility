import pandas as pd
from tabulate import tabulate

# Read the CSV file
df_base = pd.read_csv('Base_csv.csv')
df_old = pd.read_csv('Old_csv.csv')

# Filter the data for actnr == 1 (assuming Actnr is the column name)
filtered_df_base = df_base[df_base['Actnr'] == 1]
filtered_df_old = df_old[df_old['Actnr'] == 1]

# Group by age category and gender, and calculate the percentage of population
result = filtered_df_base.groupby(['Age', 'Gend']).size() / len(filtered_df_base) * 100
result_old = filtered_df_old.groupby(['Age', 'Gend']).size() / len(filtered_df_old) * 100

# Unstack to create a nice table, fill NaN values with 0, and add total column and row
result_table = result.unstack().fillna(0)
result_table_old = result_old.unstack().fillna(0)

result_table['Total'] = result_table.sum(axis=1)
result_table.loc['Total'] = result_table.sum()

result_table_old['Total'] = result_table_old.sum(axis=1)
result_table_old.loc['Total'] = result_table_old.sum()

# Round the values to have only one digit after the decimal point
result_table = result_table.round(2)
result_table_old = result_table_old.round(2)

# Print the result
print("Percentage of population in each age category for male and female:")
print("------------------------- Base data -------------------------")
print(tabulate(result_table, headers='keys', tablefmt='pretty'))
print("===================================================================")
print("------------------------- Old data -------------------------")
print(tabulate(result_table_old, headers='keys', tablefmt='pretty'))

# Save the tables to LaTeX format
result_table_latex = result_table.to_latex(index=True, escape=False, float_format="%.2f")
result_table_old_latex = result_table_old.to_latex(index=True, escape=False, float_format="%.2f")

# Modify LaTeX code to include lines and remove {lrrr} formatting
result_table_latex = result_table_latex.replace('\\begin{tabular}{lrrr}', '\\begin{table}[htbp]\n\\centering\n\\caption{Base Data}\n\\label{tab:base_data}\n\\begin{tabular}{|c|' + '|'.join(['c']*len(result_table.columns)) + '|}\n')
result_table_old_latex = result_table_old_latex.replace('\\begin{tabular}{lrrr}', '\\begin{table}[htbp]\n\\centering\n\\caption{Old Data}\n\\label{tab:old_data}\n\\begin{tabular}{|c|' + '|'.join(['c']*len(result_table_old.columns)) + '|}\n')
result_table_latex = result_table_latex.replace('\\toprule', '\hline')
result_table_latex = result_table_latex.replace('\\midrule', '\hline')
result_table_latex = result_table_latex.replace('\\bottomrule', '\hline\n\\end{tabular}\n\\end{table}\n')

result_table_old_latex = result_table_old_latex.replace('\\toprule', '\hline')
result_table_old_latex = result_table_old_latex.replace('\\midrule', '\hline')
result_table_old_latex = result_table_old_latex.replace('\\bottomrule', '\hline\n\\end{tabular}\n\\end{table}\n')

# Write the modified LaTeX code to files with the desired names
with open('Assignment1_base.tex', 'w') as f:
    f.write(result_table_latex)

with open('Assignment1_old.tex', 'w') as f:
    f.write(result_table_old_latex)

print("Tables saved as Assignment1_base.tex and Assignment1_old.tex")
