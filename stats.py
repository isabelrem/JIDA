############################### SQL TO PANDAS ###############################
import allel
import numpy as np


def SQLtoPandasViaPOS(database, table, start, end):
    ' Using the inputs of a database name, table name, and start and end genomic coordinates, produces a pandas dataframe'
    # importing dependencies
    import pandas as pd
    import sqlite3

    # connecting to database
    conn = sqlite3.connect(database)
    query = "SELECT * FROM " + table
    sql_query = pd.read_sql_query(query, conn)

    # converting sql file to dataframe, specifying the columns
    df = pd.DataFrame(sql_query, columns=['chromosome', 'position', 'rs_value', 'population', 'reference', 'alternate',
                                          'sample_count', '0|0', '0|1', '1|0', '1|1'])

    # converting all values in the position column to integers
    df["position"] = df["position"].astype(int)

    # reducing the dataframe to snps within the start and end coordinates specified
    d = df[(df['position'] >= start) & (df['position'] <= end)]

    # resetting the dataframe index
    d = d.reset_index()

    return d


############################### HAPLOTYPE LIST ###############################

def haplotype_list(dataframe):
    ''' Using a dataframe as input, creates a haplotype list '''

    # producing an empty genotype columns dataframe, with the column headers specified.
    genotype_columns = dataframe[['0|0', '0|1', '1|0', '1|1']]

    # extracting the row labels/ indices from the input dataframe
    row_labels = list(genotype_columns.index)

    # initiating the haplotype list
    ALL_HAPLOTYPE_LIST = []

    # for each row of the dataframe, create a haplotype list using the haplotype counts present in the input dataframe
    for row in row_labels:
        # initiate single row haplotype list
        single_variant_haplotype_list = []
        # extract the value from the row for a specified column
        count00 = genotype_columns.loc[row, '0|0']
        # convert count value to an integer
        count00 = int(count00)
        for count in range(count00):
            for value in [0, 0]:
                # add haplotype to single row haplotype list
                single_variant_haplotype_list.append(int(value))

        # extract the value from the row for a specified column
        count01 = genotype_columns.loc[row, '0|1']
        # convert count value to an integer
        count01 = int(count01)
        for count in range(count01):
            for value in [0, 1]:
                # add haplotype to single row haplotype list
                single_variant_haplotype_list.append(int(value))

        # extract the value from the row for a specified column
        count10 = genotype_columns.loc[row, '1|0']
        # convert count value to an integer
        count10 = int(count10)
        for count in range(count10):
            for value in [1, 0]:
                # add haplotype to single row haplotype list
                single_variant_haplotype_list.append(int(value))

        # extract the value from the row for a specified column
        count11 = genotype_columns.loc[row, '1|1']
        # convert count value to an integer
        count11 = int(count11)
        for count in range(count11):
            for value in [1, 1]:
                # add haplotype to single row haplotype list
                single_variant_haplotype_list.append(int(value))

        # append the haplotype list for the row/variant to the total haplotype list
        ALL_HAPLOTYPE_LIST.append(single_variant_haplotype_list)

    return ALL_HAPLOTYPE_LIST


############################### GENOTYPE LIST ###############################


def genotype_list(dataframe):
    '''takes a dataframe as input and outputs a genotype list'''
    # initiate empty genotype column dataframe with specified column headers
    genotype_columns = dataframe[['0|0', '0|1', '1|0', '1|1']]

    # extract the row names/indices from the dataframe
    row_labels = list(genotype_columns.index)

    # initiate an empty genotype list
    GENOTYPE_LIST = []

    # for each row/variant, create a genotype list
    for row in row_labels:
        # initiate single row/variant genotype list
        single_variant_genotype_list = []

        # extract the value from the row for a specified column
        count00 = genotype_columns.loc[row, '0|0']
        # convert count value to an integer
        count00 = int(count00)
        for count in range(count00):
            # append genotype to single row/variant genotype list
            single_variant_genotype_list.append([0, 0])

        # extract the value from the row for a specified column
        count01 = genotype_columns.loc[row, '0|1']
        # convert count value to an integer
        count01 = int(count01)
        for count in range(count01):
            # append genotype to single row/variant genotype list
            single_variant_genotype_list.append([0, 1])

        # extract the value from the row for a specified column
        count10 = genotype_columns.loc[row, '1|0']
        # convert count value to an integer
        count10 = int(count10)
        for count in range(count10):
            single_variant_genotype_list.append([1, 0])

        # extract the value from the row for a specified column
        count11 = genotype_columns.loc[row, '1|1']
        # convert count value to an integer
        count11 = int(count11)
        for count in range(count11):
            single_variant_genotype_list.append([1, 1])

        # append the row/variant genotype to the total genotype list
        GENOTYPE_LIST.append(single_variant_genotype_list)

    return GENOTYPE_LIST


