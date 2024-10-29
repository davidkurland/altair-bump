import pytest
import numpy as np
import pandas as pd
from altair_bump import sigmoid_curve

def test_sigmoid_curve_basic():
    curve = sigmoid_curve(0, 0, 1, 1)
    assert isinstance(curve, pd.DataFrame)
    assert len(curve) == 100  # default n_points
    assert all(col in curve.columns for col in ['x', 'y'])
    
def test_sigmoid_curve_endpoints():
    x1, y1 = 0, 0
    x2, y2 = 1, 1
    curve = sigmoid_curve(x1, y1, x2, y2)
    
    # Check if curve starts and ends at the given points (approximately)
    assert np.isclose(curve['x'].iloc[0], x1, atol=1e-10)
    assert np.isclose(curve['y'].iloc[0], y1, atol=1e-10)
    assert np.isclose(curve['x'].iloc[-1], x2, atol=1e-10)
    assert np.isclose(curve['y'].iloc[-1], y2, atol=1e-10)

def test_sigmoid_curve_monotonicity():
    curve = sigmoid_curve(0, 0, 1, 1)
    # Check if x and y values are strictly increasing
    assert all(np.diff(curve['x']) > 0)
    assert all(np.diff(curve['y']) > 0)

def test_sigmoid_curve_custom_points():
    n_points = 50
    curve = sigmoid_curve(0, 0, 1, 1, n_points=n_points)
    assert len(curve) == n_points

def test_sigmoid_curve_smoothness():
    # Test different smoothness parameters
    curve1 = sigmoid_curve(0, 0, 1, 1, smoothness=2)
    curve2 = sigmoid_curve(0, 0, 1, 1, smoothness=8)
    
    # Calculate rate of change at middle point
    mid1 = np.gradient(curve1['y'].values)[len(curve1)//2]
    mid2 = np.gradient(curve2['y'].values)[len(curve2)//2]
    
    # Higher smoothness should result in steeper curve at midpoint
    assert abs(mid2) > abs(mid1) 