# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:41:31 2022

@author: dpava
"""
# Import pandas
import pandas as pd

# Store the csv in a dataframe
pop_df = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/snp_characteristics/4-snp_characteristics1000001-end.csv')


# Create a new dataframe specifying the old name and new name of the column 
fixed_df = pop_df.rename(columns = {'population':'pop_id'})

# Export the dataframe as a csv, with no index (row names)
fixed_df.to_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/snp_characteristics/4fix-snp_characteristics1000001-end.csv', index = False)
