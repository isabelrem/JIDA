####### Dependencies #######
# Install flask using command line before: pip install flask
# Install flask_wtf using command line: pip install flask-wtf
# Install plotly using command line: pip install plotly

# Import flask
# Import neccessary library required from flask
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file

# Pandas for handling and data/dataframe
import pandas as pd

# sqlite3 for accessing pandas
import sqlite3

# Import forms from form.py file
from forms import SNPForm

# IO for input/output operations
import io

# import functions to calculate genotype frequency and allele frequency function's
from GF_AF_functions import gtfreq, allefreq

# importing the functions for stats
from stats import *

# importing search and query functions
from Validate_Search_Functions import *

# imports json
import json

# importing graph libraries
import plotly
import plotly.express as px

# importing functions to produce multiple plotly graphs
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# importing combinations to allow all pairwise combination calculations of populations for FST
from itertools import combinations

################################################# FLASK #################################################

# Create a flask application object
app = Flask(__name__, template_folder='templates')

# A secret key is needed to create and process forms(inputs)
app.config['SECRET_KEY'] = 'f466c2ef7b41e5c65e9f'


# Link to the main page - base.html.
# Methods GET and POST allow the user to input information from forms.
@app.route("/", methods=['GET', 'POST'])
def basepage():
    return render_template('base.html')


# This will render our SNP browser page.
@app.route('/home', methods=['GET', 'POST'])
def home():
    # resets session except flash warnings. Source: https://stackoverflow.com/questions/27747578/how-do-i-clear-a-flask-session
    [session.pop(key) for key in list(session.keys()) if key != '_flashes']

    # get the form
    form = SNPForm()
    # return the snp browser template
    return render_template('home_template.html',
                           text="JIDA SNP browser",
                           form=form)  # formatted using a separate html template file


# Takes the input from forms.py and home_template and redirects the user

@app.route("/search", methods=['GET', 'POST'])
################################################# SEARCH FUNCTIONS #####################################################

