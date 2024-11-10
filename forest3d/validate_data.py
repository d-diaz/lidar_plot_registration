"""Functions for checking that user-provided data conform to required
formats.
"""

import os

import geopandas as gpd
import pandas as pd


def tree_list_checker(filename):
    """Checks if the input file of tree list dataset is a valid dataset.
    It means that the file contains the required columns such as
    'stem_x', 'stem_y', 'dbh', 'species', 'top_height' and 'cr_ratio'.
    The file can contain other atribute the user wishes.

    Parameters
    -----------
    filename:  str, path to file
        The name of the file with the extension specified.

    Returns:
    --------
    bool
        True if the file fits the format and is not null. False otherwise.
    """
    if (
        type(filename) == pd.core.frame.DataFrame
        or type(filename) == gpd.geodataframe.GeoDataFrame
    ):
        df = filename
    elif not os.path.isfile(filename):
        raise FileNotFoundError("The file does not exist.")
    else:  # check file type and open with pandas or geopandas
        file_type = os.path.basename(filename).split(".")[1]
        if file_type == "csv":
            df = pd.read_csv(filename)
        elif file_type == "shp":
            df = gpd.read_file(filename)
        else:
            raise TypeError("Unknown file type")

    # check for required columns
    STEM_X, STEM_Y = "stem_x", "stem_y"
    SPECIES = "species"
    DBH = "dbh"
    TOP_HEIGHT = "top_height"
    CR_RATIO = "cr_ratio"
    GEOMETRY = "geometry"
    REQUIRED_COLS = [STEM_X, STEM_Y, SPECIES, DBH, TOP_HEIGHT, CR_RATIO]

    if len(REQUIRED_COLS) > len(df.columns) or df.empty:  # not enough columns
        print("At least one of these required columns is missing:")
        print(", ".join(REQUIRED_COLS))
        return False
    for col in REQUIRED_COLS:
        if True not in [col.upper() in c.upper() for c in df.columns]:
            print(f"{col} not found, but is required")
            return False
    NUMERIC_COLS = REQUIRED_COLS.copy()
    NUMERIC_COLS.remove(SPECIES)
    try:
        df_columns = df.drop(columns=[GEOMETRY])
    except KeyError:  # was a dataframe, not geodataframe
        pass
    for col in df_columns:
        if True in [req_col in str(col) for req_col in NUMERIC_COLS]:
            if df[col].dtype.kind not in ["i", "f"]:
                print(f"{col} needs to be an integer or float")
                return False
    return True
