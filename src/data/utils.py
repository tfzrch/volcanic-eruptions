import pandas as pd

"""
Setup 'Crust Type' variable as a Category.
"""

def ts_crust_type_to_cat(data):
    
    # Get categories
    categories = data['ts_crust_type'].dropna().unique().tolist()
    categories.sort(reverse = True)
    
    # Define category
    data['ts_crust_type'] = pd.Categorical(
        data['ts_crust_type'],
        categories = categories,
        ordered = True
    )
    
    # Return
    return data
