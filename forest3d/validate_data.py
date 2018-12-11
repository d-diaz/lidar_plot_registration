"""Functions for checking that user-provided data conform to required
formats."""

import os
import pandas as pd
import geopandas as gpd


def tree_list_checker(filename):
    """Checks if the input file of tree list dataset is a valid dataset.
    It means that the file contains the required columns such as
    'stem_x', 'stem_y', 'dbh', 'species', 'top_height' and 'cr_ratio'.
    The file can contain other atribute the user wishes.

    Parameters
    -----------
    filename:  str, path to file
        The name of the file with the extension specified.

    Returns
    --------
    bool
        True if the file fits the format and is not null. False otherwise.
    """
    if type(filename) == pd.core.frame.DataFrame:
        df = filename
    elif type(filename) == gpd.geodataframe.GeoDataFrame:
        df = filename
    elif not os.path.isfile(filename):
        raise FileNotFoundError('The file does not exist.')
    else:  # check file type and open with pandas or geopandas
        file_type = os.path.basename(filename).split('.')[1]
        if file_type == "csv":
            df = pd.read_csv(filename)
        elif file_type == "shp":
            df = gpd.read_file(filename)
        else:
            raise TypeError('Unknown file type')

    # check for required columns
    required_cols = [
        'stem_x', 'stem_y', 'species', 'dbh', 'top_height', 'cr_ratio'
    ]
    if len(required_cols) > len(df.columns) or df.empty:  # not enough columns
        print('At least one of these required columns is missing:')
        print(', '.join(required_cols))
        return False
    for col in required_cols:
        if True not in [col.upper() in c.upper() for c in df.columns]:
            print('{} not found, but is required'.format(col))
            return False
    numeric_cols = required_cols.copy()
    numeric_cols.remove('species')
    try:
        df_columns = df.drop(columns=['geometry'])
    except KeyError:  # was a dataframe, not geodataframe
        pass
    for col in df_columns:
        if True in [req_col in str(col) for req_col in numeric_cols]:
            if (df[col].dtype.kind not in ['i', 'f']):
                print('{} needs to be an integer or float'.format(col))
                return False
    return True
