import os

import numpy as np
from forest3d.geometry import (Tree, get_hull_apex_and_base,
                               get_treetop_location)


def test_stem_x_hull_isolation():
    """Changes in stem_x coordinate alter expected coordinates describing crown."""

    x1, y1, z1 = Tree(
        species='Douglas-fir',
        dbh=7.5,
        top_height=85,
        stem_x=0,
        stem_y=0,
        stem_z=0).crown

    x2, y2, z2 = Tree(
        species='Douglas-fir',
        dbh=7.5,
        top_height=85,
        stem_x=10,
        stem_y=0,
        stem_z=0).crown

    assert not np.allclose(x1, x2)
    assert np.allclose(y1, y2)
    assert np.allclose(z1, z2)

def test_stem_y_hull_isolation():
    """Changes in stem_y coordinate alter expected coordinates describing crown."""

    x1, y1, z1 = Tree(
        species='Douglas-fir',
        dbh=7.5,
        top_height=85,
        stem_x=0,
        stem_y=0,
        stem_z=0).crown

    x2, y2, z2 = Tree(
        species='Douglas-fir',
        dbh=7.5,
        top_height=85,
        stem_x=0,
        stem_y=10,
        stem_z=0).crown
    
    assert np.allclose(x1, x2)
    assert not np.allclose(y1, y2)
    assert np.allclose(z1, z2)

def test_stem_z_hull_isolation():
    """Changes in stem_z coordinate alter expected coordinates describing crown."""

    x1, y1, z1 = Tree(
        species='Douglas-fir',
        dbh=7.5,
        top_height=85,
        stem_x=0,
        stem_y=0,
        stem_z=0).crown

    x2, y2, z2 = Tree(
        species='Douglas-fir',
        dbh=7.5,
        top_height=85,
        stem_x=0,
        stem_y=0,
        stem_z=10).crown

    assert np.allclose(x1, x2)
    assert np.allclose(y1, y2)
    assert not np.allclose(z1, z2)


def test_treetop_stem_x_isolation():
    """Changes in treetop_stem_x alter expected coordinates describing crown."""

    stem1 = (0, 0, 0)
    stem2 = (10, 0, 0)

    trans1 = get_treetop_location(stem1, 75)
    trans2 = get_treetop_location(stem2, 75)

    assert not np.allclose(trans1[0], trans2[0])
    assert np.allclose(trans1[1], trans2[1])
    assert np.allclose(trans1[2], trans2[2])

def test_treetop_stem_y_isolation():
    """"Changes in treetop_stem_y alter expected coordinates describing crown."""

    stem1 = (0, 0, 0)
    stem2 = (0, 10, 0)

    trans1 = get_treetop_location(stem1, 75)
    trans2 = get_treetop_location(stem2, 75)

    assert np.allclose(trans1[0], trans2[0])
    assert not np.allclose(trans1[1], trans2[1])
    assert np.allclose(trans1[2], trans2[2])

def test_treetop_stem_z_isolation():
    """Changes in treetop_stem_z alter expected coordinates describing crown."""

    stem1 = (0, 0, 0)
    stem2 = (0, 0, 1)

    trans1 = get_treetop_location(stem1, 75)
    trans2 = get_treetop_location(stem2, 75)

    assert np.allclose(trans1[0], trans2[0])
    assert np.allclose(trans1[1], trans2[1])
    assert not np.allclose(trans1[2], trans2[2])

def test_hull_apex_and_base_consisten():
    """make_hull() has same apex and base as get_hull_apex_and_base()."""

    tree = Tree(
        species= 'Douglas-fir',
        dbh= 8.5,
        top_height= 80, 
        stem_x= 0,
        stem_y= 0,
        stem_z= 0,
        crown_radii= (10, 10, 10, 10),
        crown_ratio= 0.5,
    )

    apex1, base1 = get_hull_apex_and_base(tree.crown_radii, tree.top_height, tree.crown_ratio)
    crown_x, crown_y, crown_z = tree.crown

    apex2 = (tree.stem_x, tree.stem_y, crown_z.max())
    base2 = (tree.stem_x, tree.stem_y, crown_z.min())

    assert np.allclose(apex1, apex2)
    assert np.allclose(base1, base2)