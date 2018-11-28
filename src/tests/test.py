import unittest
import numpy as np
from shapely.geometry import Point, Polygon
from src.geometry.geometry import get_raster_bbox_as_polygon
from src.geometry.geometry import get_elevation

test_dem = './sample_data_for_testing/elevation_raster.tif'


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestGeometryMethods(unittest.TestCase):
    def test_raster_bbox_getter_returns_polygon(self):
        """Checks whether get_raster_bbox_... return a Polygon object."""

        result = get_raster_bbox_as_polygon(test_dem)
        self.assertIsInstance(result, Polygon)

    def test_elevation_getter_invalid_bounds(self):
        """Checks whether get_elevation returns IndexError with invalid when
        point outside bounding box is queried."""

        poly = get_raster_bbox_as_polygon(test_dem)
        bounds = poly.bounds
        x = bounds[0] - 1.0  # outside left bound
        y = bounds[1] - 1.0  # outside bottom bound

        self.assertRaises(IndexError, get_elevation, *[test_dem, x, y])

    def test_elevation_getter_valid_bounds(self):
        """Checks whether get_elevation returns a float or int when a valid
        query location is used."""

        poly = get_raster_bbox_as_polygon(test_dem)
        bounds = poly.bounds
        x = np.mean(bounds[0::2])  # middle of xs
        y = np.mean(bounds[1::2])  # middle of ys

        result_type = get_elevation(test_dem, x, y).dtype.kind
        self.assertIn(result_type, ['i', 'u', 'f'])


if __name__ == '__main__':
    unittest.main()
