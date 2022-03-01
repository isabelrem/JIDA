# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 22:00:54 2022

@author: dpava
"""

# The following functions work in flask, not python # For python queries, go to Validate_Search_Functions_python.py#


def search_term(gene,rs,start,end):
    '''
        Receives the user input from the forms in the order gene, rs, start, end, and returns a tuple
        containing the key search parameters to input in the sql query .
        The function checks if the user entered multiple illegal entries or no entries at all.'''

    # Variables to store the input to search sql
    search_1 = None   # for gene, rs or start
    search_2 = None   # for end 
    warning = None    # for message in case of error
    
    
    #List of inputs to check if they are empty
    inputs = [gene,rs,start,end]
        
    
    # Boolean to check if there is input
    no_input = True
    error = False
    
    #If the inputs contain searching terms we continue if not, a message is displayed
    for inp in inputs:
        if inp != "":
            no_input = False
    if no_input == True:
       
        error = True
        warning = 'No search term submitted'
    else: 
    
        #Checks for multiple entries, if there are an error is raised 
        if (gene != "") and (rs != ""):
            error = True 
            warning = "Please insert only one gene name or one rs value"
             
                
        elif (gene != "") and ((start != "") or (end != "")):
            error = True
            warning = "Please insert only one gene name or the start and end positions"
            
             
        elif (rs != "") and ((start != "") or (end != "")):
            error = True
            warning = "Please insert only one rs value or the start and end positions"
            
            
        elif ((start != "") and (end == "")) or ((start == "") and (end != "")):
            error = True 
            warning = "One position missing"
            
            
        else: 
        
        # if an error was found, an error is returned. 
            if error == True:
                search_1 = None
                search_2 = None

            else:

                # otherwise, the searched term is assigned to a variable
                if rs != "":
                    search_1 = rs
                elif gene != "":
                    search_1 = gene
                else:
                    search_1 = start
                    search_2 = end
    
    # returns empty values if there was an error and a message with the error, or the search term if successful.
    return search_1,search_2,warning



def query_select(search_1,search_2,gene,rs,start,end):
    
    '''Receives 6 parameters: two search terms with previous correctness checks from search_term()
        and 4 variables where the form data was introduced (gene,rs,start,end). It returns the query that corresponds
        to the type of input from the user. 
        The function has 3 pre-written queries and selects the correct one based on the type of data
        in the user input.'''


    # query for rs value search: 
    query_rs = f""" SELECT chr_id AS chromosome,
                gen_coor.position AS position, 
                snp.rs_value AS rs_value,
                name AS population,
                reference,
                alternate,
                sample_count,
                gt_00_count AS "0|0",
                gt_01_count AS "0|1",
                gt_10_count AS "1|0",
                gt_11_count AS "1|1"
                FROM snp_characteristics AS snpc
                INNER JOIN snp ON snpc.rs_value = snp.rs_value
                INNER JOIN population ON snpc.pop_id = population.id
                INNER JOIN gen_coor ON gen_coor.position = snp.position
                WHERE snp.rs_value = '{rs}' """

    # query for gene name search
    query_gene = f""" SELECT chr_id as chromosome,
                gen_coor.position AS position, 
                snp.rs_value AS rs_value,
                name AS population,
                reference,
                alternate,
                sample_count,
                gt_00_count AS "0|0",
                gt_01_count AS "0|1",
                gt_10_count AS "1|0",
                gt_11_count AS "1|1"
                FROM snp_characteristics AS snpc
                INNER JOIN snp ON snpc.rs_value = snp.rs_value
                INNER JOIN population ON snpc.pop_id = population.id
                INNER JOIN gen_coor ON gen_coor.position = snp.position
                INNER JOIN gene ON gen_coor.gene_id = gene.id
                WHERE gene.id = '{gene}' """

    # query for gene alias search 
    query_alias = f"""SELECT chr_id as chromosome,
                gen_coor.position AS position, 
                snp.rs_value AS rs_value,
                name AS population,
                reference,
                alternate,
                sample_count,
                gt_00_count AS "0|0",
                gt_01_count AS "0|1",
                gt_10_count AS "1|0",
                gt_11_count AS "1|1"
                FROM snp_characteristics AS snpc
                INNER JOIN snp ON snpc.rs_value = snp.rs_value
                INNER JOIN population ON snpc.pop_id = population.id
                INNER JOIN gen_coor ON gen_coor.position = snp.position
                INNER JOIN gene ON gen_coor.gene_id = gene.id
                INNER JOIN gene_alias ON gene.id = gene_alias.gene_id
                INNER JOIN alias ON gene_alias.alias_id = alias.id
                WHERE alias.id = '{gene}' """

    # query for position search
    query_pos = f""" SELECT chr_id as chromosome,
                gen_coor.position AS position, 
                snp.rs_value AS rs_value,
                name AS population,
                reference,
                alternate,
                sample_count,
                gt_00_count AS "0|0",
                gt_01_count AS "0|1",
                gt_10_count AS "1|0",
                gt_11_count AS "1|1"
                FROM snp_characteristics AS snpc
                INNER JOIN snp ON snpc.rs_value = snp.rs_value
                INNER JOIN population ON snpc.pop_id = population.id
                INNER JOIN gen_coor ON gen_coor.position = snp.position
                WHERE snp.position BETWEEN {start} AND {end} """
    
    # Dictionary storing the queries where keys are the name of query and values are the queries.    
    query_dic = {
                "query_rs":query_rs,
                "query_gene":query_gene,
                "query_pos":query_pos,
                "query_alias":query_alias
                }

    # List of known genes to decide between a gene or an alias search
    list_gene = ['NCOR1P4', 'U1', 'LINC01667', 'RN7SL52P', 'SNORA70', 'CDRT15P8', 'BAGE2', 'TPTE', 'SLC25A15P4', 'ABCC13', 'HSPA13', 'SAMSN1', 'POLR2CP1', 'GAPDHP16', 'RBMX2P1', 'NRIP1', 'CYCSP42', 'RNU6-1326P', 'RAD23BP3', 'USP25', 'MIR99AHG', 'VDAC2P1', 'SNORD74B', 'MIR99A', 'MIRLET7C', 'MIR125B2', 'RNU1-98P', 'NEK4P1', 'RNU6-113P', 'LINC01549', 'RPL39P40', 'RN7SL163P', 'CXADR', 'BTG3', 'BTG3-AS1', 'C21orf91-OT1', 'C21orf91', 'CHODL-AS1', 'RPL37P3', 'CHODL', 'TMPRSS15', 'MIR548XHG', 'PPIAP22', 'SLC6A6P1', 'RNU1-139P', 'RPL37P4', 'NIPA2P3', 'SREK1IP1P1', 'C1QBPP1', 'LINC01683', 'LINC02573', 'RNU6-772P', 'RN7SKP147', 'FDPSP6', 'KRT18P2', 'RPS3AP1', 'LINC00320', 'PPIAP1', 'NCAM2', 'LINC00317', 'LINC01425', 'LINC01687', 'LINC00308', 'RNU4-45P', 'MAPK6P2', 'ZNF299P', 'RNU2-55P', 'D21S2088E', 'EEF1A1P1', 'Y_RNA', 'LINC01689', 'LINC01684', 'LINC01692', 'RPL13AP7', 'LINC00158', 'MIR155HG', 'MRPL39', 'JAM2', 'ATP5PF', 'GABPA', 'APP', 'APP-DT', 'RNU6-926P', 'CYYR1-AS1', 'CYYR1', 'ADAMTS1', 'ADAMTS5', 'GPX1P2', 'RPL10P1', 'NCSTNP1', 'LINC01673', 'LINC00113', 'LINC00314', 'LINC01697', 'LINC01695', 'LINC00161', 'U6', 'N6AMT1', 'HSPD1P7', 'THUMPD1P1', 'LTN1', 'RPL23P2', 'RWDD2B', 'USP16', 'CCT8', 'MAP3K7CL', 'U3', 'LINC00189', 'BACH1', 'GRIK1', 'CLDN17', 'LINC00307', 'CLDN8', 'RPL8P2', 'KRTAP24-1', 'KRTAP25-1', 'KRTAP26-1', 'KRTAP27-1', 'KRTAP23-1', 'KRTAP13-6P', 'KRTAP13-2', 'MIR4327', 'KRTAP13-1', 'KRTAP13-3', 'KRTAP13-4', 'KRTAP13-5P', 'KRTAP15-1', 'KRTAP19-1', 'KRTAP19-2', 'KRTAP19-3', 'KRTAP19-4', 'KRTAP19-5', 'KRTAP19-9P', 'KRTAP19-10P', 'KRTAP19-11P', 'KRTAP19-6', 'KRTAP19-7', 'KRTAP22-2', 'KRTAP6-3', 'KRTAP6-2', 'KRTAP22-1', 'KRTAP6-1', 'KRTAP20-1', 'KRTAP20-4', 'KRTAP20-2', 'KRTAP20-3', 'KRTAP21-3', 'KRTAP21-4P', 'KRTAP21-2', 'KRTAP21-1', 'KRTAP8-2P', 'KRTAP8-3P', 'KRTAP8-1', 'KRTAP7-1', 'KRTAP11-1', 'KRTAP19-8', 'UBE3AP2', 'TIAM1', 'FBXW11P1', 'SOD1', 'SCAF4', 'TPT1P1', 'HUNK', 'LINC00159', 'MIS18A', 'MIS18A-AS1', 'MRAP', 'URB1', 'URB1-AS1', 'CFAP298-TCP10L', 'EVA1C', 'TCP10L', 'CFAP298', 'OR7E23P', 'SYNJ1', 'PAXBP1-AS1', 'PAXBP1', 'C21orf62-AS1', 'C21orf62', 'OLIG2', 'OLIG1', 'LINC01548', 'IFNAR2', 'IL10RB-DT', 'IL10RB', 'IFNAR1', 'IFNGR2', 'TMEM50B', 'RPS5P3', 'DNAJC28', 'GART', 'SON', 'DONSON', 'CRYZL1', 'ITSN1', 'ATP5PO', 'LINC00649', 'MRPS6', 'SLC5A3', 'RPS5P2', 'LINC00310', 'KCNE2', 'SMIM11A', 'SMIM34A', 'KCNE1', 'RCAN1', 'CLIC6', 'LINC00160', 'LINC01426', 'RUNX1', 'LINC01436', 'RPL23AP3', 'SETD4', 'CBR1', 'MEMO1P1', 'CBR3-AS1', 'RPS9P1', 'CBR3', 'DOP1B', 'SRSF9P1', 'MORC3', 'CHAF1B', 'CLDN14', 'SIM2', 'HLCS', 'MRPL20P1', 'RIPPLY3', 'RNU6-696P', 'PIGP', 'TTC3', 'DSCR9', 'VPS26C', 'DYRK1A', 'KCNJ6', 'DSCR8', 'KCNJ15', 'LINC01423', 'ERG', 'LINC00114', 'ETS2', 'LINC01700', 'RPL23AP12', 'PCBP2P1', 'PSMG1', 'BRWD1', 'BRWD1-AS1', 'HMGN1', 'RNF6P1', 'GET1', 'LCA5L', 'SH3BGR', 'JCADP1', 'B3GALT5', 'IGSF5', 'PCP4', 'DSCAM', 'YRDCP3', 'LINC00323', 'MIR3197', 'BACE2', 'FAM3B', 'MX2', 'MX1', 'TMPRSS2', 'PCSEAT', 'LINC00111', 'LINC00479', 'LINC00112', 'RIPK4', 'PRDM15', 'C2CD2', 'ZBTB21', 'ZNF295-AS1', 'UMODL1', 'ABCG1', 'TFF3', 'TFF2', 'TFF1', 'TMPRSS3', 'UBASH3A', 'RSPH1', 'SLC37A1', 'LINC01671', 'PDE9A', 'LINC01668', 'WDR4', 'NDUFV3', 'ERVH48-1', 'MIR5692B', 'PKNOX1', 'CBS', 'U2AF1', 'MRPL51P2', 'FRGCA', 'CRYAA', 'LINC00322', 'LINC01679', 'SIK1', 'LINC00319', 'LINC00313', 'HSF2BP', 'RRP1B', 'PDXK', 'CSTB', 'TMEM97P1', 'RRP1', 'AATBC', 'MYL6P1', 'AGPAT3', 'RNU6-1150P', 'TRAPPC10', 'PWP2', 'GATD3A', 'ICOSLG', 'DNMT3L', 'AIRE', 'PFKL', 'CFAP410', 'TRPM2', 'LRRC3-DT', 'LRRC3', 'MTCYBP21', 'MTND6P21', 'MTND5P1', 'LINC02575', 'TSPEAR', 'UBE2G2', 'LINC01424', 'SUMO3', 'PTTG1IP', 'ITGB2', 'LINC01547', 'FAM207A', 'LINC00163', 'LINC00165', 'PICSAR', 'SSR4P1', 'ADARB1', 'LINC00334', 'POFUT2', 'LINC00205', 'LINC00315', 'LINC00316', 'MTCO1P3', 'COL18A1', 'SLC19A1', 'LINC01694', 'PCBP3', 'COL6A1', 'PSMA6P3', 'COL6A2', 'FTCD', 'SPATC1L', 'LSS', 'MCM3AP-AS1', 'MCM3AP', 'YBEY', 'C21orf58', 'PCNT', 'DIP2A', 'S100B', 'PRMT2', 'RPL23AP4']

    
    # Conditional that compares the filtered input vs all the inputs and selects the query based on the user input 
    if search_1 == rs:
        query = query_dic['query_rs']
        
    elif search_1 == gene:
        
        #if query is by gene, the input is looked for in a list to select gene query
        if gene in list_gene:
            query = query_dic['query_gene']
            
        #otherwise, the gene query stays as introduced and searches by alias
        else:
            query = query_dic['query_alias']
    else:
        query = query_dic['query_pos']
        

    # Returns the correct query and if the query is gene or alias related
    return query

    
def window_check(Window,start,end):
    ''' Checks the window size and makes sure it is not greater than the difference between genomic coordinates. 

    Parameters 
    ----------
    Window: int 
    start : int
    end: int

    ''' 
  
    # error message 
    message = None

    # difference in genomic coordinates
    if (end - start) >2:
        if ((end - start) < Window) or (Window < 3):
            message = "Window size is greater than the distance between start and end positions.\
                 | Window= " + str(Window) + ", position distance= " + str(end-start)


    return message


