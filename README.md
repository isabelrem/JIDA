# JIDA

JIDA is a web application that retrieves SNP information for a genomic region of interest in Homo sapiens and calculates specific summary statistics of interest for specified populations. Users are able to enter either the RS value, start and end genomic positions or the gene name and its aliases and select information for particular statistics and populations. The statistical outputs the website provides are Nucleotide diversity, Haplotype diversity, Tajima's D and FST. Information for the British, Finnish, Colombian, Punjabi and Telugu population is present in the database and is utilised by the web application. 

## Important links
Github:

This repository contains most of the Application files, the documentation files and some of the Appendix files (not all owing to size constraints).
https://github.com/isabelrem/JIDA
Google Drive:

This link gives you access to SNPB (1).db only. It is neccessary for those who download the application files from github, and wish to run the application locally. 

https://drive.google.com/file/d/1gwdoDF3-y1kKkkFve3NVvJC9ZvSpXwYy/view?usp=sharing

OneDrive:

This folder is only accessible to those with QMUL email addresses, owing to being stored on the QMUL Onedrive. This folder contains (1) an Application subdirectory, which contains everything you need to run the application locally (2) a Documentation subdirectory, which contains all documentation and (3) an Appendix subdirectory which contains scripts, CSVs and VCF files used to create the SQL database.

https://qmulprod-my.sharepoint.com/:f:/g/personal/bt211032_qmul_ac_uk/EpmZJ8ghymBEuY17LKb-fLcBkITJzF_EQsm9QVqqZLWMDQ?e=1fZi79


## OS
Note the application is supported on Windows and Linux machines.

## Installation

Using python versions 3.9.2 and 3.8.10.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

Please download the following packages in your terminal...

```bash
pip install Flask
pip install flask-wtf
pip install biopython
pip install scikit-allel[full]
pip install plotly
pip install pandas
pip install numpy
```

## How to run via command line
Clone the git repository or onedrive folder to your local machine. Within your terminal, navigate to inside the repository, such that running ls (linux) or dir (windows) produces this output. PLEASE NOTE: if cloning the git repository, you will also have to separately download the SNP database 'SNPB (1).db' from the Onedrive.

```bash
PS C:\Users\isabe\PycharmProjects\JIDA> ls


    Directory: C:\Users\isabe\PycharmProjects\JIDA


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       01/03/2022     13:35                static
d-----       01/03/2022     14:04                templates
-a----       02/03/2022     12:25          38388 APP.py
-a----       28/02/2022     18:14           1610 forms.py
-a----       28/02/2022     14:01           2665 GF_AF_functions.py
-a----       01/03/2022     13:35            198 Installation Requirements.txt
-a----       01/03/2022     13:49      389398528 SNPB (1).db
-a----       28/02/2022     19:20          23184 stats.py
-a----       01/03/2022     18:11          12701 Validate_Search_Functions.py
```

Once all prerequisites have been confirmed present, you can run the web application locally using the following terminal command.

```bash
python APP.py
```
The terminal will display a local http address, please copy and paste this into your browser of preference. 

## How to run via pycharm

First, open a new project. This is an important step as it allowed a virtual environemnt folder to be generated.

Second, clone the git repository or onedrive folder to your local machine. PLEASE NOTE: if cloning the git repository, you will also have to separately download the SNP database 'SNPB (1).db' from the Onedrive. Copy the downloaded contents into your newly created Pycharm project file.

Thirdly, download the prerequisite python packages/modules. This can be done from the terminal within Pycharm, or a separate application such as Windows Powershell.

```bash
pip install Flask
pip install flask-wtf
pip install biopython
pip install scikit-allel[full]
pip install plotly
pip install pandas
pip install numpy
```


Finally, within Pycharm open APP.py, and run the script.
The terminal will display a local http address, clicking it will open a browser with the app.


## Credits and Contact
Janeesh Kaur Bansal : j.k.bansal@se21.qmul.ac.uk

Isabel Rachel Thompson : i.r.thompson@se21.qmul.ac.uk

Diego Pava Mejia : d.a.pava@se21.qmul.ac.uk

Aravind Pattisapu : v.pattisapu@se21.qmul.ac.uk
