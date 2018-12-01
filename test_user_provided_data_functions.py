"""
Description
"""
import unittest
import geopandas as gpd
import tree_list_checker

FILE = "/data/interim/wind_river/wind_river_live_trees.shp"

def primary_data_for_test():
    gdf = gpd.read_file(FILE).sample(3)
    return gdf

gdf = primary_data_for_test()

class TestUserDataFunctionality(unittest.TestCase):
    """
    class that checks if the functionalities of the method checking user provided 
    data works accordingly
    """

    def test_empty_file_throws_error(self):
        """
        Test that if the user provides an empty tree list, 
        the function yield approriate error and message of
        ValueError
        """
        test_df = gpd.GeoDataFrame(gdf.columns)
        self.assertTrue(False, tree_list_checker(test_df))
    
    def test_pass_test_if_all_column_data_ok(self):
        """
        Test that the tree_list_checker functions returns true
        when the user provided data meet the requirements. In other words that 
        the data is of the appropriate format (CSV, SHAPEFILE, TXT) and 
        has all the required columns (x_tree, y_tree, species, crown_ratio, dbh)
        """
        pass

    def test_names_ok_but_not_datatype(self):
        """
        Checks if tree_list_checker throws appropriate error when the data contains the right
        names but the datatype is wrong. 

        """
        pass
    
    def test_data_ok_with_extra_columns(self):
        """
        Checks that the function tree_list _cheker returns is ok when the data contains besides the 
        required columns, other supplementary columns
        """
        pass
    
    def test_pass_column_in_different_order(self):
        """
        Checks that the tree_list_checker returns true when the required column and data is correct
        but columns are provided in unordered manner
        """
        pass

    def test_raise_warning_if_some_missing_values(self):
        """
        checks if the function tree_list_checker raise warning when it has rows containing missing values
        """
        pass

    def test_tree_list_bound_cheker_returns_approprate_value(self):
        """
        Checks if the list 
        """
        pass

    def test_tree_list_bound_cheker_throws_appropriate_error(self):
        pass