def search():

    try:

        # do the calculation only if method is POST
        if request.method == 'POST':

            # Connects to the database
            conn = sqlite3.connect('SNPB (1).db')

            # creates a cursor, something that lets us interact with the db in sql language
            cur = conn.cursor()

            # Assigns the user input to variables
            gene = request.form['gene'].upper()
            rs = request.form['rs'].lower()
            start = request.form['start']
            end = request.form['end']

            # Creating a global variable
            global Window
            # Taking the input for window size (default = 3)
            try:
                Window = request.form['Window']
                Window = int(Window)
            except:
                Window = 3

            # Runs the inputs through a function that filters if the input is valid
            search = search_term(gene, rs, start, end)

            # If no population selected, user is redirected to the home template and a warning sign is displayed
            if ('GBR' not in request.form) & ('COL' not in request.form) & ('PUN' not in request.form) & ('FIN' not in request.form) & ('TEL' not in request.form):
                flash('Please select at least one population', "Error")
                return redirect(url_for('home'))

            # If the input is invalid, the user is redirected to the home template and a warning sign is displayed
            if (search[0] == None) and (search[1] == None):
                flash(f'{search[2]}', "Error")
                return redirect(url_for('home'))

            # If the input is value, the inputs are assigned to the an appropriate query(There are 4 separate queries for gene, gene alias, rs and positions)
            else:
                query = query_select(search[0], search[1], gene, rs, start, end)

                # Executes the query and extracts the requested data
                sql_query = pd.read_sql_query(query, conn)

                # Checking if the query returned any results and displays a flash message accordingly
                # if there were not results, the user is redirected to the home page and an error message is displayed
                if sql_query.empty == True:
                    flash('We could not find information for your query. Please note the genomic positions covered by this web application for your selected chromosome span from 9411239 - 48119740.', "Error")
                    return redirect(url_for('home'))

                # if there were valid results, the user is redirected to the search page, a df is created with the data
                # and a flash message is displayed on the search page.
                else:
                    flash('Query successful!', "Success")

                # Creates a pandas dataframe form the sql query
                df = pd.DataFrame(sql_query, columns=['chromosome', 'position', 'rs_value', 'population',
                                                      'reference',
                                                      'alternate',
                                                      'sample_count', '0|0', '0|1', '1|0', '1|1'])


                # Checks the size of the sliding window is appropriate for the difference between genomic positions (start,end)
                w_check = window_check(Window, df.iloc[1][1], df.iloc[-1][1])


                # if the sliding window size is bigger than the distance between positions
                # AND the input wasn't an rs value
                # AND the number of bases between the user's chosen positions isn't less than 3
                # returns an error message.
                if (w_check != None) and (rs == ""):
                    flash(f'{w_check}', "Error")
                    return redirect(url_for('home'))


            # Checking/ coverting position values to integer
            df["position"] = df["position"].astype(int)

            # creating empty columns for calculations
            df['af-0'] = ""
            df['af-1'] = ""
            df['gt-00'] = ""
            df['gt-01'] = ""
            df['gt-10'] = ""
            df['gt-11'] = ""

            # iter over each row and calculate af and gf values
            for i, row in df.iterrows():
                gt = gtfreq(row['0|0'], row['0|1'], row['1|0'], row['1|1'])
                af = allefreq(row['0|0'], row['0|1'], row['1|0'], row['1|1'])

                # converting the values from dict into a list
                ls = list(gt.values())
                ls2 = list(af.values())

                # storing the values in specified location
                df['gt-00'].iloc[i] = ls[0]
                df['gt-01'].iloc[i] = ls[1]
                df['gt-10'].iloc[i] = ls[2]
                df['gt-11'].iloc[i] = ls[3]

                df['af-0'].iloc[i] = ls2[0]
                df['af-1'].iloc[i] = ls2[1]

            # getting the user input data from html file home_template for population checkboxex
            population_list = []
            population_names = []
            if 'GBR' in request.form:
                population_list.append('British')
                population_names.append('British')
            if 'COL' in request.form:
                population_list.append('Colombian')
                population_names.append('Colombian')
            if 'FIN' in request.form:
                population_list.append('Finnish')
                population_names.append('Finnish')
            if 'PUN' in request.form:
                population_list.append('Punjabi')
                population_names.append('Punjabi')
            if 'TEL' in request.form:
                population_list.append('Telugu')
                population_names.append('Telugu')

            # getting the statistics in a list acording to user's input
            # i.e if user clicks the check box on home_template
            stats_list = []
            if 'nud' in request.form:
                stats_list.append('nud')
            if 'hapd' in request.form:
                stats_list.append('hapd')
            if 'td' in request.form:
                stats_list.append('td')
            if 'fst' in request.form:
                stats_list.append('fst')

            # dropping the columns and storing in a new variable that can be later used to while rendering output
            df_temp = df
            df_temp = df_temp.drop(['sample_count', '0|0', '0|1', '1|0', '1|1'], axis=1)

            # selecting only specific rows acording to input
            ind = pd.DataFrame([], columns=df_temp.columns.values)

            # to show the populations one by one
            for i, j in enumerate(population_list):
                d = df_temp[df_temp["population"] == j]

                # concating the data into ind from d
                ind = pd.concat([ind, d], axis=0)

            # Show the summary statistics only when the user enters genome and gene name
            if (request.form['start'] != "" and request.form['end'] != "") or (request.form['gene'] != ""):

                # p_names will contain -> all the data for selected population
                p_names = {}

                # zipping 2 lists together
                for pl, pn in zip(population_list, population_names):
                    p_names[pn] = df[df['population'] == pl]

                # Booleans- later made true acording to the user input
                check_nud = False
                check_hapd = False
                check_td = False
                check_fst = False

                ######################################### STATISTICAL FUNCTIONS  ##########################################

                # key -> E.g. : df_british (name)
                # val -> all the rows for british pop only

                # at this point the df has one row per population
                number_of_pops = len(population_list)
                number_of_variants = len(df) / number_of_pops

                if 'nud' in request.form:
                    if number_of_variants > 3:
                        nud = {}
                        nud_w = {}
                        for key, val in p_names.items():
                            # calculating the ND values from the start and end positions for each population selected by the user
                            nud[key] = SQLtoNucDiv(val, val.iloc[0]["position"], val.iloc[-1]["position"])
                            # calculating the ND sliding window values for each population selected by the user
                            nud_w[key] = nuc_div_sliding(val, Window)
                        check_nud = True
                    elif number_of_variants > 1:
                        nud = {}
                        for key, val in p_names.items():
                            nud[key] = SQLtoNucDiv(val, val.iloc[0]["position"], val.iloc[-1]["position"])
                        check_nud = True
                    else:
                        check_nud = False


                if 'hapd' in request.form:
                    if number_of_variants >= 3:
                        hapd = {}
                        hapd_w = {}
                        for key, val in p_names.items():
                            # calculating the HD values for each population selected by the user
                            hapd[key] = SQLtoHapDiv(val)
                            # calculating the HD sliding window values for each population selected by the user
                            hapd_w[key] = SQLtoHapDiv_window(val, Window)
                        check_hapd = True
                    elif number_of_variants > 1:
                        hapd = {}
                        for key, val in p_names.items():
                            hapd[key] = SQLtoHapDiv(val)
                        check_hapd = True
                    else:
                        check_hapd = False

                if 'td' in request.form:
                    if number_of_variants >= 3:
                        td = {}
                        td_w = {}
                        for key, val in p_names.items():
                            # calculating the TD value for each population selected by the user
                            td[key] = SQLtoTD(val)
                            # calculating the TD sliding window for each population selected by the user
                            td_w[key] = SQLtoTD_window(val, Window)
                        check_td = True
                    elif number_of_variants > 1:
                        td = {}
                        for key, val in p_names.items():
                            td[key] = SQLtoTD(val)
                        check_td = True
                    else:
                        check_td = False

                if 'fst' in request.form:
                    if number_of_variants > 1:
                        # making a list of tuples with every combination possible for the populations selected by the user
                        combos = list(combinations(population_list, 2))
                        fst = {}
                        # for each tuple the two populations were extracted and used to produce the key
                        for element in combos:
                            pop1 = element[0]
                            pop2 = element[1]
                            key = str("FST - " + pop1 + " - " + pop2)
                            # the FST value was calculated for each combination of population and stored in the dictionary
                            fst[key] = SQLtoFST(df[df["population"] == pop1], df[df["population"] == pop2])
                        check_fst = True

                        if number_of_variants >= 3:
                            fst_w = {}
                            # extracting out the two populations in the tuple and making them the key for the dictionary
                            for element in combos:
                                pop1 = element[0]
                                pop2 = element[1]
                                key = str("FST - " + pop1 + " - " + pop2)
                                # calculating the FST sliding windows for the pairs of populations and storing the value in the dictinary
                                fst_w[key] = SQLtoFST_window(df[df["population"] == pop1], df[df["population"] == pop2], Window)
                        check_fst = True
                    else:
                        check_fst = False

                # final_stat contains all the values calculated  by stat functions
                final_stat = {}
                if check_nud:
                    final_stat['Nucleotide diversity'] = nud
                    if number_of_variants >= 3:
                        final_stat['Nucleotide Diversity Window'] = nud_w
                if check_hapd:
                    final_stat['Haplotype Diversity'] = hapd
                    if number_of_variants >= 3:
                        final_stat['Haplotype Diversity Window'] = hapd_w
                if check_td:
                    final_stat['Tajimas D'] = td
                    if number_of_variants >= 3:
                        final_stat['Tajimas D Window'] = td_w
                if check_fst:
                    final_stat['FST'] = fst
                    if number_of_variants >= 3:
                        final_stat['FST Window'] = fst_w

                # creating global variables
                # global variables can be accessed throughout the program body by all functions
                global final_stat_global
                final_stat_global = final_stat
                global start_df_global
                start_df_global = df.iloc[0]["position"]
                global end_df_global
                end_df_global = df.iloc[-1]["position"]
            else:
                final_stat_global = {}
                start_df = pd.DataFrame()
                end_df = pd.DataFrame()

            # boolean to check if there is more than one rs value
            rs_unique = False

            # checks if the number of unique rs values found is smaller than 2, if so, rs_unique becomes true.
            if len(df['rs_value'].unique()) < 2:
                rs_unique = True

            # if data is empty than return simple empty arrray (for safety)
            if df.empty:
                return render_template('output.html', d=ind, zip=zip)

            # final return.
            return render_template('output.html', column_names=["Chromosome", "Genomic Position", "rs value", "Population",
                                                                "Reference Allele (0)", "Alternate Allele (1)",
                                                                "Reference Allele Frequency", "Alternate Allele Frequency",
                                                                "0|0 Genotype Frequency", "0|1 Genotype Frequency",
                                                                "1|0 Genotype Frequency", "1|1 Genotype Frequency"],
                                   d=list(ind.values.tolist()),
                                   final_stat=final_stat_global, col_name=population_names, zip=zip,
                                   rs_unique=rs_unique,
                                   t_search=search[0], t2_search=search[1])

    except:
        flash('Something went wrong. Please double check your input. If this error persists, please contact the developers using our contact information on the website', "Error")
        return redirect(url_for('home'))


