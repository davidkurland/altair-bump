import pandas as pd
import numpy as np

def prepare_rank_data(data, category_col, value_col, time_col):
    """Prepare data for bump chart by computing ranks.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame containing the data
    category_col : str
        Column name for categories
    value_col : str
        Column name for values to rank
    time_col : str
        Column name for time periods
        
    Returns
    -------
    pd.DataFrame
        DataFrame with computed ranks, where higher values get lower ranks
        (e.g., highest value gets rank 1) and ties are randomly broken
        to ensure unique ranks
    """
    if data.empty:
        raise ValueError("Input DataFrame is empty")
    
    def random_rank_with_ties(series):
        # Get initial ranks with higher values getting lower ranks
        initial_ranks = series.rank(method='min', ascending=False)
        final_ranks = initial_ranks.copy()
        
        # For each tied rank, randomly assign consecutive ranks
        for rank in initial_ranks.unique():
            mask = initial_ranks == rank
            count = mask.sum()
            if count > 1:  # If there's a tie
                tied_indices = initial_ranks[mask].index
                # Generate consecutive ranks starting from the current rank
                consecutive_ranks = np.arange(rank, rank + count)
                # Randomly assign these consecutive ranks to tied values
                np.random.shuffle(consecutive_ranks)
                final_ranks[tied_indices] = consecutive_ranks
        
        return final_ranks.astype(int)  # Cast to integer
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Preserve original index for proper alignment
    result = (data
             .assign(rank=data.groupby(time_col)[value_col]
                    .transform(random_rank_with_ties))
             .sort_values([time_col, category_col])  # Sort by time and category to maintain consistent order
             .reset_index(drop=True))
    
    return result