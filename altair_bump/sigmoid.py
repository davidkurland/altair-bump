import numpy as np
import pandas as pd

def sigmoid_curve(x1, y1, x2, y2, n_points=100, smoothness=8):
    """Generate a smooth sigmoid curve between two points."""
    # Generate x values
    x = np.linspace(x1, x2, n_points)
    
    # Normalize x to [-smoothness, smoothness] range for sigmoid
    x_norm = (x - x1) / (x2 - x1) * (2 * smoothness) - smoothness
    
    # Calculate sigmoid ensuring it starts at y1 and ends at y2
    sigmoid = (1 / (1 + np.exp(-x_norm)))
    
    # Normalize sigmoid to [0, 1] range
    sigmoid = (sigmoid - sigmoid[0]) / (sigmoid[-1] - sigmoid[0])
    
    # Scale to match y range
    y = y1 + (y2 - y1) * sigmoid
    
    return pd.DataFrame({'x': x, 'y': y}) 