############################################### APP ROUTE FOR GRAPHS ###################################################

# assigning the populations to a specific colour
# list of all the populations
all_pop = ["British", "Colombian", "Finnish", "Punjabi", "Telugu"]

# list of the colours - muted blue, safety orange, cooked asparagus green, brick red, muted purple
colours = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# making a dictionary of the populations and colours
pop_colour = dict(zip(all_pop, colours))


############################################### NUCLEOTIDE DIVERSITY ###################################################

@app.route("/Nucleotide diversity")
def Nucleotide_graph():
    ''' This function takes the Nucleotide diversity statistic calculated for the user's selected genomic range,
    and returns a scatter plot of the nucleotide diversity values versus the user's selected populations.
    Points on the graph when hovered over will display the exact values.
    '''

    # retrieving the nucleotide diversity calculations and the population names then producing a pandas dataframe
    name = []
    val = []
    for i, j in final_stat_global["Nucleotide diversity"].items():
        name.append(i)
        val.append(j)
    df = pd.DataFrame()
    df["name"] = name
    df["val"] = val

    # producing a scatterplot of ND vs population from the dictionary
    fig = px.scatter(df, x="name", y="val", labels=dict(name="Population", val="Nucleotide Diversity"), width=1500,
                     height=600)

    # returning the graph with a header and a description
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Nucleotide Diversity Graph"
    description = """Hover over the points to see the specific values"""
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route("/Nucleotide Diversity Window")
def Nucleotide_w_graph():
    ''' This function takes the windowed nucleotide diversity statistics calculated for the user's selected genomic range,
    and returns a plot of the windowed nucleotide diversity values versus the user's selected genomic positions.
    Points on the graph when hovered over will display the exact values.
    Populations can be selected or deselected using an interactive legend.
    '''

    # making empty lists to store the ND window values and the population name
    ND_window_list = []
    name = []

    # from the stats dictionary extract the population and the ND window values for ND and append these to the lists
    for population, ND_window_values in final_stat_global["Nucleotide Diversity Window"].items():
        name.append(population)
        ND_window_list.append(ND_window_values)

    # creates the list of colours for the populations that the user has selected
    final_colours = []
    for n in range(len(name)):
        # taking the population and extracting the colour assigned from the dictionary
        if name[n] in pop_colour.keys():
            final_colours.append(pop_colour[name[n]])

    # extracting the start and end positions to produce the x axis for genomic position
    start_pos = start_df_global
    end_pos = end_df_global
    # starting the x axis with the start genomic position
    x_axis = [start_pos]
    n = 0
    # the x axis values are produced with the addition of the window size and the result is capped at the end genomic position
    while x_axis[n] + Window <= end_pos:
        x_axis.append(x_axis[n] + Window)
        n += 1

    # producing the overall graph with all the population results
    fig = make_subplots(rows=1, cols=1)

    # start a counter for to produce the graph for the first population
    n = 0
    for ND_values in ND_window_list:
        # producing a scatter plot with the specific population colour and recording the name in the label legend
        fig.add_trace(go.Scatter(x=x_axis, y=ND_values, name=name[n], marker=dict(color=final_colours[n])), row=1,
                      col=1)
        # stating the height and width of the graph and the legend title
        fig.update_layout(height=600, width=1500, legend_title="Population")
        # updating the x and y axis labels
        fig.update_xaxes(title_text="Genomic Position", row=1, col=1)
        fig.update_yaxes(title_text="Nucleotide Diversity", row=1, col=1)
        # adding to the counter to continue for the next population the user has selected
        n += 1
        
        # allows the x axis to be shown in whole numbers rather than the abbreviation of million as "M"
        fig.update_layout(xaxis=dict(tickformat = ".0f"))

    # returning the figure withe header and the description
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Nucleotide Diversity Sliding Window Graph"
    description = """Click on the specific populations in the population legend to view/hide the results """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


