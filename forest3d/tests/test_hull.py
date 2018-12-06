import os
import unittest
import numpy as np
from shapely.geometry import Point, Polygon
from forest3d.geometry import get_raster_bbox_as_polygon
from forest3d.geometry import get_elevation
from forest3d.geometry import get_treetop_location
from forest3d.geometry import Tree

this_dir = os.path.dirname(__file__)
data_dir = os.path.join(this_dir, 'sample_data_for_testing')
test_dem = os.path.join(data_dir, 'elevation_raster.tif')

class TestHull(unittest.TestCase):
    """Tests that evaluate the make_hull() method of the Tree class."""

    def test_stem_x_critical_points_isolation(self):
        """Checks whether changes in stem_x coordinate alter y or z coordinates
        of critical points describing crown geometry."""

        tree1 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=0,
            stem_z=0)

        tree2 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=10, # this is changed
            stem_y=0,
            stem_z=0)

        tree1_critical_points = np.vstack(
           (tree1.crown_apex,
           tree1.crown_base,
           tree1.peripheral_points)
           ).T

        tree2_critical_points = np.vstack(
          (tree2.crown_apex,
           tree2.crown_base,
           tree2.peripheral_points)
           ).T

        # make sure x coordinates are different
        self.assertFalse(
          np.allclose(
            tree1_critical_points[0],
            tree2_critical_points[0]
            ))
        # make sure y and z coordinates are the same
        self.assertTrue(
          np.allclose(
            tree1_critical_points[1:3],
            tree2_critical_points[1:3]
            ))


    def test_stem_y_critical_points_isolation(self):
        """Checks whether changes in stem_y coordinate alter x or z coordinates
        of critical points describing crown geometry."""

        tree1 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=0,
            stem_z=0)

        tree2 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=10, # this is changed
            stem_z=0)

        tree1_critical_points = np.vstack(
           (tree1.crown_apex,
           tree1.crown_base,
           tree1.peripheral_points)
           ).T

        tree2_critical_points = np.vstack(
          (tree2.crown_apex,
           tree2.crown_base,
           tree2.peripheral_points)
           ).T
        # make sure x and z coordinates are the same
        self.assertTrue(
          np.allclose(
            tree1_critical_points[[0,2]],
            tree2_critical_points[[0,2]]
            ))
        # make sure y coordinates are different
        self.assertFalse(
          np.allclose(
            tree1_critical_points[1],
            tree2_critical_points[1]
            ))


    def test_stem_z_critical_points_isolation(self):
        """Checks whether changes in stem_z coordinate alter x or y coordinates
        of critical points describing crown geometry."""

        tree1 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=0,
            stem_z=0)

        tree2 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=0,
            stem_z=10) # this is changed

        tree1_critical_points = np.vstack(
           (tree1.crown_apex,
           tree1.crown_base,
           tree1.peripheral_points)
           ).T

        tree2_critical_points = np.vstack(
          (tree2.crown_apex,
           tree2.crown_base,
           tree2.peripheral_points)
           ).T

        # make sure x and y coordinates are the same
        self.assertTrue(
          np.allclose(
            tree1_critical_points[0:1],
            tree2_critical_points[0:1]
            ))
        # make sure z coordinates are different
        self.assertFalse(
          np.allclose(
            tree1_critical_points[2],
            tree2_critical_points[2]
            ))

    def test_stem_x_hull_isolation(self):
        """Checks whether changes in stem_x coordinate alter y or z coordinates
        of all points describing the crown hull."""

        x1, y1, z1 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=0,
            stem_z=0).get_hull()

        x2, y2, z2 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=10,
            stem_y=0,
            stem_z=0).get_hull()

        self.assertFalse(np.allclose(x1, x2))
        self.assertTrue(np.allclose(y1, y2))
        self.assertTrue(np.allclose(z1, z2))

    def test_stem_y_hull_isolation(self):
        """Checks whether changes in stem_y coordinate alter x or z coordinates
        of points in the crown."""

        x1, y1, z1 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=0,
            stem_z=0).get_hull()

        x2, y2, z2 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=10,
            stem_z=0).get_hull()

        self.assertTrue(np.allclose(x1, x2))
        self.assertFalse(np.allclose(y1, y2))
        self.assertTrue(np.allclose(z1, z2))

    def test_stem_z_hull_isolation(self):
        """Checks whether changes in stem_z coordinate alter x or y coordinates
        of all points describing the crown hull."""

        x1, y1, z1 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=0,
            stem_z=0).get_hull()

        x2, y2, z2 = Tree(species='Douglas-fir',
            dbh=7.5,
            height=85,
            stem_x=0,
            stem_y=0,
            stem_z=10).get_hull()

        self.assertTrue(np.allclose(x1, x2))
        self.assertTrue(np.allclose(y1, y2))
        self.assertFalse(np.allclose(z1, z2))


if __name__ == '__main__':
    unittest.main()