############################### NUCLOTIDE DIVERSITY ###############################

def nucleotide_diversity(genotype_list, start, end):
    ''' Using a genotype list and two genomic coordinates as input, outputs the nucleotide diversity for this DNA'''

    # import dependencies
    import allel

    # using the genotype list, create a genotype array
    g_array = allel.GenotypeArray(genotype_list)

    # using the genotype array, extract the allele counts
    AC = g_array.count_alleles()

    # initiate an empty position list
    pos = []
    # fills the pos list with values spanning from the start and end genomic coordinates specified.
    for x in range(start, end):
        pos.append(x)

    # calculate nucleotide diversity using the scikit-allel function allel.sequence_diversity()
    pi = allel.sequence_diversity(pos, AC)

    # return nucleotide diversity value
    return pi


############################ HAPLOTYPE DIVERSITY #############################

def haplotype_diversity(haplotypelist):
    ''' Calculating haplotype diversity with a haplotype list input '''

    # importing dependencies
    import allel

    # using the input haplotype list, generate a haplotype array
    h = allel.HaplotypeArray(haplotypelist, dtype='i1', copy=False)

    # from the haplotype array, calculate the haplotype diversity
    hd = allel.haplotype_diversity(h)

    # return the haplotype diversity
    return hd





################################### TAJIMA'S D ########################################

def Tajimas_D(genotype_list,POS):
    ''' Calculating Tajima's D with the genotype list and a list with the variant positions '''

    # import required dependencies
    import allel

    # producing a genotype array
    g_array = allel.GenotypeArray(genotype_list)

    # getting the allele counts
    AC = g_array.count_alleles()

    # calculating Tajima's D
    TD = allel.tajima_d(AC, pos = POS, min_sites=1)

    # returning Tajima's D value
    return TD

############################### HUDSON FST ###############################

def hudson_FST(pop1_genotype_list, pop2_genotype_list):
    ''' Calculating Hudsons FST with the genotype lists of two populations '''

    # import dependencies
    import allel
    import numpy as np

    # using the genotype lists, generate genotype array
    gt_pop1_array = allel.GenotypeArray(pop1_genotype_list)
    gt_pop2_array = allel.GenotypeArray(pop2_genotype_list)

    # get the allele counts from the arrays
    AC_pop1 = gt_pop1_array.count_alleles()
    AC_pop2 = gt_pop2_array.count_alleles()

    # get the numerator and denominator for the overall FST calculation
    num, den = allel.hudson_fst(AC_pop1, AC_pop2)

    #if the denominator is so small that numpy rounds it to zero, set the fst to 0.
    if np.sum(den) == 0:
        fst_average = 0
    # if the denominator does not equal zero, proceed with division calculation
    else:
        fst_average = np.sum(num) / np.sum(den)

    # if the FST value is nan, set to 0
    if np.isnan(fst_average) == True:
        fst = 0.0

    # return the fst
    return fst_average

######################################################################################
#################################### SQL stuff #######################################
######################################################################################

############################### SQL to Nucleotide Diversity ###############################

def SQLtoNucDiv(df, start, end):
    ''' Using a dataframe and genomic start and end coordinates as inputs, outputs nucleotide diversity'''

    # from the dataframe, produce a genotype list
    gen_list = genotype_list(df)

    # using the genotype list and start and end genomic coordinates, calculate the nucleotide diversity
    nuc_div = nucleotide_diversity(gen_list, start, end)

    # return the nucleotide diversity value
    return nuc_div


############################### WINDOWED NUCLEOTIDE DIVERSITY ###############################

