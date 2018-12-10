"""Functions for checking that user-provided data conform to required
formats."""

import os
import pandas as pd
import geopandas as gpd
import numpy as np


def tree_list_checker(filename):
    """Checks if the input file of tree list dataset is a valid dataset.
    It means that the file contains the required columns such as
    'x_tree', 'y_tree', 'dbh', 'species' and the 'height' and 'crow_ratio'.
    The file can contain other atribute the user wishes.

    Parameters
    -----------
    filename:  str
            The name of the file with the extension specified

    Returns
    --------
    bool
        True if the file fits the format and is not null
        False otherwise
    """
    if not os.path.isfile(filename):
        raise FileNotFoundError('The file does not exist.')
    file_type = os.path.basename(filename).split('.')[1]
    if file_type == "csv":
        df = pd.read_csv(filename)
    elif file_type == "shp":
        df = gpd.read_file(filename)
    else:
        raise TypeError('Unknown file type')
    required_columns = ['x_tree', 'y_tree', 'specie', 'dbh', 'height', 'rat']
    if len(required_columns) > len(df.columns) or df.empty:
        return False
    for col in required_columns:
        if True not in [col.upper() in c.upper() for c in df.columns]:
            return False
    num_cols = required_columns.copy()
    num_cols.pop(2)
    try:
        df_columns = df.drop(columns=['geometry'])
    except Exception:
        print()
    for col in df_columns:
        if True in [req_col in str(col) for req_col in num_cols]:
            if (df[col].dtype != np.float64) and (df[col].dtype != np.int64):
                return False
    return True
