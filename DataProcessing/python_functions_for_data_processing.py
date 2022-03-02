########## VCF TO PANDAS DATAFRAME ##########  

def VCFtoPandas(infile):
    ''' converts VCF to pandas dataframe: from https://stackoverflow.com/questions/70219758/vcf-data-to-pandas-dataframe
    
    Parameters
    ----------
    
    infile: str
    
    
    Description
    -----------
    
    Takes 1 parameter, the path to a VCF file. Opens the VCF file and extracts lines that begin with #CHROM only. 
    Tab separate the data and convert it to a pandas dataframe.
    This function depends on the python packages/modules pandas.
    
    Returns
    -------
    
    A pandas dataframe
    
    '''

    # import dependencies
    import pandas as pd
    print("dependencies imported")

    # produce db from VCf file specified
    with open(infile, "r") as f:
        lines = f.readlines()
        chrom_index = [i for i, line in enumerate(lines) if line.strip().startswith("#CHROM")]
        data = lines[chrom_index[0]:]
    print("VCF opened")

    # set headers and database content
    header = data[0].strip().split("\t")
    informations = [d.strip().split("\t") for d in data[1:]]

    # convert content to pandas dataframe
    print("pandas df created")
    return pd.DataFrame(informations, columns=header)


########## VCF TO SNP TABLE CSV ##########  


def VCF_to_snp(inVCF, outCSV, start, end):
    '''converting multiple population VCFs to a combined SNP CSV, removing multi-allelic sites. 
    
    Parameters
    ----------
    
    inVCF: str, path to a population VCF for the chromosome.
    outCSV: str, path to output CSV containing variant information for the chromosome.
    start: int, index at which to start the subset dataframe
    end: int, index at which to end the subset dataframe
    
    
    Description
    -----------
    
    Receives 4 parameters: the path to a VCF, the path to an output CSV and start and end index values.
    Converts the VCF to a dataframe, and then subsets that dataframe based on the start and end indices specified.
    Once subset, multiallelic sites are removed from the dataframe.
    The columns are then reduced to just 'chromsome','position','rs_value','reference','alternate'.
    The resultant dataframe is then written to a CSV, using the path specified by outCSV and the start and end indices.
    Converting the VCF to a dataframe uses the pre-written function VCFtoPandas().
    This function depends on the python packages/modules pandas, os, pathlib
    
    
    Returns
    -------
    One csv file with the columns 'chromsome','position','rs_value','reference','alternate', for the range specified by the start and end parameters.
    
    '''

    # import dependencies
    import pandas as pd
    import os
    from pathlib import Path

    # iterate over the 5 population vcfs
    for inVCF, outCSV in zip(inputlist,outputlist):

        # check inputs
        print("process started...")
        print(inVCF)

        # create dataframe
        df = VCFtoPandas(inVCF)
        print("dataframe created")

        # rename columns in accordance with SQL schema
        df.rename(columns={'#CHROM': 'chromosome', 'POS': 'position', 'ID': 'rs_value', 'REF': 'reference', 'ALT': 'alternate'}, inplace=True)

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
        df_info = df.filter(['rs_value'], axis=1)

        print("data filtered")


        # filter dataframe to just the desired columns
        df = df.filter(['chromsome','position','rs_value','reference','alternate'])
        
        df.to_csv(outCSV, index = False)
        

########## VCF TO SNP CHARACTERISTICS TABLE CSV ##########  