def nuc_div_sliding(dataframe, window_size):
    '''Using a dataframe and window size as input, outputs a list of nucleotide diversity values for each window'''

    # import dependencies
    import math

    # resets the index of the input database
    dataframe = dataframe.reset_index()

    # initiate empty positions list
    POS = []

    # set the start position as the position value of the first row of the input dataframe
    start = dataframe.iloc[0]["position"]
    # set the end position as the position value of the last row of the input dataframe
    end = dataframe.iloc[-1]["position"]

    # fill the positions list with every integer between and including the start and end position
    for position in range(int(start),int(end)):
        POS.append(position)

    # save the length of the positions list to a variable
    length = len(POS)

    # set the start index to 0
    startindex = 0
    # set the end index to the window size - 1 (to account for pythons 0 starting indexing)
    endindex = window_size - 1
    # save length - 1 to a variable, which represents the highest the row index can go
    finalindex = length - 1

    # calculate the number of windows expected
    number_of_windows = math.floor(length / window_size) + 1

    # initiate an empty list for the window outputs
    window_outputs = []

    # for each window calculate nucleotide diversity
    for window in range(number_of_windows):
        if endindex <= finalindex:
            # extract dataframe where the variant positions are within the start and end positions of the window
            window_df = dataframe[dataframe["position"] < POS[endindex]]
            window_df = window_df[window_df["position"] >= POS[startindex]]

            # if there are no variants in the window, set the nucleotide diversity to 0
            if window_df.empty:
                nd = 0.0

            # if there are variants, calculate the nucleotide diversity for the window
            else:
                # create a genotype list for the window
                window_gen_list = genotype_list(window_df)
                # set nucleotide starting and ending position using the POS list
                nucleotide_start = POS[startindex]
                nucleotide_end = POS[endindex]

                # calculate the nucleotide diversity for the window
                nd = nucleotide_diversity(window_gen_list, nucleotide_start, nucleotide_end)

            # append the nucleotide diversity value of the window to the windowed nucleotide diversity list
            window_outputs.append(nd)

            # increase the start and end indices by the window size
            startindex += window_size
            endindex += window_size

    # return the windowed nucleotide diversity list
    return window_outputs


############################### SQL to Haplotype Diversity ###############################

def SQLtoHapDiv(df):
    ''' Using a dataframe as input, outputs the haplotype diversity'''

    # Using the dataframe, generate a haplotype list
    hap_list = haplotype_list(df)

    # Using the haplotype list, calculate the haplotype diversity
    hap_div = haplotype_diversity(hap_list)

    # return the haplotype diversity value
    return hap_div


############################### SQL to Windowed Haplotype Diversity ###############################

def SQLtoHapDiv_window(dataframe, window_size=10):
    '''Using a dataframe and (optional) window size as input, outputs a list of haplotype diversities for each window'''

    # import dependencies
    import math

    # reset input dataframe index
    dataframe = dataframe.reset_index()

    # initiate empty positions list
    POS = []

    # set the start position as the position value of the first row of the input dataframe
    start = dataframe.iloc[0]["position"]
    # set the end position as the position value of the last row of the input dataframe
    end = dataframe.iloc[-1]["position"]

    # fill the positions list with every integer between and including the start and end position
    for position in range(int(start), int(end)):
        POS.append(position)

    # save the length of the positions list to a variable
    length = len(POS)

    # set the start index to 0
    startindex = 0
    # set the end index to the window size - 1 (to account for pythons 0 starting indexing)
    endindex = window_size - 1
    # save length - 1 to a variable, which represents the highest the row index can go
    finalindex = length - 1

    # calculate the number of windows expected
    number_of_windows = math.floor(length / window_size) + 1

    # initiate an empty list for the window outputs
    window_outputs = []

    # for each window calculate haplotype diversity
    for window in range(number_of_windows):
        if endindex <= finalindex:
            # extract dataframe where the variant positions are within the start and end positions of the window
            window_df = dataframe[dataframe["position"] < POS[endindex]]
            window_df = window_df[window_df["position"] >= POS[startindex]]

            # if there are no variants in the window, set the haplotype diversity to 0
            if window_df.empty:
                hd = 0.0

            # if there are variants, calculate the haplotype diversity for the window
            else:
                # create a genotype list for the window
                window_gen_list = haplotype_list(window_df)

                # calculate the haplotype diversity for the window
                hd = haplotype_diversity(window_gen_list)
            # append the  nucleotide diversity value of the window to the windowed haplotype diversity list
            window_outputs.append(hd)

            # increase the start and end indices by the window size
            startindex += window_size
            endindex += window_size

    # return the windowed haplotype diversity list
    return window_outputs


############################### SQL TO TAJIMA'S D ###############################

def SQLtoTD(df):
    '''Using a dataframe as input, calculates Tajima's D'''

    # Using the dataframe, generate a genotype list
    gen_list = genotype_list(df)

    # initiate empty positions list
    POS = []

    # set the start position as the position value of the first row of the input dataframe
    start = df.iloc[0]["position"]
    # set the end position as the position value of the last row of the input dataframe
    end = df.iloc[-1]["position"]

    # fill the positions list with every integer between and including the start and end position
    for position in range(int(start), int(end)):
        POS.append(position)

    # calculate Tajima's D statistic using the genotype list and position list
    TD = Tajimas_D(gen_list,POS)

    # if the Tajima's D statistic calculated is nan, replace this value with 0
    if np.isnan(TD) == True:
        TD = 0.0

    # return the Tajima's D statistic
    return (TD)

############################### SQL TO WINDOWED TAJIMA'S D ###############################

