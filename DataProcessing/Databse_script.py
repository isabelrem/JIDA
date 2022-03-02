import sqlite3


''' The following script was used to create and populate the database SNPB (1).db based on the schema found in the github.

    The database comprises 8 tables joining the main components from genomic position to snp characteristics in a manner.
    Tables are: snp, population, snp_characteristics, gen_coor, chromosome, gene, gene_alias, and gene. 
    Each table was populated with a series of csvs produced from either 1000 genomes project vcf data from chromosome 21
    and custom-made csvs including gene names, gene aliases, chromosome positions and population information.
    
    The script was divided into sections:
        1. Creating/Connecting the database
        2. Creating tables
        3. Creating indexes
        4. Queries 
        
    Note: Many lines are silenced given that they are frequently used to append or replace data in the tables. 
    
    
'''

### List of commands to populate the database ### 
# retrieving csv into a pandas df
#snp_csv = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/snp/6-snptable1000000-.csv')
#snpc_csv = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/snp_characteristics/4fix-snp_characteristics1000001-end.csv')
#pop_csv = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/population_table.csv')
#chrom_csv = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/chromosome.csv')
#gencoor_csv = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/gen_coor.csv')
#gene_csv = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/gene_table.csv')
#gene_al = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/gene_aliases_final.csv')
#alias_csv = pd.read_csv('C:/Users/dpava/Dropbox/LAPP/Queens/Software Group Project/csv files/gene_alias.csv')

#################### 1. Creating/Connecting to the database ###################

# define connection to the db (or create it if it doesn't exist)
conn = sqlite3.connect('SNPB (1).db')

# creates a cursor, something that lets us interact with the db in sql language
cur = conn.cursor()

####################### 2. CREATING TABLES ####################################

# Create snp table
create_snp = """ CREATE TABLE IF NOT EXISTS
	snp (position INTEGER,
		rs_value TEXT(20) PRIMARY KEY,
		reference TEXT(1),
		alternate TEXT(1),
		gene_id TEXT(20),
        FOREIGN KEY (position) REFERENCES gen_coor(position)) """

#Adds snp table to the database
cur.execute(create_snp)

#fill table with data
#t1 = snp_csv.to_sql('snp',conn,if_exists='append',index=False)  
#To append new csvs change the 'replace' for 'append' 

# Save changes 
conn.commit()

#create population table 

create_pop = """ CREATE TABLE IF NOT EXISTS
    population (id TEXT(3) PRIMARY KEY,
                name TEXT(30),
                details TEXT)"""
    
#Adds population to the database
cur.execute(create_pop)

#fill table with data
#t2 = pop_csv.to_sql('population',conn,if_exists='replace',index=False)

# Save changes 
conn.commit()


#create snp_characteristics table
create_snpc = """ CREATE TABLE IF NOT EXISTS
	snp_characteristics (
	rs_value TEXT(20),
    pop_id TEXT(3),
	sample_count integer,
	gt_00_count integer,
	gt_01_count integer,
	gt_10_count integer, 
	gt_11_count integer,
	FOREIGN KEY (rs_value) REFERENCES snp(rs_value),
    FOREIGN KEY (pop_id) REFERENCES population(id))"""

#Adds snpc to the database
cur.execute(create_snpc)

#fill table with data
#t3 = snpc_csv.to_sql('snp_characteristics',conn,if_exists='append',index=False)

# Save changes 
conn.commit()


#Create genomic_coordinates table
create_genpos = """ CREATE TABLE IF NOT EXISTS
    gen_coor(position INTEGER PRIMARY KEY,
             chr_id TEXT(2),
             gene_id TEXT (30),
             FOREIGN KEY (chr_id) REFERENCES chromosome(id),
             FOREIGN KEY (gene_id) REFERENCES gene(id))"""

# Add gen_coor to the database
cur.execute(create_genpos)
#fill table with data
#t3 = gencoor_csv.to_sql('gen_coor',conn,if_exists='replace',index=False)

# Save changes 
conn.commit()

#Create chromosome table
create_chrom = """ CREATE TABLE IF NOT EXISTS
    chromosome(id TEXT(2) PRIMARY KEY,
               start INTEGER,
               end INTEGER)"""
# Add gen_coor to the database
cur.execute(create_chrom)
#fill table with data
#t4 = chrom_csv.to_sql('chromosome',conn,if_exists='replace',index=False)

# Save changes 
conn.commit()

#Create gene table
create_gene = """ CREATE TABLE IF NOT EXISTS
    gene (id TEXT(30) PRIMARY KEY,
        details TEXT)"""

