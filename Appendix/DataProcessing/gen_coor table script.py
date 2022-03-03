# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:58:41 2022

@author: dpava
"""

''' Script to read multiple csv's in a folder, take the position column and append them to a new data frame
    Adapted from: https://stackoverflow.com/questions/58564257/how-to-iterate-over-files-extract-file-name-and-pass-to-pandas-logic'''

# Imports
import pandas as pd
import os
import numpy as np

# Creates a new data frame to store position data
position_df = pd.DataFrame(columns = ['position'])

# directory where the files are stored 
directory = 'C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/snp/'

# Loop to go over each file in the directory, read every csv, store the position column and append it in the final data frame. 
for file in os.listdir(directory):
    if file.endswith(".csv"):
        temp_file = pd.read_csv(directory + file)
        temp_df = pd.DataFrame(temp_file['position'])
        position_df = position_df.append(temp_df,ignore_index= True)
    else:
        print('file ',file,' was not included')
    continue


# File to check the positions were extracted correctly and print to check length against SQL 
#position_df.to_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/positions.csv',index = False)
print('position ',len(position_df))

### GENERATING A FILE WITH ALL POSITIONS ###  

# Put the columns from the gene names folder into a data frame 
gene_file = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/genenamesall.csv')
gene_df = pd.DataFrame(gene_file)

# Use the merge function to join both data frames based on the whole list of position values. 
result = pd.merge(position_df,gene_df,on="position",\
                  how = 'left')

# In the chr_id columns, all NaN values are replaced for number 21 as an integer. 
result['chr_id'] = result['chr_id'].replace(np.nan,21).astype(int)
print('results ',len(result))

# Checking for duplicates:
uniques = pd.DataFrame(data=None)
uniques = result['position'].unique()\
    
# Checking length of values to see if there were duplicates 
print('uniques ',len(uniques))

# Looking at the end to see if they missmatched 
#print(result.tail())
#print(position_df.tail())


# Identified the difference in excel, dropping the repeated rows below
print(result[result['position']==21231655].index.values)

# new data frame to store the clean results df
modresult = result.drop([result.index[234661],\
                         result.index[234660],\
                         result.index[234659]])

# Checker to see if any repeated values remain 
print(modresult[modresult['position']==21231655].index.values)

# Exporting the csv for the SQL data base.  
modresult.to_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/gen_coor.csv',\
              index = False)

#print length modresult
print('modresults ',len(modresult))


