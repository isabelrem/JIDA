
SQLtoFST(df_pop1, df_pop2)
Using two population dataframes as input, calculates the FST value for the two populations.
 
Parameters
----------
 
df_pop1: a pandas dataframe containing variant data from only 1 population, created using the python pandas library.
df_pop2: a pandas dataframe containing variant data from only 1 population, created using the python pandas library.
 
 
Description
-----------
 
Recieves 2 parameters, one pandas dataframe for one population, another pandas dataframe for a second population.
The FST statistic is calculated across both dataframes.
Calculating the FST for each window uses the pre-written functions genotype_list() and hudson_FST().
This function depends on the python packages/modules scikit-allel, pandas, numpy.
 
Returns
-------
 
A list of FST values calculated for each window.
SQLtoFST_window(df_pop1, df_pop2, window_size=10)
Using two population dataframes and (optional) window size as input, calculates windowed FST between the two populations.
 
Parameters
----------
 
df_pop1: a pandas dataframe containing variant data from only 1 population, created using the python pandas library.
df_pop2: a pandas dataframe containing variant data from only 1 population, created using the python pandas library.
window_size: int
 
Description
-----------
 
Recieves 3 parameters, one pandas dataframe for one population, another pandas dataframe for a second population, and a window_size.
Using the window_size integer, the both population dataframes are subset into windows and the FST statistic is calculated across the window using both dataframes.
Calculating the FST for each window uses the pre-written functions SQLtoFST().
This function depends on the python packages/modules scikit-allel, pandas, numpy and math.
 
Returns
-------
 
A list of FST values calculated for each window.
SQLtoHapDiv(df)
Using a dataframe as input, outputs the haplotype diversity
 
Parameters
----------
 
dataframe: a pandas dataframe, created using the python pandas library.
 
Description
-----------
 
Recieves 1 parameter, a pandas dataframe. The haplotype diversity is calculated across the dataframe.
Calculating haplotype diversity uses the pre-written functions haplotype_list() and haplotype_diversity().
This function depends on the python packages/modules scikit-allel, pandas.
 
Returns
-------
 
A haplotype diversity value.
SQLtoHapDiv_window(dataframe, window_size=10)
Using a dataframe and (optional) window size as input, outputs a list of haplotype diversities for each window
 
Parameters
----------
 
dataframe: a pandas dataframe, created using the python pandas library.
window_size: int
 
Description
-----------
 
Recieves 2 parameters, a pandas dataframe and a window_size. Using the window_size integer, the dataframe is subset into windows and the haplotype diversity is calculated across the window.
Calculating haplotype diversity for the windows uses the pre-written functions haplotype_list() and haplotype_diversity().
This function depends on the python packages/modules scikit-allel, pandas and math.
 
Returns
-------
 
A list of haplotype diversity values calculated for each window.
SQLtoNucDiv(df, start, end)
Using a dataframe and genomic start and end coordinates as inputs, outputs nucleotide diversity.
 
Parameters
----------
dataframe: a pandas dataframe, created using the python pandas library.
start: int, the genomic position to begin the search at.
end: int, the genomic position to end the search at.
Description
-----------
Recieves 3 parameters, a pandas dataframe and start and end genomic positions.
The nucleotide diversity is calculated across the dataframe.
Calculating nucleotide diversity for the windows uses the pre-written functions genotype_list() and nucleotide_diversity().
This function depends on the python packages/modules scikit-allel, pandas.
Returns
-------
A nucleotide diversity value for between the specified start and end genomic positions.
SQLtoPandasViaPOS(database, table, start, end)
Using the inputs of a database name, table name, and start and end genomic coordinates, produces a pandas dataframe
SQLtoTD(df)
Using a dataframe as input, calculates Tajima's D.
 
 Parameters
----------
 
dataframe: a pandas dataframe, created using the python pandas library.
 
Description
-----------
 
