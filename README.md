# Altair Bump Charts

A Python library for creating elegant bump charts using Altair. Perfect for visualizing ranking changes over time.

## Installation

```bash
pip install altair-bump
```

## Basic Usage

```python
import pandas as pd
from altair_bump import bump_chart, prepare_rank_data

# Create sample data
data = pd.DataFrame({
    'year': [2018, 2019, 2020] * 3,
    'company': ['Apple', 'Google', 'Microsoft'] * 3,
    'revenue': [265.6, 161.9, 110.4, 260.2, 182.5, 125.8, 274.5, 257.6, 143.0]
})

# Prepare ranked data
ranked_data = prepare_rank_data(
    data=data,
    category_col='company',
    value_col='revenue',
    time_col='year'
)

# Create basic bump chart
chart = bump_chart(
    data=ranked_data,
    x='year',
    y='rank',
    group='company',
    interpolate='sigmoid'
)
```

## Features

- **Smooth Transitions**: Sigmoid curve interpolation between points
- **Rank Handling**: 
  - Proper handling of rank ties with configurable random assignment
  - Support for entries/exits from rankings
  - Automatic rank calculation from raw values
- **Styling Options**:
  - Line thickness and opacity
  - Custom color schemes
  - Adjustable curve smoothness
  - Configurable point sizes
  - Axis and label customization

## API Reference

### prepare_rank_data()
```python
prepare_rank_data(data, category_col, value_col, time_col)
```
Prepares data for bump chart visualization by computing ranks.

**Parameters:**
- `data`: DataFrame containing the raw data
- `category_col`: Column name for categories (e.g., 'company')
- `value_col`: Column name for values to rank (e.g., 'revenue')
- `time_col`: Column name for time periods (e.g., 'year')

### bump_chart()
```python
bump_chart(data, x, y, group=None, color=None, smooth=8, line_size=3,
          point_size=100, interpolate='linear', **kwargs)
```
Creates a bump chart visualization.

**Parameters:**
- `data`: DataFrame with ranked data
- `x`: Column name for x-axis
- `y`: Column name for y-axis (typically 'rank')
- `group`: Column name for grouping
- `color`: Column name for color encoding (defaults to group)
- `smooth`: Curve smoothness (default=8)
- `line_size`: Line width (default=3)
- `point_size`: Point size (default=100)
- `interpolate`: 'linear' or 'sigmoid'

## Examples

Check out the [examples directory](docs/examples/) for:
- Basic bump charts
- Custom styling examples
- Handling rank ties
- Different interpolation methods

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

Inspired by:
- [ggbump](https://github.com/davidsjoberg/ggbump)