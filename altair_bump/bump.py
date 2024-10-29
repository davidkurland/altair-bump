import altair as alt
import pandas as pd
import numpy as np
from .sigmoid import sigmoid_curve

def bump_chart(
    data, 
    x, 
    y, 
    group=None, 
    color=None, 
    smooth=8, 
    line_size=3,
    point_size=100,
    interpolate='linear',
    **kwargs
):
    """Create a bump chart using Altair.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame containing the data
    x : str
        Column name for x-axis (typically time/sequence)
    y : str 
        Column name for y-axis (typically rank)
    group : str, optional
        Column name for grouping data (typically category/entity name)
    color : str, optional
        Column name for color encoding (defaults to group if not specified)
    smooth : int, default=8
        Smoothing parameter for curves. Higher means less smoothing.
    line_size : int, default=3
        Width of the connecting lines
    point_size : int, default=100
        Size of the points
    interpolate : str, default='linear'
        Type of interpolation ('linear' or 'sigmoid')
    **kwargs
        Additional arguments passed to Altair chart
        
    Returns
    -------
    alt.Chart
        An Altair chart object
    """
    if group is None and color is None:
        raise ValueError("Either 'group' or 'color' must be specified")
    
    if color is None:
        color = group
        
    # Create base chart
    base = alt.Chart(data)
    
    # Get the scale for y-axis (reversed, so rank 1 is at top)
    y_scale = alt.Scale(domain=[data[y].max(), data[y].min()])
    
    if interpolate == 'sigmoid':
        # Generate sigmoid curves for each group
        curves_data = []
        for name, group_data in data.groupby(group):
            group_data = group_data.sort_values(x)
            for i in range(len(group_data) - 1):
                x1, y1 = group_data.iloc[i][[x, y]]
                x2, y2 = group_data.iloc[i + 1][[x, y]]
                curve = sigmoid_curve(x1, y1, x2, y2, smoothness=smooth)
                curve[group] = name
                curves_data.append(curve)
        
        curves_df = pd.concat(curves_data, ignore_index=True)
        
        # Create smooth lines with reversed y-axis
        line = alt.Chart(curves_df).mark_line(
            size=line_size
        ).encode(
            x='x:Q',
            y=alt.Y('y:Q', scale=y_scale),
            color=alt.Color(f'{group}:N', legend=alt.Legend(title=group))
        )
    else:
        # Create straight lines with reversed y-axis
        line = base.mark_line(
            size=line_size
        ).encode(
            x=x,
            y=alt.Y(y, scale=y_scale),
            color=alt.Color(f'{color}:N', legend=alt.Legend(title=color))
        )
    
    # Add points with reversed y-axis
    points = base.mark_circle(
        size=point_size,
        filled=True
    ).encode(
        x=x,
        y=alt.Y(y, scale=y_scale),
        color=alt.Color(f'{color}:N', legend=alt.Legend(title=color))
    )
    
    # Combine and configure
    chart = (line + points).properties(**kwargs)
    
    return chart.configure_view(
        strokeWidth=0
    ).configure_axis(
        grid=False
    ) 