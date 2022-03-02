# JIDA

JIDA is a web application that retrieves SNP information for a genomic region of interest in Homo sapiens and calculates specific summary statistics of interest for specified populations. Users are able to enter either the RS value, start and end genomic positions or the gene name and its aliases and select information for particular statistics and populations. The statistical outputs the website provides are Nucleotide diversity, Haplotype diversity, Tajima's D and FST. Information for the British, Finnish, Colombian, Punjabi and Telugu population is present in the database and is utilised by the web application. 

## OS
Note the application is supported on Windows and Linux machines.

## Installation

Using python versions 3.9.2 and 3.8.10.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

Please download the following packages in your terminal...

```bash
pip install pandas (in case this was not installed along with python)
pip install Flask
pip install flask-wtf
pip install biopython
pip install scikit-allel[full]
pip install plotly
```

## How to run via command line
Clone the git repository or onedrive folder to your local machine. Within your terminal, navigate to inside the repository, such that running ls produces this output. PLEASE NOTE: if cloning the git repository, you will also have to separately download the SNP database 'SNPB (1).db' from the Onedrive.

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

## How to run via pycharm

First, open a new project. This is an important step as it allowed a virtual environemnt folder to be generated.

Second, clone the git repository or onedrive folder to your local machine. PLEASE NOTE: if cloning the git repository, you will also have to separately download the SNP database 'SNPB (1).db' from the Onedrive. Copy the downloaded contents into your newly created Pycharm project file.

Thirdly, download the prerequisite python packages/modules. This can be done from the terminal within Pycharm, or a separate application such as Windows Powershell.

```bash
pip install pandas (in case this was not installed along with python)
pip install Flask
pip install flask-wtf
pip install biopython
pip install scikit-allel[full]
pip install plotly
```


Finally, within Pycharm open APP.py, and run the script. 


## Credits and Contact
Janeesh Kaur Bansal : j.k.bansal@se21.qmul.ac.uk

Isabel Rachel Thompson : i.r.thompson@se21.qmul.ac.uk

Diego Pava Mejia : d.a.pava@se21.qmul.ac.uk

Aravind Pattisapu : v.pattisapu@se21.qmul.ac.uk
