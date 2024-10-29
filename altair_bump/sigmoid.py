import numpy as np
import pandas as pd

def sigmoid_curve(x1, y1, x2, y2, n_points=100, smoothness=8):
    """Generate a smooth sigmoid curve between two points.
    
    Parameters
    ----------
    x1, y1 : float or str
        Coordinates of the starting point. x1 can be categorical (string)
    x2, y2 : float or str
        Coordinates of the ending point. x2 can be categorical (string)
    n_points : int, default=100
        Number of points to generate along the curve
    smoothness : float, default=8
        Controls the steepness of the curve. Higher values create sharper curves.
        
    Returns
    -------
    pd.DataFrame
        DataFrame containing x and y coordinates of the curve
    """
    # Handle categorical x values
    if isinstance(x1, str) or isinstance(x2, str):
        # Create numerical x values for interpolation
        x_num = np.linspace(0, 1, n_points)
        
        # Generate sigmoid curve
        x_norm = (x_num - 0) / (1 - 0) * (2 * smoothness) - smoothness
        sigmoid = 1 / (1 + np.exp(-x_norm))
        
        # Normalize sigmoid to exactly match endpoints
        sigmoid = (sigmoid - sigmoid[0]) / (sigmoid[-1] - sigmoid[0])
        
        # Scale y values
        y = y1 + (y2 - y1) * sigmoid
        
        # Create categorical x values
        x = np.array([x1] * len(x_num))
        x[-1] = x2
        
        return pd.DataFrame({'x': x, 'y': y})
    
    # Handle numerical x values
    x = np.linspace(x1, x2, n_points)
    
    # Normalize x to [-smoothness, smoothness] range for sigmoid
    x_norm = (x - x1) / (x2 - x1) * (2 * smoothness) - smoothness
    
    # Calculate sigmoid
    sigmoid = 1 / (1 + np.exp(-x_norm))
    
    # Normalize sigmoid to exactly match endpoints
    sigmoid = (sigmoid - sigmoid[0]) / (sigmoid[-1] - sigmoid[0])
    
    # Scale to match y range
    y = y1 + (y2 - y1) * sigmoid
    
    return pd.DataFrame({'x': x, 'y': y}) 