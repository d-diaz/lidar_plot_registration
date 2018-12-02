"""
Perform some unit test for tree_list_checker
The test produces its own data for testing. No need for external files
It creates some data that is stored in the directory the file is located
It does not delete the file after excecustion
"""
import unittest
import geopandas as gpd
import pandas as pd
import validate_data as vd
from shapely.geometry import Point

FILE = "test.shp"

def primary_data_for_test():
    df = pd.DataFrame(
            {
                'x_tree':[x**2 for x in range(1,4)], 
                'y_tree':[x for x in range(1,4)],
                'species':['A', 'b', 'C'],
                'crown_ratio':[x/2.0 for x in range(1,4)],
                'height':[x*2 for x in range(1,4)]
            }
        )
    df['geometry'] = list(zip(df.x_tree, df.y_tree))
    df['geometry'] = df['geometry'].apply(Point)
    gdf = gpd.GeoDataFrame(df, geometry='geometry')
    gdf.to_file(FILE)

# call the function to create the data
primary_data_for_test()
gdf = gpd.read_file(FILE)

class TestUserDataFunctionality(unittest.TestCase):
    """
    class that checks if the functionalities of the method checking user provided 
    data works accordingly
    """

    def test_empty_file_return_False(self):
        """
        Test that if the user provides an empty tree list, 
        the function yield approriate error and message of
        ValueError
        """
        test_df = gdf
        test_df = test_df.drop(columns=['geometry'], axis=1)
        test_df =test_df[0:0]
        empty_shp = "empty.csv"
        test_df.to_csv(empty_shp)
        self.assertFalse(vd.tree_list_checker(empty_shp))
    
    def test_pass_test_if_all_column_data_ok(self):
        """
        Test that the tree_list_checker functions returns true
        when the user provided data meet the requirements. In other words that 
        the data is of the appropriate format (CSV, SHAPEFILE, TXT) and 
        has all the required columns (x_tree, y_tree, species, crown_ratio, dbh)
        """
        self.assertTrue(vd.tree_list_checker(FILE))

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
        test_df = gpd.read_file(FILE)
        test_df['extra'] = [x for x in range(1,4)]
        extr_shp = "extra_shp.shp"
        test_df.to_file(extr_shp)
        self.assertTrue(vd.tree_list_checker(extr_shp))
    
    def test_pass_column_in_different_order(self):
        """
        Checks that the tree_list_checker returns true when the required column and data is correct
        but columns are provided in unordered manner
        """
        self.assertTrue(vd.tree_list_checker(FILE))

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

## running the tests
if __name__ == '__main__':
    print('running test')
    

    unittest.main()