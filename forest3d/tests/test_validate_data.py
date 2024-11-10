import geopandas as gpd
import pandas as pd
import pytest
from forest3d import validate_data as vd
from shapely.geometry import Point

TEST_SHAPEFILE_FILENAME = "test.shp"
TEST_CSV_FILENAME = "test.csv"

df = pd.DataFrame({
    "stem_x": [x**2 for x in range(1, 4)],
    "stem_y": [x for x in range(1, 4)],
    "species": ["A", "b", "C"],
    "cr_ratio": [x / 2.0 for x in range(1, 4)],
    "dbh": [x * 1.20 for x in range(1, 4)],
    "top_height": [x * 2 for x in range(1, 4)]
})

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.stem_x, df.stem_y), crs=4326)


def test_empty_file_return_False(tmp_path):
    """Test whether providing an empty tree list fails tree_list_checker."""
    empty_gdf = gdf[0:0]
    outpath = tmp_path / TEST_CSV_FILENAME
    empty_gdf.to_csv(outpath)
    assert len(empty_gdf) == 0
    assert not vd.tree_list_checker(outpath)


def test_pass_test_if_all_column_data_ok(tmp_path):
    """tree_list_checker returns True with valid data.
    
    In other words data are appropriate format (CSV, SHAPEFILE, TXT) and have all the 
    required columns...
    """
    outpath = tmp_path / TEST_SHAPEFILE_FILENAME
    gdf.to_file(outpath)
    assert vd.tree_list_checker(outpath)

def test_names_ok_but_not_datatype(tmp_path):
    """tree_list_checker returns False when the data have wrong the datatype."""
    test_df = gdf.drop(columns=["stem_x"], axis=1)
    test_df["stem_x"] = ["a", "b", "c"]
    outpath = tmp_path / TEST_SHAPEFILE_FILENAME
    test_df.to_file(outpath)
    assert not vd.tree_list_checker(outpath)

def test_data_ok_with_extra_columns(tmp_path):
    """tree_list_checker returns True when supplementary columns exist."""
    test_df = gdf.copy()
    test_df["extra"] = [x for x in range(1, 4)]
    outpath = tmp_path / TEST_SHAPEFILE_FILENAME
    test_df.to_file(outpath)
    assert vd.tree_list_checker(outpath)