################################################# HAPLOTYPE DIVERSITY #################################################

@app.route("/Haplotype Diversity")
def Haplotype_graph():
    ''' This function takes the haplotype diversity statistic calculated for the user's selected genomic range,
    and returns a scatter plot of the haplotype diversity values versus the user's selected populations.
    Points on the graph when hovered over will display the exact values. '''

    # retreiving the population and the HD value to produce a pandas dataframe
    name = []
    val = []
    for i, j in final_stat_global["Haplotype Diversity"].items():
        name.append(i)
        val.append(j)
    df = pd.DataFrame()
    df["Population"] = name
    df["Value"] = val

    # the pandas dataframe is used to produce the scatter plot
    fig = px.scatter(df, x="Population", y="Value", labels=dict(name="Population", val="Haplotype Diversity"),
                     width=1500, height=600)

    # the scatter plot is returned with the header and description
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Haplotype Diversity graph"
    description = """Hover over the points to see the specific values"""
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route("/Haplotype Diversity Window")
def Haplotype_w_graph():
    ''' This function takes the windowed haplotype diversity statistics calculated for the user's selected genomic range,
        and returns a plot of the windowed haplotype diversity values versus the user's selected genomic positions.
        Points on the graph when hovered over will display the exact values.
        Populations can be selected or deselected using an interactive legend.
        '''
    # making empty lists to store the ND window values and the population name
    HD_window_list = []
    name = []

    # from the stats dictionary extract the population and the ND window values for ND and append these to the lists
    for population, HD_window_values in final_stat_global["Haplotype Diversity Window"].items():
        name.append(population)
        HD_window_list.append(HD_window_values)

    # creates the list of colours for the populations that the user has selected
    final_colours = []
    for n in range(len(name)):
        # taking the population and extracting the colour assigned from the dictionary
        if name[n] in pop_colour.keys():
            final_colours.append(pop_colour[name[n]])

    # extracting the start and end positions
    start_pos = start_df_global
    end_pos = end_df_global
    # the start of the x axis values is the start position
    x_axis = [start_pos]
    n = 0
    # adding to the start position the window number and capping it before the end position is reached
    while x_axis[n] + Window <= end_pos:
        # the position is appended to a list with all the x axis values
        x_axis.append(x_axis[n] + Window)
        n += 1

    # making a single plot with all the populations results
    fig = make_subplots(rows=1, cols=1)

    # for each population the HD values are plotted from the HD window list
    # start a counter for to produce the graph for the first population
    n = 0
    for HD_values in HD_window_list:
        # the plots are produced with specific colours for each population
        fig.add_trace(go.Scatter(x=x_axis, y=HD_values, name=name[n], marker=dict(color=final_colours[n])), row=1,
                      col=1)
        # the height, width and legend title is updated
        fig.update_layout(height=600, width=1500, legend_title="Population")
        # the x and y axis labels are updated
        fig.update_xaxes(title_text="Genomic Position", row=1, col=1)
        fig.update_yaxes(title_text="Haplotype Diversity", row=1, col=1)
        # this occurs for each population thus the counter increases
        n += 1
        
        # allows the x axis to be shown in whole numbers rather than the abbreviation of million as "M"
        fig.update_layout(xaxis=dict(tickformat = ".0f"))


    # the graph is returned along with a header and description
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Haplotype Diversity Sliding Window Graph"
    description = """ Click on the specific populations in the population legend to view/hide the results """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