def SQLtoTD_window(dataframe, window_size=10):
    ''' Using a dataframe and (optional) window size as input, returns a list of Tajima's D values for each window'''

    # import dependencies
    import numpy as np
    import math

    # resets the index of the input database
    dataframe = dataframe.reset_index()

    # initiate empty positions list
    POS = []

    # set the start position as the position value of the first row of the input dataframe
    start = dataframe.iloc[0]["position"]
    # set the end position as the position value of the last row of the input dataframe
    end = dataframe.iloc[-1]["position"]

    # fill the positions list with every integer between and including the start and end position
    for position in range(int(start), int(end)):
        POS.append(position)

    # save the length of the positions list to a variable
    length = len(POS)

    # set the start index to 0
    startindex = 0
    # set the end index to the window size - 1 (to account for pythons 0 starting indexing)
    endindex = window_size - 1
    # save length - 1 to a variable, which represents the highest the row index can go
    finalindex = length - 1

    # calculate the number of windows expected
    number_of_windows = math.floor(length / window_size) + 1

    # initiate an empty list for the window outputs
    window_outputs = []

    # for each window calculate Tajima's D
    for window in range(number_of_windows):
        if endindex <= finalindex:
            # extract dataframe where the variant positions are within the start and end positions of the window
            window_df = dataframe[dataframe["position"] < POS[endindex]]
            window_df = window_df[window_df["position"] >= POS[startindex]]

            # if there are no variants in the window, set the Tajima's D to 0
            if window_df.empty:
                td = 0.0

            # if there are variants, calculate Tajima's D for the window
            else:
                td = SQLtoTD(window_df)

            # append the  Tajima's D value of the window to the windowed Tajima's D list
            window_outputs.append(td)

            # increase the start and end indices by the window size
            startindex += window_size
            endindex += window_size

    # return the windowed Tajima's D list
    return window_outputs

############################### SQL TO FST ###############################

def SQLtoFST(df_pop1, df_pop2):
    ''' Using two population dataframes as input, calculates the FST value for the two populations'''

    # Using the first input dataframe, generate a genotype list for population 1
    gen_list_pop1 = genotype_list(df_pop1)

    # Using the second input dataframe, generate a genotype list for population 2
    gen_list_pop2 = genotype_list(df_pop2)

    # Using both genotype lists, calculate the FST value between the two populations
    FST = hudson_FST(gen_list_pop1, gen_list_pop2)

    # return the FST value
    return FST

############################### SQL TO WINDOWED FST ###############################

def SQLtoFST_window(df_pop1, df_pop2, window_size=10):
    ''' Using two population dataframes and (optional) window size as input, calculates windowed FST between the two populations'''

    # import dependencies
    import numpy as np
    import math

    # resets the index of the input dataframes
    df_pop1 = df_pop1.reset_index()
    df_pop2 = df_pop2.reset_index()

    # initiate empty positions list
    POS = []

    # set the start position as the position value of the first row of the input dataframe
    start = df_pop1.iloc[0]["position"]
    # set the end position as the position value of the last row of the input dataframe
    end = df_pop1.iloc[-1]["position"]

    # fill the positions list with every integer between and including the start and end position
    for position in range(int(start), int(end)):
        POS.append(position)

    # save the length of the positions list to a variable
    length = len(POS)

    # set the start index to 0
    startindex = 0
    # set the end index to the window size - 1 (to account for pythons 0 starting indexing)
    endindex = window_size - 1
    # save length - 1 to a variable, which represents the highest the row index can go
    finalindex = length - 1

    # calculate the number of windows expected
    number_of_windows = math.floor(length / window_size) + 1

    # initiate an empty list for the window outputs
    window_outputs = []

    # for each window calculate FST
    for window in range(number_of_windows):
        if endindex <= finalindex:

            # for population 1, extract dataframe where the variant positions are within the start and end positions of the window
            pop1_window_df = df_pop1[df_pop1["position"] < POS[endindex]]
            pop1_window_df = pop1_window_df[pop1_window_df["position"] >= POS[startindex]]

            # for population 2, extract dataframe where the variant positions are within the start and end positions of the window
            pop2_window_df = df_pop2[df_pop2["position"] < POS[endindex]]
            pop2_window_df = pop2_window_df[pop2_window_df["position"] >= POS[startindex]]

            # if there are no variants in the window, set the nucleotide diversity to 0
            if pop1_window_df.empty or pop2_window_df.empty:
                fst = 0.0

            # if there are variants, calculate the FST for the window
            else:
                fst = SQLtoFST(pop1_window_df,pop2_window_df)

            # append the  nucleotide diversity value of the window to the windowed FST list
            window_outputs.append(fst)

            # increase the start and end indices by the window size
            startindex += window_size
            endindex += window_size

    # return the windowed FST list
    return window_outputs
