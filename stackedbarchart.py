import pandas as pd
import plotly.graph_objects as go

# Load data
data = pd.read_csv('Cleaned_User_Reviews.csv')  # Ensure the cleaned reviews dataset is loaded
app_data = pd.read_csv('Cleaned_Play_Store_Data.csv')

# Merge datasets if needed
merged_data = pd.merge(data, app_data, on='App', how='inner')

# Filter data
filtered_data = merged_data[merged_data['Reviews'] > 1000]

# Create rating groups
filtered_data['Rating_Group'] = pd.cut(filtered_data['Rating'], bins=[0, 2, 4, 5], labels=['1-2 stars', '3-4 stars', '4-5 stars'])

# Aggregate sentiment counts by category and rating group
top_categories = filtered_data['Category'].value_counts().nlargest(5).index
filtered_data = filtered_data[filtered_data['Category'].isin(top_categories)]
sentiment_counts = filtered_data.groupby(['Category', 'Rating_Group', 'Sentiment'])['Sentiment'].count().unstack().fillna(0)

# Create the stacked bar chart
fig = go.Figure()
for sentiment in ['Positive', 'Neutral', 'Negative']:
    fig.add_trace(go.Bar(
        x=sentiment_counts.index,
        y=sentiment_counts[sentiment],
        name=sentiment
    ))

fig.update_layout(
    barmode='stack',
    title='Sentiment Distribution by Rating Groups (Top 5 Categories)',
    xaxis_title='Category',
    yaxis_title='Number of Reviews'
)
fig.show()