# Add gen_coor to the database
cur.execute(create_gene)
#fill table with data
#t5 = gene_csv.to_sql('gene',conn,if_exists='replace',index=False)

# Save changes 
conn.commit()

#Create gene_alias table
create_galias = """CREATE TABLE IF NOT EXISTS
    gene_alias(gene_id TEXT(30),
               alias_id TEXT(50),
               FOREIGN KEY (gene_id) REFERENCES gene(id),
               FOREIGN KEY (alias_id) REFERENCES alias(id),
               PRIMARY KEY(gene_id,alias_id))"""

# Add gen_coor to the database
cur.execute(create_galias)
#fill table with data
#t6 = gene_al.to_sql('gene_alias',conn,if_exists='replace',index=False)

#Create alias table
create_alias = """ CREATE TABLE IF NOT EXISTS
    alias(id TEXT(50) PRIMARY KEY)"""

# Add gen_coor to the database
cur.execute(create_alias)
#fill table with data
#t7 = alias_csv.to_sql('alias',conn,if_exists='replace',index=False)
conn.commit()



############################ 3. CREATING INDEXES ##############################


# gen_coor index based on position
gen_cor_ind = """ 
                CREATE INDEX IF NOT EXISTS idx_genomic_position
                ON gen_coor(position)
            """
            
cur.execute(gen_cor_ind)


#gene id index based on gene id
gen_id_ind = """ 
                CREATE INDEX IF NOT EXISTS idx_gene_id
                ON gene(id)    
            """
            
cur.execute(gen_id_ind)

# alias id index based on alias id
al_ind = """CREATE INDEX IF NOT EXISTS idx_alias 
            ON alias (id)
           """ 
            
            
cur.execute(al_ind)

# gene_alias compound index based on gene name and gene alias 
gen_al_ind = """CREATE INDEX IF NOT EXISTS idx_gene_alias 
            ON gene_alias(gene_id,alias_id) 
            """
            
cur.execute(gen_al_ind)



# snp_characteristics compound index based on rs_value and pop_id
snpc_rs_pop_ind = """ CREATE INDEX IF NOT EXISTS idx_snpc_rs_pop
                ON snp_characteristics(rs_value,pop_id) """

cur.execute(snpc_rs_pop_ind)
# save changes
conn.commit()


# Shows information about tables and indexes in the database 
ind_query =  """SELECT *
                 FROM SQLite_master
                 """
cur.execute(ind_query)
conn.commit()

masind = cur.fetchall()
print(masind) 
   
############################### 4. Queries ####################################

''' Queries were constructed based on the database schema 
   
The following description applies for query_rs, query_gene and query_pos which correspond to rs, gene, and position queries, respectively.
    The query_alias string has further explanantion within the query comments. 
    
    The SELECT statements selects the columns from to database for display:
        the format of each column is given by the column name alone or as table.column name (example: gene_coor.position)
        The AS statement, creates a view/alias of the column name for display (example: instead of displaying chr_id it displays chromosome)
    The FROM statement selects a table and links it with another table using the INNER JOIN ON syntax using the common values (primary and foreign keys). 
        Example: the snp_characteristics table is joined to the snp table by indicating which columns are related: 
        snpc.rs_value = snp.rs_value. 
    The WHERE statement is where the search term is inserted to look for the corresponding data of data value in the database.
'''

# Position query
posquery = """ SELECT chr_id AS chromosome,
            gen_coor.position AS position, 
            snp.rs_value AS rs_value,
            name AS population,
            sample_count,
            gt_00_count AS "0|0",
            gt_01_count AS "0|1",
            gt_10_count AS "1|0",
            gt_11_count AS "1|1"
            FROM snp
            INNER JOIN snp_characteristics AS snpc ON snpc.rs_value = snp.rs_value
            INNER JOIN population ON snpc.pop_id = population.id
            INNER JOIN gen_coor ON gen_coor.position = snp.position
            WHERE snp.position BETWEEN 21231655 AND 21231656"""

# Gene name query 
gquery = """ SELECT chr_id as chromosome,
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
            WHERE gene.id = 'BAGE2'  """
            
# Gene alias query            
alquery = """ SELECT chr_id as chromosome,
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
            WHERE alias.id = 'HRMT1L1' """            

# rs value query 
rsquery = """SELECT DISTINCT chr_id AS chromosome,
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
            WHERE snp.rs_value = 'rs531532860' """

#custom/general query 
query = ''' 
            

        ''' 
# Executes the query, to change the query change the parameter.
cur.execute(rsquery)

#Prints the results of the query in the console 
for row in cur.fetchall():  
    print(row)
    
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     