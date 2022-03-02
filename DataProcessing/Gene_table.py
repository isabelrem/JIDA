# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 23:15:29 2022

@author: dpava
"""

import pandas as pd

''' The following script takes a csv file with repeated gene names in a column,
    stores the name of each gene once, and exports it as a csv '''

# Reads a csv and stores it in a dataframe
gene_df = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/genenamesall.csv')

# List with the unique values in the gene_id column
gene_keys = gene_df['gene_id'].unique()

# Dataframe with values and titles of columns
genes_df = pd.DataFrame(gene_keys, columns=['id'] )

#Exporting to csv 
genes_df.to_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/gene_table.csv', index = False)



