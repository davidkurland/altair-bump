import pytest
import pandas as pd
import altair as alt
from altair_bump import bump_chart

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'year': [2018, 2019, 2020] * 3,
        'company': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        'rank': [1, 2, 3, 2, 1, 2, 3, 3, 1]
    })

def test_bump_chart_basic(sample_data):
    chart = bump_chart(
        data=sample_data,
        x='year',
        y='rank',
        group='company'
    )
    assert isinstance(chart, (alt.Chart, alt.LayerChart))

def test_bump_chart_invalid_input():
    with pytest.raises(ValueError):
        bump_chart(
            data=pd.DataFrame({'x': [1, 2], 'y': [1, 2]}),
            x='x',
            y='y'
        )

def test_bump_chart_sigmoid_interpolation(sample_data):
    chart = bump_chart(
        data=sample_data,
        x='year',
        y='rank',
        group='company',
        interpolate='sigmoid'
    )
    assert isinstance(chart, (alt.Chart, alt.LayerChart))

def test_bump_chart_customization(sample_data):
    chart = bump_chart(
        data=sample_data,
        x='year',
        y='rank',
        group='company',
        line_size=5,
        point_size=150,
        smooth=10
    )
    assert isinstance(chart, (alt.Chart, alt.LayerChart))