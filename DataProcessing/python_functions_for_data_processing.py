def VCFtosnp(inputlist, outputlist, popcodelist):
    'converting multiple population VCFs to a combined CSV, removing multi-allelic sites. Author: Isabel Thompson.'

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
        df = df.loc[1000001:]

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
