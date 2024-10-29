import pytest
import pandas as pd
from altair_bump import prepare_rank_data

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'year': [2018, 2018, 2018, 2019, 2019, 2019],
        'company': ['A', 'B', 'C', 'A', 'B', 'C'],
        'value': [100, 200, 150, 180, 160, 190]
    })

def test_prepare_rank_data(sample_data):
    ranked = prepare_rank_data(
        data=sample_data,
        category_col='company',
        value_col='value',
        time_col='year'
    )
    
    assert 'rank' in ranked.columns
    assert ranked.shape[0] == sample_data.shape[0]
    
    # Check if ranks are correct for 2018 (higher value = lower rank)
    ranks_2018 = ranked[ranked['year'] == 2018]['rank'].values
    assert list(ranks_2018) == [3, 1, 2]  # 100->3, 200->1, 150->2
    
    # Check if ranks are correct for 2019
    ranks_2019 = ranked[ranked['year'] == 2019]['rank'].values
    assert list(ranks_2019) == [2, 3, 1]  # 180->2, 160->3, 190->1

def test_prepare_rank_data_ties():
    data = pd.DataFrame({
        'year': [2018, 2018, 2018],
        'company': ['A', 'B', 'C'],
        'value': [100, 100, 90]
    })
    
    ranked = prepare_rank_data(
        data=data,
        category_col='company',
        value_col='value',
        time_col='year'
    )
    
    # Check that all ranks are unique
    assert len(ranked['rank'].unique()) == len(ranked)
    
    # Check that tied values get consecutive ranks
    tied_ranks = sorted(ranked[ranked['value'] == 100]['rank'].values)
    assert tied_ranks == [1, 2]  # Higher tied values get lower ranks
    assert ranked[ranked['value'] == 90]['rank'].iloc[0] == 3  # Lowest value gets highest rank

def test_prepare_rank_data_multiple_ties():
    data = pd.DataFrame({
        'year': [2018] * 6,
        'company': ['A', 'B', 'C', 'D', 'E', 'F'],
        'value': [100, 100, 100, 90, 80, 80]
    })
    
    ranked = prepare_rank_data(
        data=data,
        category_col='company',
        value_col='value',
        time_col='year'
    )
    
    # Check that all ranks are unique
    assert len(ranked['rank'].unique()) == len(ranked)
    
    # Check that ranks are in correct range
    assert set(ranked['rank']) == {1, 2, 3, 4, 5, 6}
    
    # Check that tied values get consecutive ranks
    triple_tie_ranks = sorted(ranked[ranked['value'] == 100]['rank'].values)
    assert triple_tie_ranks == [1, 2, 3]  # Highest values get lowest consecutive ranks
    
    double_tie_ranks = sorted(ranked[ranked['value'] == 80]['rank'].values)
    assert double_tie_ranks == [5, 6]  # Lowest values get highest consecutive ranks
    
    assert ranked[ranked['value'] == 90]['rank'].iloc[0] == 4  # Middle value gets middle rank

def test_prepare_rank_data_empty():
    with pytest.raises(ValueError, match="Input DataFrame is empty"):
        prepare_rank_data(
            data=pd.DataFrame(),
            category_col='company',
            value_col='value',
            time_col='year'
        )