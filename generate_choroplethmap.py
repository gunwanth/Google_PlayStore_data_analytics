import pandas as pd
import plotly.express as px
from datetime import datetime

try:
    # Load dataset
    app_data = pd.read_csv("Merged_Data_with_Country.csv")  # Replace with your dataset path

    # Filter top 5 categories by installs
    top_categories = app_data.groupby('Category')['Installs'].sum().nlargest(5).index
    filtered_data = app_data[
        (app_data['Category'].isin(top_categories)) & 
        (app_data['Installs'] > 1_000_000) &
        (~app_data['Category'].str.startswith(('A', 'C', 'G', 'S')))
    ]

    # Time-based restriction (6 PM to 8 PM IST)
    current_time = datetime.now().time()
    allowed_start = datetime.strptime("18:00", "%H:%M").time()
    allowed_end = datetime.strptime("20:00", "%H:%M").time()

    if allowed_start <= current_time <= allowed_end:
        # Create choropleth map showing installs by country
        fig = px.choropleth(
            app_data,
            locations="Country",  # Ensure the dataset has a 'Country' column
            locationmode="country names",
            color="Installs",
            hover_name="Category",
            title="Global Installs by Country",
            color_continuous_scale=px.colors.sequential.Plasma
        )

        # Save the map to an HTML file
        fig.write_html("choropleth_map.html")
        print("Choropleth map saved as 'choropleth_map.html'. Open it in a browser to view the map.")
    else:
        print("The Choropleth map is only available between 6 PM and 8 PM IST.")
except FileNotFoundError:
    print("Dataset file not found. Please check the path to your dataset.")
except Exception as e:
    print(f"An error occurred: {e}")
