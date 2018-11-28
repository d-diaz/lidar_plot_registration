import os
import unittest
import numpy as np
from shapely.geometry import Point, Polygon
from src.geometry.geometry import get_raster_bbox_as_polygon
from src.geometry.geometry import get_elevation
from src.geometry.geometry import get_treetop_location

this_dir = os.path.dirname(__file__)
data_dir = os.path.join(this_dir, 'sample_data_for_testing')
test_dem = os.path.join(data_dir, 'elevation_raster.tif')


class TestGeometryMethods(unittest.TestCase):
    def test_raster_bbox_getter_returns_polygon(self):
        """Checks whether get_raster_bbox_... return a Polygon object."""

        result = get_raster_bbox_as_polygon(test_dem)
        self.assertIsInstance(result, Polygon)

    def test_elevation_getter_single_point_out_of_bounds(self):
        """Checks whether get_elevation returns IndexError with invalid when
        point outside bounding box is queried."""

        poly = get_raster_bbox_as_polygon(test_dem)
        bounds = poly.bounds
        x = bounds[0] - 1.0  # outside left bound
        y = bounds[1] - 1.0  # outside bottom bound

        self.assertRaises(IndexError, get_elevation, *[test_dem, x, y])

    def test_elevation_getter_single_point_dtype(self):
        """Checks whether get_elevation returns a float or int when a valid
        query location is used."""

        poly = get_raster_bbox_as_polygon(test_dem)
        bounds = poly.bounds
        x = np.mean(bounds[0::2])  # middle of xs
        y = np.mean(bounds[1::2])  # middle of ys

        result = get_elevation(test_dem, x, y)
        result_type = result.dtype.kind

        self.assertIn(result_type, ['i', 'u', 'f'])

    def test_elevation_getter_array_dtype(self):
        """Checks whether get_elevation returns an array with dtype float or int
        when a valid query location is used."""

        poly = get_raster_bbox_as_polygon(test_dem)
        bounds = poly.bounds
        mean_x = np.mean(bounds[0::2])  # middle of xs
        mean_y = np.mean(bounds[1::2])  # middle of ys
        x = np.array((mean_x, mean_x))
        y = np.array((mean_y, mean_y))

        result = get_elevation(test_dem, x, y)
        result_type = result.dtype.kind
        self.assertIsInstance(result, np.ndarray)
        self.assertIn(result_type, ['i', 'u', 'f'])

    def test_treetop_getter_invalid_lean(self):
        """Checks whether get_treetop_location raises ValueError when lean >= 90
        degrees specified."""

        args = [0, 0, 0, 100]  # x, y, z, and height
        kwargs = {'lean_severity': 90}

        self.assertRaises(ValueError, get_treetop_location, *args, **kwargs)

    def test_treetop_getter_invalid_height(self):
        """Checks whether get_treetop_location raises ValueError when height < 0
        specified."""

        args = [0, 0, 0, -1]  # x, y, z, and height

        self.assertRaises(ValueError, get_treetop_location, *args)

    def test_treetop_getter_single_point_result_format(self):
        """Checks whether get_treetop_location returns a numpy array with shape
        (3,) when a single point is provided."""

        args = [0, 0, 0, 100]  # x, y, z, and height
        result = get_treetop_location(*args)
        shape = result.shape

        self.assertTrue(shape[0], 3)

    def test_treetop_getter_array_result_format(self):
        """Checks whether get_treetop_location returns a numpy array with shape
        (3,N) when lists of points are provided."""

        x = [0, 1.0]
        y = [0, 2.0]
        z = [0, 3.0]
        height = [100, 75]
        args = [x, y, z, height]  # x, y, z, and height
        result = get_treetop_location(*args)
        shape = result.shape

        self.assertTrue(shape[0], 3)
        self.assertTrue(shape[1], len(x))

    def test_treetop_getter_array_result_format(self):
        """Checks whether get_treetop_location returns ValueError when arrays
        submitted are of different shapes."""

        x = [0, 0]
        y = [0, 5]
        z = [3.0, 2.0]
        height = [100, 75, 85]
        args = [x, y, z, height]

        self.assertRaises(ValueError, get_treetop_location, *args)


if __name__ == '__main__':
    unittest.main()