Recieves 1 parameter, a pandas dataframe. The Tajima's D statistic is calculated across the dataframe.
Calculating Tajima's D uses the pre-written functions Tajimas_D() and genotype_list.
This function depends on the python packages/modules scikit-allel, pandas, numpy.
 
Returns
-------
 
A Tajima's D value.
SQLtoTD_window(dataframe, window_size=10)
Using a dataframe and (optional) window size as input, returns a list of Tajima's D values for each window.
 
Parameters
----------
 
dataframe: a pandas dataframe, created using the python pandas library.
window_size: int
 
Description
-----------
 
Recieves 2 parameters, a pandas dataframe and a window_size. Using the window_size integer, the dataframe is subset into windows and the Tajima's D statistic is calculated across the window.
Calculating Tajima's D for each window uses the pre-written functions SQLtoTD().
This function depends on the python packages/modules scikit-allel, pandas, numpy and math.
 
Returns
-------
 
A list of Tajima's D values calculated for each window.
Tajimas_D(genotype_list, POS)
Calculates Tajima's D
Parameters
----------
genotype_list: list
POS: list
Description
-----------
Converts the genotype list into a genotype array and extracts the allele counts. Using the SciKit Allel function
tajima d the allele count and variant position list is inserted, the minimum segregated sites selected is 1.
Returns
-------
Single Tajima's D value
genotype_list(dataframe)
Produces a genotype list from a dataframe
Parameters
----------
dataframe: dataframe
Description
-----------
From the dataframe the phased genotype frequency columns are extracted. For each row the value of the counter is
the number of times the phased genotype is appended to the list. This runs through each phased genotype column.
Returns
-------
Genotype list
haplotype_diversity(haplotypelist)
Calculates haplotype diversity
Parameters
----------
haplotypelist: list
Description
-----------
Converts the haplotype list into a haplotype array. The haplotype array is inserted in the haplotype diversity
function from SciKit Allel.
Returns
-------
Single haplotype diversity value
haplotype_list(dataframe)
Produces a haplotype list from a dataframe
Parameters
----------
dataframe: dataframe
Description
-----------
From the dataframe the phased genotype frequency columns are extracted. For each row the value of the counter is
the number of times the phased genotype is appended to the list. Both the alleles are appended to the haplotype list.
This runs through each phased genotype column.
Returns
-------
Haplotype list
hudson_FST(pop1_genotype_list, pop2_genotype_list)
Calculates Hudson FST
Parameters
----------
pop1_genotype_list: list
pop2_genotype_list: list
Description
-----------
Converts the genotype lists for both populations into a genotype arrays and extracts the allele counts. Using the
hudson fst function from SciKit Allel the numerator and denominator values are extracted. If the denominator value
is 0, then the FST value is returned as 0. Otherwise, FST is calculated by dividing the sum of the numerator and
denominator. If NaN is returned then the FST value is returned as 0.
Returns
-------
Single Hudson FST value
nuc_div_sliding(dataframe, window_size)
Using a dataframe and window size as input, outputs a list of nucleotide diversity values for each window
Parameters
----------
dataframe: a pandas dataframe, created using the python pandas library.
window_size: int
Description
-----------
Recieves 2 parameters, a pandas dataframe and a window_size. Using the window_size integer, the dataframe is subset into windows and the nucleotide diversity is calculated across the window.
Calculating nucleotide diversity for the windows uses the pre-written functions genotype_list() and nucleotide_diversity().
This function depends on the python packages/modules scikit-allel, pandas and math.
Returns
-------
A list of nucleotide diversity values calculated for each window.
nucleotide_diversity(genotype_list, start, end)
Calculates nucleotide diversity
Parameters
----------
genotype_list: list
start: int
end: int
Description
-----------
Converts the genotype list into a genotype array and extracts the allele counts. Using the start and end genomic
position inputs a variant position list is produced. Using the sequence diversity function from SciKit Allel
the variant position and allele counts are inserted.
Returns
-------
Single nucleotide diversity value