def VCF_to_snp_characteristics(inputlist, outputlist, popcodelist, start, end):
    '''converting multiple population VCFs to a combined SNP characterisitcs CSV, removing multi-allelic sites.
    
    Parameters
    ----------
    
    inputlist: list of strings in which each string is the file path to a population VCF.
    outputlist: list of strings in which each string is the file path to an output population CSV.
    popcodelist: list of strings, in which each string is a three letter population code.
    start: int, index at which to start the subset dataframe.
    end: int, index at which to end the subset dataframe.
    
    
    Description
    -----------
    
    Receives 5 parameters: the paths to population VCFs, the paths to output population CSVs, a list of population codes and 
     start and end index values.
    Each population VCF is converted to a pandas dataframe, and then subset that based on the start and end indices specified.
    Once subset, multiallelic sites are removed from each dataframe. The dataframes are filtered to just the 'rs_value'
     column, while a new dataframe is created in which the sample count and calculated phased genotype counts are stored.
     Following these calculations, the two dataframes per population are fused together, and written to CSV.
    Converting the VCF to a dataframe uses the pre-written function VCFtoPandas().
    This function depends on the python packages/modules pandas, os, pathlib, glob. 
    
    Returns
    -------
    
    (1) a csv for each population, containing the rs_value, sample count and phased genotype counts.
    (2) a csv made from the combination of each population csv.
    
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

        # shorten the df
        #df = df.loc[start:]

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

        length = len(df)
        totallength = length * 5
        print(length)
        print(totallength)
        print(emergencystop)

        # extract updated row names
        row_labels_df = list(df.index)


        # remove unwanted columns
        df_info = df.filter(['rs_value'], axis=1)

        print("data filtered")

        # filter dataframe to just the sample columns
        sample_cols = [col for col in df if col.startswith('HG')]
        print("columns filtered")
        df_samples = df[sample_cols]
        #print(df_samples)

        # delete df to free up memory
        del df

        # initiate new df
        more_info = pd.DataFrame(columns=('population', 'sample_count', 'gt_00_count', 'gt_01_count', 'gt_10_count', 'gt_11_count'))


        # fill more info df
        for row in row_labels_df:
            sample_count = 0
            gt_00_count = 0
            gt_01_count = 0
            gt_10_count = 0
            gt_11_count = 0
            for column in df_samples:
                gt = df_samples.loc[row, column]
                if gt == '0|0':
                    sample_count += 1
                    gt_00_count += 1
                elif gt == '0|1':
                    sample_count += 1
                    gt_01_count += 1
                elif gt == '1|0':
                    sample_count += 1
                    gt_10_count += 1
                elif gt == '1|1':
                    sample_count += 1
                    gt_10_count += 1
            more_info = more_info.append({'population': popcode, 'sample_count': sample_count, 'gt_00_count': gt_00_count,
                                              'gt_01_count': gt_01_count, 'gt_10_count': gt_10_count,
                                              'gt_11_count': gt_11_count}, ignore_index=True)
            print("row added")


        df_final = pd.concat([df_info, more_info], axis=1)
        print("concatenation done")


        filepath = Path(outCSV)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df_final.to_csv(filepath,index = False)

        # delete dataframe(s) and free memory
        del df_info
        del df_samples
        del df_final
        del more_info

    import glob
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    # combine all files in the list
    combined = pd.concat([pd.read_csv(f, dtype={'rs_value': 'str',
                                                 'population': 'str',
                                                'sample_count': 'str', 'gt_00_count': 'str', 'gt_01_count': 'str',
                                                'gt_10_count': 'str', 'gt_11_count': 'str'}) for f in all_filenames])
    # export to csv
    filename = "snp_characteristics" + str(start) + "-" + str(end) + ".csv"
    combined.to_csv(filename, index=False, encoding='utf-8-sig')
    
    
########## GENOMIC POSITION TO GENE NAME ##########    

def genomic_position_to_gene_name(chromosome, genome_position):
    """" Extracting gene name from genome position using pyensembl 
    
    Parameters
    ----------
    
    chromosome: int
    genome_position: int
    
    
    Description
    -----------
    
    Using the chromsome and genome position specified, connects to the ensembl database and extracts the gene name
     associated with the position (if there is one present). 
    This function depends on the python packages/modules pandas, and pyensembl.
     
    
    Returns
    -------
    
    Returns as a tuple the genome position and its associated gene name.
    
    
    """

    # Import the required dependencies
    import pyensembl
    import pandas as pd

    # The ensembl database called the object ensembl
    ensembl = pyensembl.EnsemblRelease()

    genes = ensembl.genes_at_locus(contig=chromosome, position=genome_position)

    # Finding the gene at a particular location
    # contig - the chromosome we are interested in
    # e.g. pos - 18714230, gene name - MIR548XHG
    gene_info = genes[0]


    # extracting out all the information and placing them in a dictionary
    gene_info_dict = {"gene_id": gene_info.gene_id,
                      "gene_name": gene_info.gene_name,
                      "biotype": gene_info.biotype,
                      "contig": gene_info.contig,
                      "start": gene_info.start,
                      "end": gene_info.end,
                      "strand": gene_info.strand,
                      "genome": gene_info.genome}
    name = gene_info_dict['gene_name']

    # returning the dictionary
    return genome_position,name

################ GENE ALIAS ################

def gene_aliases(gene_name):
    ''' Converted from genomic position to gene name using PyEnsembl

    Parameters
    ----------
    gene_name: str

    Description
    -----------
    The main body of the code was extracted from biostars (https://www.biostars.org/p/126277/). Minor changes were made
    where the alias list produced could be indexed and spaces could be removed.

    Returns
    -------
    A list of gene aliases'''

    # import the required dependencies
    import json
    from Bio import Entrez
    Entrez.email = "bt211032@qmul.ac.uk"

    most_likely_entry = Entrez.esearch(db="gene",term="{gene_name} [Preferred Symbol] AND 9606 [Taxonomy ID]".format(gene_name=gene_name),retmode="json")
    most_likely_entry_json = json.loads(most_likely_entry.read())
    my_ids = most_likely_entry_json['esearchresult']['idlist']
    if my_ids == []:
        all_ids_entries =  Entrez.esearch(db="gene",term="{gene_name} AND 9606 [Taxonomy ID]".format(gene_name=gene_name),retmode="json")
        all_ids_json = json.loads(all_ids_entries.read())
        all_ids = all_ids_json['esearchresult']['idlist']
        # print all_ids
        for an_iden in all_ids:
            record_with_aliases = Entrez.efetch(db="gene",id=an_iden,retmode="json")
            aliases = []
            for line in record_with_aliases:
                if line.startswith("Official Symbol:"):
                    aliases.append(line.split("and Name")[0].split(":")[1])
                if line.startswith("Other Aliases:"):
                    for x in [y.strip() for y in [x.strip() for x in line.split(":")[1:]][0].split(",")]:
                        aliases.append(x)
                    # print aliases
                    if gene_name in aliases:
                        return aliases[0]
                    elif gene_name.replace(" ","") in aliases:
                        return aliases[0]
                    elif gene_name.replace("-","") in aliases:
                        return aliases[0]
                    else:
                        continue
        print("not found :)")
        return "NOT FOUND"
    else:
        # We got the ID with the Preferred Symbol lookup
        print("Got ID:",my_ids)
        for an_iden in my_ids:

            # add an empty list to add the aliases to
            gene_aliases_list = []

            record_with_aliases = Entrez.efetch(db="gene",id=an_iden,retmode="json")
            for line in record_with_aliases:
                print(line)
                if line.startswith("Other Aliases:"):
                    print(line.split(":")[1:])
                    alias_list = line.split(":")[1:]

                    ####### JANEESH ADDED CODE #######

                    # extracting each gene name and extending to the gene alias list
                    for element in alias_list:
                        # splitting according to commas
                        word = element.split(", ")
                        # extending the list with the alias
                        gene_aliases_list.extend(word)
                    # removing the spaces in the first alias
                    first_value = gene_aliases_list[0]
                    gene_aliases_list[0] = first_value.replace(" ", "")
                    # removing the \n in the last alias
                    last_value = gene_aliases_list[-1]
                    gene_aliases_list[-1] = last_value.rstrip("\n")

                    ###################################

            entry = record_with_aliases.read()
            print(entry)
            return gene_aliases_list


