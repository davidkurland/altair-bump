"""
Altair Bump Charts
=================

A Python library for creating bump charts using Altair.
"""

from .bump import bump_chart
from .sigmoid import sigmoid_curve
from .utils import prepare_rank_data

__version__ = "0.1.0"

__all__ = ['bump_chart', 'sigmoid_curve', 'prepare_rank_data'] 