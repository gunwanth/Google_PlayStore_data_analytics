from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route("/")
def time_series_chart():
    data = pd.read_csv("Merged_Data (1).csv")

    data['Last Updated'] = pd.to_datetime(data['Last Updated'])
    data = data[data['Installs'] > 10000]
    data = data[data['Content Rating'] == 'Teen']
    data = data[data['App Name'].str.startswith('E')]

    data['Month'] = data['Last Updated'].dt.to_period('M')
    monthly_installs = data.groupby(['Month', 'App Category'])['Installs'].sum().reset_index()
    monthly_installs['Month'] = monthly_installs['Month'].dt.to_timestamp()

    fig = px.line(
        monthly_installs,
        x="Month",
        y="Installs",
        color="App Category",
        title="Time Series: Total Installs Over Time by App Category",
        labels={"Installs": "Total Installs", "Month": "Time"},
        line_shape="spline",
    )
    fig_html = pio.to_html(fig, full_html=False)

    return render_template("chart.html", plot=fig_html)

if __name__ == "__main__":
    app.run(debug=True)
