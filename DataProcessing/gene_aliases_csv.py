# import the dependencies
import pandas as pd
import numpy as np
from python_functions_for_data_processing import gene_aliases
import csv

# Import file with gene names
gene_pd = pd.read_csv('gene_table.csv')

# producing a NaN value
NaN = np.nan

# start a counter
n = 0

# produce an empty list for the gene names
gene_list = []

# going along the entire list of gene names
while n in range(len(gene_pd)):
    # get the gene name from the pandas dataframe
    gene_name = gene_pd.iloc[n][0]
    # get the alias from the gene name using the function
    gene_alias = gene_aliases(gene_name)
    # if the result is "not found" or an empty list append the gene name and NaN in a tuple to the main list
    if (gene_alias == "NOT FOUND") or (gene_alias == []):
        unknown_alias = (gene_name, NaN)
        gene_list.append(unknown_alias)
    # otherwise get the gene alias and produce a tuple of the gene name and alias and append to the gene list
    else:
        for alias in gene_alias:
            one_alias = (gene_name, alias)
            gene_list.append(one_alias)

    # add to the counter for the next gene name to be assessed
    n += 1

print(gene_list)

# opening the gene alias csv
with open('gene_aliases_final.csv', 'w') as f:
    # at the end of the end of each line make a new line
    writer = csv.writer(f , lineterminator='\n')
    # add the titles to the rows
    writer.writerow(['gene_name','gene_alias'])
    # for each of the tuples in the gene list write the tuple in the csv
    for tup in gene_list:
        writer.writerow(tup)