###################################################### TAJIMAS D ######################################################

@app.route("/Tajimas D")
def Tajimas_graph():
    ''' This function takes the Tajima's D statistic calculated for the user's selected genomic range,
    and returns a scatter plot of the Tajima's D values versus the user's selected populations.
    Points on the graph when hovered over will display the exact values. '''

    # the TD values and the populations have been extracted from the dictionary and made into a pandas database
    name = []
    val = []
    for i, j in final_stat_global["Tajimas D"].items():
        name.append(i)
        val.append(j)
    df = pd.DataFrame()
    df["Population"] = name
    df["Value"] = val
    # the pandas database was utilised to produce the scatter plot for TD values vs population
    fig = px.scatter(df, x="Population", y="Value", labels=dict(name="Population", val="Tajima's D"), width=1500,
                     height=600)

    # the graph was returned along side the header and the description
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Tajima's D graph"
    description = """Hover over the points to see the specific values"""
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route("/Tajimas D Window")
def Tajimas_w_graph():
    ''' This function takes the windowed Tajima's D statistics calculated for the user's selected genomic range,
    and returns a plot of the windowed Tajima's D values versus the user's selected genomic positions.
    Points on the graph when hovered over will display the exact values.
    Populations can be selected or deselected using an interactive legend. '''

    # making empty lists to store the ND window values and the population name
    TD_window_list = []
    name = []

    # from the stats dictionary extract the population and the ND window values for ND and append these to the lists
    for population, TD_window_values in final_stat_global["Tajimas D Window"].items():
        name.append(population)
        TD_window_list.append(TD_window_values)

    # creates the list of colours for the populations that the user has selected
    final_colours = []
    for n in range(len(name)):
        # taking the population and extracting the colour assigned from the dictionary
        if name[n] in pop_colour.keys():
            final_colours.append(pop_colour[name[n]])

    # extracting the start and end positions and starting the x axis values list with the start position
    start_pos = start_df_global
    end_pos = end_df_global
    # the start position is the first value in the x axis list
    x_axis = [start_pos]
    # to the start position the window number is added and this is capped before the value goes above the end position
    n = 0
    while x_axis[n] + Window <= end_pos:
        # the values are appended to the x axis list
        x_axis.append(x_axis[n] + Window)
        n += 1

    # making a graph for all the population TD results
    fig = make_subplots(rows=1, cols=1)

    # getting the TD values from the list for each population
    # start a counter for to produce the graph for the first population
    n = 0
    for TD_values in TD_window_list:
        # the plot is produced for the specific population with a specific colour
        fig.add_trace(go.Scatter(x=x_axis, y=TD_values, name=name[n], marker=dict(color=final_colours[n])), row=1,
                      col=1)
        # the height, wdith and legend of the grpah is updated
        fig.update_layout(height=600, width=1500, legend_title="Population")
        # the x and y axis labels are updated
        fig.update_xaxes(title_text="Genomic Position", row=1, col=1)
        fig.update_yaxes(title_text="Tajima's D", row=1, col=1)
        # this plot is for all populations so the counter increases to produce results for the next selected population
        n += 1
        
        # allows the x axis to be shown in whole numbers rather than the abbreviation of million as "M"
        fig.update_layout(xaxis=dict(tickformat = ".0f"))


    # returning the graph with the header and the description
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Tajima's D Sliding Window Graph"
    description = """Click on the specific populations in the population legend to view/hide the results """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


