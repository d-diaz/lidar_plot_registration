import numpy as np
from forest3d.models.dataclass import Tree

TREE_WITH_RADIUS = {
    "species": "abc",
    "dbh": 10.0,
    "top_height": 10.0,
    "crown_ratio": 0.8,
    "crown_radius": 3.0,
    "stem_x": 5.0,
    "stem_y": 10.0,
}

TREE_WITH_RADIUS_AND_RADII = {
    "species": "abc",
    "dbh": 10.0,
    "top_height": 10.0,
    "crown_ratio": 0.8,
    "crown_radius": 3.0,
    "crown_radii": np.array((1.0, 2.0, 3.0, 4.0)),
    "stem_x": 5.0,
    "stem_y": 10.0,
}

def test_crown_radius_to_radii():
    tree = Tree.model_validate(TREE_WITH_RADIUS)
    assert tree.crown_radius == TREE_WITH_RADIUS["crown_radius"]
    assert np.all(tree.crown_radii == TREE_WITH_RADIUS["crown_radius"])

def test_tree_with_radius_and_radii():
    tree = Tree.model_validate(TREE_WITH_RADIUS_AND_RADII)
    assert tree.crown_radius == TREE_WITH_RADIUS_AND_RADII["crown_radius"]
    assert np.array_equal(tree.crown_radii, TREE_WITH_RADIUS_AND_RADII["crown_radii"])