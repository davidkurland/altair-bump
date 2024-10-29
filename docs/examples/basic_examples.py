import altair as alt
import pandas as pd
from altair_bump import bump_chart, prepare_rank_data

# Create sample data
data = pd.DataFrame({
    'year': [2018, 2019, 2020, 2021] * 5,
    'company': ['Apple', 'Apple', 'Apple', 'Apple',
                'Google', 'Google', 'Google', 'Google',
                'Microsoft', 'Microsoft', 'Microsoft', 'Microsoft',
                'Amazon', 'Amazon', 'Amazon', 'Amazon',
                'Facebook', 'Facebook', 'Facebook', 'Facebook'],
    'revenue': [265.6, 260.2, 274.5, 365.8,
                136.2, 161.9, 182.5, 257.6,
                110.4, 125.8, 143.0, 168.1,
                232.9, 280.5, 386.1, 469.8,
                55.8, 70.7, 85.9, 117.9]
})

# Prepare data with rankings
ranked_data = prepare_rank_data(data, 'company', 'revenue', 'year')

# Create bump chart
chart = bump_chart(
    data=ranked_data,
    x='year',
    y='rank',
    group='company',
    smooth=8,
    interpolate='sigmoid',
    title='Top Tech Companies Revenue Rankings'
)

# Save the chart
chart.save('bump_chart_example.html') 

# show the chart
chart