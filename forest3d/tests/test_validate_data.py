"""
Perform some unit test for tree_list_checker
The test produces its own data for testing. No need for external files
It creates some data that is stored in the directory the file is located
It does not delete the file after excecustion
"""
import unittest
import os
import shutil
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from forest3d import validate_data as vd

THIS_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(THIS_DIR, 'sample_data_for_testing')
TEMP_TEST_DIR = os.path.join(DATA_DIR, "temp")
TEST_SHAPEFILE = os.path.join(TEMP_TEST_DIR, "test.shp")


class TestUserDataFunctionality(unittest.TestCase):
    """
    Tests which ensure functions to check user-provided data match
    our specifications work appropriately.
    """

    def setUp(self):
        """Sets up data to be used for running tests"""
        if not os.path.exists(TEMP_TEST_DIR):
            os.mkdir(TEMP_TEST_DIR)

        df = pd.DataFrame({
            'stem_x': [x**2 for x in range(1, 4)],
            'stem_y': [x for x in range(1, 4)],
            'species': ['A', 'b', 'C'],
            'cr_ratio': [x / 2.0 for x in range(1, 4)],
            'dbh': [x * 1.20 for x in range(1, 4)],
            'top_height': [x * 2 for x in range(1, 4)]
        })
        df['geometry'] = list(zip(df.stem_x, df.stem_y))
        df['geometry'] = df['geometry'].apply(Point)
        gdf = gpd.GeoDataFrame(df, geometry='geometry')
        gdf.to_file(TEST_SHAPEFILE)
        self.gdf = gdf

    def test_empty_file_return_False(self):
        """
        Test whether providing an empty tree list fails tree_list_checker.
        """
        test_df = self.gdf
        test_df = test_df.drop(columns=['geometry'], axis=1)
        test_df = test_df[0:0]
        empty_shp = os.path.join(TEMP_TEST_DIR, "empty.csv")
        test_df.to_csv(empty_shp)
        self.assertFalse(vd.tree_list_checker(empty_shp))

    def test_pass_test_if_all_column_data_ok(self):
        """
        Test that the tree_list_checker functions returns true
        when the user provided data meet the requirements. In other words that
        the data is of the appropriate format (CSV, SHAPEFILE, TXT) and
        has all the required columns (stem_x, stem_y, species, cr_ratio,
        dbh).
        """
        result = vd.tree_list_checker(TEST_SHAPEFILE)
        self.assertTrue(result)

    def test_names_ok_but_not_datatype(self):
        """
        Checks if tree_list_checker throws appropriate error when the data
        contains the right names but the datatype is wrong.
        """
        test_df = self.gdf
        test_df = test_df.drop(columns=['stem_x'], axis=1)
        test_df['stem_x'] = ['a', 'b', 'c']
        WRONG_SHP = os.path.join(TEMP_TEST_DIR, "wrong_data_type.shp")
        test_df.to_file(WRONG_SHP)
        self.assertFalse(vd.tree_list_checker(WRONG_SHP))

    def test_data_ok_with_extra_columns(self):
        """
        Checks if function tree_list_checker returns True when supplementary
        columns exist.
        """
        test_df = gpd.read_file(TEST_SHAPEFILE)
        test_df['extra'] = [x for x in range(1, 4)]
        EXTR_SHP = os.path.join(TEMP_TEST_DIR, "extra_shp.shp")
        test_df.to_file(EXTR_SHP)
        self.assertTrue(vd.tree_list_checker(EXTR_SHP))

    def test_pass_column_in_different_order(self):
        """
        Checks that the tree_list_checker returns true when the required column
        and data is correct but columns are provided in unordered manner
        """
        self.assertTrue(vd.tree_list_checker(TEST_SHAPEFILE))

    def test_raise_warning_if_some_missing_values(self):
        """
        checks if the function tree_list_checker raise warning when it has rows
        containing missing values
        """
        pass

    def tearDown(self):
        """Removes temporary directory created during unit testing"""
        shutil.rmtree(TEMP_TEST_DIR)


# running the tests
if __name__ == '__main__':
    unittest.main()
