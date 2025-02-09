import datetime as dt
from pytz import timezone

# Filter data
app_data['Last Updated'] = pd.to_datetime(app_data['Last Updated'])
filtered_data = app_data[
    (app_data['Rating'] >= 4.0) &
    (app_data['Size'] > 10_000_000) &  # Assuming size is in bytes
    (app_data['Last Updated'].dt.month == 1)
]

top_categories = filtered_data.groupby('Category')['Installs'].sum().nlargest(10).index
filtered_data = filtered_data[filtered_data['Category'].isin(top_categories)]

# Group by category
summary = filtered_data.groupby('Category').agg(
    Avg_Rating=('Rating', 'mean'),
    Total_Reviews=('Reviews', 'sum')
).reset_index()

# Ensure time-based visibility (3 PM to 5 PM IST)
ist = timezone('Asia/Kolkata')
current_time = dt.datetime.now(ist).time()
if dt.time(15, 0) <= current_time <= dt.time(17, 0):
    # Plot grouped bar chart
    fig = go.Figure()
    fig.add_trace(go.Bar(x=summary['Category'], y=summary['Avg_Rating'], name='Average Rating'))
    fig.add_trace(go.Bar(x=summary['Category'], y=summary['Total_Reviews'], name='Total Reviews'))

    fig.update_layout(
        barmode='group',
        title='Average Rating and Total Reviews (Top 10 Categories)',
        xaxis_title='Category',
        yaxis_title='Values'
    )
    fig.show()
else:
    print("This graph is not available at this time.")