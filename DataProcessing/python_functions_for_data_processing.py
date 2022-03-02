def VCFtosnp(inputlist, outputlist, popcodelist,start,end):
    '''converts multiple population VCFs to a combined CSV containing information on the genomic position,
    reference and alternate alleles, and rs values. Removes multi-allelic sites.
    
    Parameters
    ----------
    
    inputlist: list of strings, where each string is the path to a population VCF file
    outputlist: list of strings, where each string is the path to an output population snp table CSV
    popcodelist: list of strings, where each string is a three letter code for a different population
    start:
    end:
    
    
    Description
    -----------
    
    Recieve 5 parameters: a list of input file paths, a list of output file paths, and a list of population codes. 
    
    '''

    # import dependencies
    import pandas as pd
    import os
    from Conversion_scripts import VCFtoPandas
    from pathlib import Path

    # iterate over the 5 population vcfs
    for inVCF, outCSV,popcode in zip(inputlist,outputlist,popcodelist):

        # check inputs
        print("process started...")
        print(inVCF)

        # create dataframe
        df = VCFtoPandas(inVCF)
        print("dataframe created")

        # rename columns in accordance with SQL schema
        df.rename(columns={'#CHROM': 'chromosome', 'POS': 'position', 'ID': 'rs_value', 'REF': 'reference', 'ALT': 'alternate'}, inplace=True)
        print("columns renamed")

        # shorten the df
        df = df.loc[start:end]

        # extract row names
        row_labels_df = list(df.index)

        # remove multiallelic sites
        for row in row_labels_df:
            alt = df.loc[row,'alternate']
            alt = len(alt)
            if alt != 1:
                # delete multiallelic row from dataframe
                df = df.drop(labels=row)

        print("multi allelic sites removed")
        df = df.reset_index()
        print("index reset")

        # extract updated row names
        row_labels_df = list(df.index)


        # remove unwanted columns
        df_info = df.filter(['position', 'rs_value', 'reference', 'alternate'], axis=1)

        # export to csv
        df_info.to_csv(outCSV, index=False)
