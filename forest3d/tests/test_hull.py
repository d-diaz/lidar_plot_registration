import os
import unittest
import numpy as np
from forest3d.geometry import get_treetop_location
from forest3d.geometry import get_hull_apex_and_base
from forest3d.geometry import Tree

this_dir = os.path.dirname(__file__)
data_dir = os.path.join(this_dir, 'sample_data_for_testing')
test_dem = os.path.join(data_dir, 'elevation_raster.tif')


class TestHull(unittest.TestCase):
    """Tests that evaluate the make_hull() method of the Tree class."""

    def test_stem_x_hull_isolation(self):
        """Checks whether changes in stem_x coordinate alter y or z coordinates
        of all points describing the crown hull."""

        x1, y1, z1 = Tree(
            species='Douglas-fir',
            dbh=7.5,
            top_height=85,
            stem_x=0,
            stem_y=0,
            stem_z=0).get_crown()

        x2, y2, z2 = Tree(
            species='Douglas-fir',
            dbh=7.5,
            top_height=85,
            stem_x=10,
            stem_y=0,
            stem_z=0).get_crown()

        self.assertFalse(np.allclose(x1, x2))
        self.assertTrue(np.allclose(y1, y2))
        self.assertTrue(np.allclose(z1, z2))

    def test_stem_y_hull_isolation(self):
        """Checks whether changes in stem_y coordinate alter x or z coordinates
        of points in the crown."""

        x1, y1, z1 = Tree(
            species='Douglas-fir',
            dbh=7.5,
            top_height=85,
            stem_x=0,
            stem_y=0,
            stem_z=0).get_crown()

        x2, y2, z2 = Tree(
            species='Douglas-fir',
            dbh=7.5,
            top_height=85,
            stem_x=0,
            stem_y=10,
            stem_z=0).get_crown()

        self.assertTrue(np.allclose(x1, x2))
        self.assertFalse(np.allclose(y1, y2))
        self.assertTrue(np.allclose(z1, z2))

    def test_stem_z_hull_isolation(self):
        """Checks whether changes in stem_z coordinate alter x or y coordinates
        of all points describing the crown hull."""

        x1, y1, z1 = Tree(
            species='Douglas-fir',
            dbh=7.5,
            top_height=85,
            stem_x=0,
            stem_y=0,
            stem_z=0).get_crown()

        x2, y2, z2 = Tree(
            species='Douglas-fir',
            dbh=7.5,
            top_height=85,
            stem_x=0,
            stem_y=0,
            stem_z=10).get_crown()

        self.assertTrue(np.allclose(x1, x2))
        self.assertTrue(np.allclose(y1, y2))
        self.assertFalse(np.allclose(z1, z2))

    def test_treetop_stem_x_isolation(self):
        """Checks whether changes in stem_z coordinate alter x or y coordinates
        of all points describing the crown hull."""

        stem1 = (0, 0, 0)
        stem2 = (10, 0, 0)

        trans1 = get_treetop_location(stem1, 75)
        trans2 = get_treetop_location(stem2, 75)

        self.assertFalse(np.allclose(trans1[0], trans2[0]))
        self.assertTrue(np.allclose(trans1[1], trans2[1]))
        self.assertTrue(np.allclose(trans1[2], trans2[2]))

    def test_treetop_stem_y_isolation(self):
        """Checks whether changes in stem_z coordinate alter x or y coordinates
        of all points describing the crown hull."""

        stem1 = (0, 0, 0)
        stem2 = (0, 10, 0)

        trans1 = get_treetop_location(stem1, 75)
        trans2 = get_treetop_location(stem2, 75)

        self.assertTrue(np.allclose(trans1[0], trans2[0]))
        self.assertFalse(np.allclose(trans1[1], trans2[1]))
        self.assertTrue(np.allclose(trans1[2], trans2[2]))

    def test_treetop_stem_z_isolation(self):
        """Checks whether changes in stem_z coordinate alter x or y coordinates
        of all points describing the crown hull."""

        stem1 = (0, 0, 0)
        stem2 = (0, 0, 1)

        trans1 = get_treetop_location(stem1, 75)
        trans2 = get_treetop_location(stem2, 75)

        self.assertTrue(np.allclose(trans1[0], trans2[0]))
        self.assertTrue(np.allclose(trans1[1], trans2[1]))
        self.assertFalse(np.allclose(trans1[2], trans2[2]))

    def test_hull_apex_and_base_consisten(self):
        """Checks whether make_hull() has same apex and base as estimated from
        get_hull_apex_and_base()."""

        SPECIES = 'Douglas-fir'
        DBH = 8.5
        CROWN_RADII = (10, 10, 10, 10)
        TOP_HT = 80
        CROWN_RATIO = 0.50
        STEM_X, STEM_Y, STEM_Z = (0, 0, 0)

        apex1, base1 = get_hull_apex_and_base(CROWN_RADII, TOP_HT, CROWN_RATIO)
        crown = Tree(
            SPECIES,
            DBH,
            TOP_HT,
            STEM_X,
            STEM_Y,
            STEM_Z,
            crown_ratio=CROWN_RATIO).get_crown()

        crown_x, crown_y, crown_z = crown
        apex2 = (STEM_X, STEM_Y, crown_z.max())
        base2 = (STEM_X, STEM_Y, crown_z.min())

        self.assertTrue(np.allclose(apex1, apex2))
        self.assertTrue(np.allclose(base1, base2))


if __name__ == '__main__':
    unittest.main()