###################################################### FST #############################################################

@app.route("/FST")
def FST_graph():
    ''' This function takes the FST statistic calculated for the user's selected genomic range,
    and returns a scatter plot of the FST values versus pairwise comparisons of the user's selected populations.
    Points on the graph when hovered over will display the exact values. '''

    # extracting the FST values and populations and appending the values to a list
    name = []
    val = []
    for i, j in final_stat_global["FST"].items():
        name.append(i)
        val.append(j)
    # from the lists a pandas dataframe is produced containing the population and the FST value
    df = pd.DataFrame()
    df["Population"] = name
    df["Value"] = val
    # A scatter plot is produced for the FST value against the population
    fig = px.scatter(df, x="Population", y="Value", width=1500, height=600)

    # the graph is returned with a header and description
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "FST graph"
    description = """Hover over the points to see the specific values"""
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route("/FST Window")
def FST_w_graph():
    ''' This function takes the FST statistics calculated for the user's selected genomic range,
    and returns a plot of the windowed FST values versus the user's selected genomic positions.
    Points on the graph when hovered over will display the exact values.
    Pairwise population comparisons can be selected or deselected using an interactive legend. '''

    # making empty lists to store the ND window values and the population name
    FST_window_list = []
    name = []

    # from the stats dictionary extract the population and the ND window values for ND and append these to the lists
    for population, FST_window_values in final_stat_global["FST Window"].items():
        name.append(population)
        FST_window_list.append(FST_window_values)

        # the start and end positions are called
        start_pos = start_df_global
        end_pos = end_df_global
        # the start position is the starting point for the x axis values
        x_axis = [start_pos]

        # to the start position the window size is added and the value is appended to the list
        # the x axis values are capped before exceeding the final position
        n = 0
        while x_axis[n] + Window <= end_pos:
            x_axis.append(x_axis[n] + Window)
            # addition to the counter to allow further additon of windows
            n += 1

    # producing a single plot with all the population results
    fig = make_subplots(rows=1, cols=1)

    # the FST values in the list are extracted for each population and plotted
    n = 0
    for FST_values in FST_window_list:
        # the results for the first selected population are plotted
        fig.add_trace(go.Scatter(x=x_axis, y=FST_values, name=name[n]), row=1, col=1)
        # the the height, width and legend title are updated
        fig.update_layout(height=600, width=1500, legend_title="Population")
        # the x and y axis labels are updated
        fig.update_xaxes(title_text="Genomic Position", row=1, col=1)
        fig.update_yaxes(title_text="FST", row=1, col=1)
        # the counter increases to produce the plot for the next selected population
        n += 1
        
        # allows the x axis to be shown in whole numbers rather than the abbreviation of million as "M"
        fig.update_layout(xaxis=dict(tickformat = ".0f"))


    # the graph is returnd alongside the header and description
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "FST Sliding Window Graph"
    description = """Click on the specific populations in the population legend to view/hide the results """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


################################################## DOWNLOAD BUTTON #####################################################


# Download button
@app.route("/Download", methods=['GET', 'POST'])
# this function will download the summary statistics output as a text file
def export_txt():
    data = {}
    for i, j in final_stat_global.items():
        name = []
        val = []
        for k, l in j.items():
            name.append(k)
            val.append(l)
        df = pd.DataFrame()
        df["name"] = name
        df["val"] = val
        data[i] = df

    # convert the dataframe into text file
    # buffer is used to writing a file
    buffer = io.BytesIO()

    for i, df in data.items():
        buffer.write(bytes("\n" + i + "\n", 'utf-8'))
        # converting into csv
        df.to_csv(buffer, index=False)

    buffer.seek(0)
    return send_file(buffer,
                     attachment_filename="output.csv",
                     mimetype='text/csv')


################################################# Start web server #####################################

if __name__ == '__main__':
    app.run(debug=True)
