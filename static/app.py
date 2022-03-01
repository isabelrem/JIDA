# in the console...
# pip install scikit-allel
# pip install flask
# pip install pandas
# pip install plotly

from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart1')
def chart1():
    # importing the function for sliding windows
    from TD_sliding_window import TD_windows

    # producing the sliding window array
    TD_windows_array = TD_windows("Punjabi_SNV_only.vcf", 9411239, 9414448, 50)

    # converting the sliding window into a list
    TD_windows_list = TD_windows_array.tolist()

    # making a list of the window sizes
    x_values = list(range(1, len(TD_windows_array)+1))

    # producing a dictionary of the window number and the FST value
    my_dict = {"Window":x_values, "TD":TD_windows_list}

    # converting the dictionary into a pandas dataframe
    df = pd.DataFrame(my_dict)

    fig = px.scatter(df, x="Window", y="TD")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Tajima's D"
    description = """
    yay we just calculated tajimas d love stats hehehehehe
    """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)



 #### edit below to produce other statistical calculations
  
@app.route('/chart2')
def chart2():
    df = pd.DataFrame({
        "Vegetables": ["Lettuce", "Cauliflower", "Carrots", "Lettuce", "Cauliflower", "Carrots"],
        "Amount": [10, 15, 8, 5, 14, 25],
        "City": ["London", "London", "London", "Madrid", "Madrid", "Madrid"]
    })

    fig = px.bar(df, x="Vegetables", y="Amount", color="City", barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Vegetables in Europe"
    description = """
    The rumor that vegetarians are having a hard time in London and Madrid can probably not be
    explained by this chart.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)