"""Functions for generating interactive visualizations of 3D models of trees."""

import warnings

import ipyvolume as ipv
import numpy as np
import pandas as pd
import seaborn as sns
from forest3d.models.dataclass import Tree
from forest3d.models.dataframe import TreeListDataFrameModel
from forest3d.utils.geometry import get_elevation
from ipywidgets import Accordion, FloatSlider, HBox, Layout, Text, VBox

warnings.filterwarnings("ignore", message="invalid value encountered in double_scalars")
warnings.filterwarnings("ignore", message="invalid value encountered in greater_equal")
warnings.filterwarnings("ignore", message="invalid value encountered in less")
warnings.filterwarnings("ignore", message="invalid value encountered in true_divide")


def _make_tree_all_params(
    species,
    dbh,
    top_height,
    stem_x,
    stem_y,
    stem_z,
    lean_direction,
    lean_severity,
    crown_ratio,
    crown_radius_east,
    crown_radius_north,
    crown_radius_west,
    crown_radius_south,
    crown_edgeht_east,
    crown_edgeht_north,
    crown_edgeht_west,
    crown_edgeht_south,
    shape_top_east,
    shape_top_north,
    shape_top_west,
    shape_top_south,
    shape_bottom_east,
    shape_bottom_north,
    shape_bottom_west,
    shape_bottom_south,
    top_only=False,
) -> (np.ndarray, np.ndarray, np.ndarray):
    """Creates a tree and returns its crown as a hull.

    Exposes all parameters used as individual arguments.

    This is used primarily for the plotting functions in the visualization.py
    script in this package. The parameters are the same as involved in
    instantiating a Tree object.

    Returns:
    --------
    x, y, z : numpy arrays
        the x, y, and z coordinates of points that occur along the edge of the
        tree crown.
    """
    crown_radii = np.array(
        (crown_radius_east, crown_radius_north, crown_radius_west, crown_radius_south)
    )

    crown_edge_heights = np.array(
        (crown_edgeht_east, crown_edgeht_north, crown_edgeht_west, crown_edgeht_south)
    )

    crown_shapes = np.array(
        (
            (shape_top_east, shape_top_north, shape_top_west, shape_top_south),
            (
                shape_bottom_east,
                shape_bottom_north,
                shape_bottom_west,
                shape_bottom_south,
            ),
        )
    )

    tree = Tree(
        species=species,
        dbh=dbh,
        top_height=top_height,
        stem_x=stem_x,
        stem_y=stem_y,
        stem_z=stem_z,
        lean_direction=lean_direction,
        lean_severity=lean_severity,
        crown_ratio=crown_ratio,
        crown_radii=crown_radii,
        crown_edge_heights=crown_edge_heights,
        crown_shapes=crown_shapes,
        top_only=top_only,
    )

    return tree.crown


def plot_tree_with_widgets():
    """Creates and interactive plot of a tree crown with widgets to control its shape.

    Returns:
        tree_plot : ipywidgets HBox widget
            widget containing the parameter widgets and a 3D scatter plot widget.
    """
    # creating all the widgets for each parameter of the tree model
    species = Text(value="Douglas-fir", description="Species")
    dbh = FloatSlider(value=5.0, min=0, max=50, step=1.0, description="dbh")
    height = FloatSlider(
        value=75, min=0, max=150, step=1.0, description="height", orientation="vertical"
    )
    stem_x = FloatSlider(value=0, min=-10, max=10, step=1.0, description="x")
    stem_y = FloatSlider(value=0, min=-10, max=10, step=1.0, description="y")
    stem_z = FloatSlider(value=0, min=-10, max=10, step=1.0, description="z")
    lean_direction = FloatSlider(min=0, max=360, step=1.0, description="direction")
    lean_severity = FloatSlider(min=0, max=89, step=1.0, description="severity")
    crown_ratio = FloatSlider(
        value=0.65,
        min=0,
        max=1.0,
        step=0.01,
        description="crown ratio",
        orientation="vertical",
    )
    crown_radius_E = FloatSlider(value=10, min=0, max=30, step=1.0, description="east")
    crown_radius_N = FloatSlider(value=10, min=0, max=30, step=1.0, description="north")
    crown_radius_W = FloatSlider(value=10, min=0, max=30, step=1.0, description="west")
    crown_radius_S = FloatSlider(value=10, min=0, max=30, step=1.0, description="south")
    crown_edge_height_E = FloatSlider(
        value=0.3, min=0, max=1, step=0.01, description="east", orientation="vertical"
    )
    crown_edge_height_N = FloatSlider(
        value=0.3, min=0, max=1, step=0.01, description="north", orientation="vertical"
    )
    crown_edge_height_W = FloatSlider(
        value=0.3, min=0, max=1, step=0.01, description="west", orientation="vertical"
    )
    crown_edge_height_S = FloatSlider(
        value=0.3, min=0, max=1, step=0.01, description="south", orientation="vertical"
    )
    shape_top_E = FloatSlider(
        value=2.0, min=0.0, max=3.0, step=0.1, description="top, east"
    )
    shape_top_N = FloatSlider(
        value=2.0, min=0.0, max=3.0, step=0.1, description="top, north"
    )
    shape_top_W = FloatSlider(
        value=2.0, min=0.0, max=3.0, step=0.1, description="top, west"
    )
    shape_top_S = FloatSlider(
        value=2.0, min=0.0, max=3.0, step=0.1, description="top, south"
    )
    shape_bot_E = FloatSlider(
        value=2.0, min=0.0, max=3.0, step=0.1, description="bottom, east"
    )
    shape_bot_N = FloatSlider(
        value=2.0, min=0.0, max=3.0, step=0.1, description="bottom, north"
    )
    shape_bot_W = FloatSlider(
        value=2.0, min=0.0, max=3.0, step=0.1, description="bottom, west"
    )
    shape_bot_S = FloatSlider(
        value=2.0, min=0.0, max=3.0, step=0.1, description="bottom, south"
    )

    # Group the parameter widgets into groups of controls
    height_controls = HBox([height, crown_ratio])
    edge_height_controls = HBox(
        [
            crown_edge_height_E,
            crown_edge_height_N,
            crown_edge_height_W,
            crown_edge_height_S,
        ]
    )
    location_controls = VBox([stem_x, stem_y, stem_z])
    lean_controls = VBox([lean_direction, lean_severity])
    radius_controls = VBox(
        [crown_radius_E, crown_radius_N, crown_radius_W, crown_radius_S]
    )
    shape_controls = VBox(
        [
            shape_top_E,
            shape_top_N,
            shape_top_W,
            shape_top_S,
            shape_bot_E,
            shape_bot_N,
            shape_bot_W,
            shape_bot_S,
        ]
    )
    # create and expandable user interface
    controls = Accordion(
        [
            location_controls,
            height_controls,
            lean_controls,
            radius_controls,
            edge_height_controls,
            shape_controls,
        ]
    )
    controls.set_title(0, "Stem Location")
    controls.set_title(1, "Tree Height")
    controls.set_title(2, "Tree Lean")
    controls.set_title(3, "Crown Radius")
    controls.set_title(4, "Crown Edge Heights")
    controls.set_title(5, "Crown Shapes")

    # create the 3D scatter widget
    tree_scatter = ipv.quickscatter(
        x=np.random.rand(
            100,
        )
        * 100
        - 50,
        y=np.random.rand(
            100,
        )
        * 100
        - 50,
        z=np.random.rand(
            100,
        )
        * 170
        - 10,
        marker="sphere",
        color="green",
        size=1,
    )
    # define some visualization parameters of the scatter plot
    tree_scatter.figure.xlim = [-50, 50]
    tree_scatter.figure.ylim = [-50, 50]
    tree_scatter.figure.zlim = [-10, 160]

    tree_scatter.figure.camera.up = [0, 1, 0]
    tree_scatter.figure.camera.position = (
        -0.03944879903076046,
        -3.097863509106879,
        0.27417047137158385,
    )

    def on_value_change(*args):  # noqa: ARG001
        """Updates values of scatter plot when parameter widgets are updated."""
        new_x, new_y, new_z = _make_tree_all_params(
            species.value,
            dbh.value,
            height.value,
            stem_x.value,
            stem_y.value,
            stem_z.value,
            lean_direction.value,
            lean_severity.value,
            crown_ratio.value,
            crown_radius_E.value,
            crown_radius_N.value,
            crown_radius_W.value,
            crown_radius_S.value,
            crown_edge_height_E.value,
            crown_edge_height_N.value,
            crown_edge_height_W.value,
            crown_edge_height_S.value,
            shape_top_E.value,
            shape_top_N.value,
            shape_top_W.value,
            shape_top_S.value,
            shape_bot_E.value,
            shape_bot_N.value,
            shape_bot_W.value,
            shape_bot_S.value,
        )

        tree_scatter.figure.scatters[0].x = new_x
        tree_scatter.figure.scatters[0].y = new_y
        tree_scatter.figure.scatters[0].z = new_z

    # set up all widgets to trigger update to scatter plot upon changed value
    species.observe(on_value_change, "value")
    dbh.observe(on_value_change, "value")
    height.observe(on_value_change, "value")
    stem_x.observe(on_value_change, "value")
    stem_y.observe(on_value_change, "value")
    stem_z.observe(on_value_change, "value")
    lean_direction.observe(on_value_change, "value")
    lean_severity.observe(on_value_change, "value")
    crown_ratio.observe(on_value_change, "value")
    crown_radius_E.observe(on_value_change, "value")
    crown_radius_N.observe(on_value_change, "value")
    crown_radius_W.observe(on_value_change, "value")
    crown_radius_S.observe(on_value_change, "value")
    crown_edge_height_E.observe(on_value_change, "value")
    crown_edge_height_N.observe(on_value_change, "value")
    crown_edge_height_W.observe(on_value_change, "value")
    crown_edge_height_S.observe(on_value_change, "value")
    shape_top_E.observe(on_value_change, "value")
    shape_top_N.observe(on_value_change, "value")
    shape_top_W.observe(on_value_change, "value")
    shape_top_S.observe(on_value_change, "value")
    shape_bot_E.observe(on_value_change, "value")
    shape_bot_N.observe(on_value_change, "value")
    shape_bot_W.observe(on_value_change, "value")
    shape_bot_S.observe(on_value_change, "value")

    return HBox([controls, tree_scatter], layout=Layout(width="100%"))


def plot_tree_list(trees: TreeListDataFrameModel, dem=None, sample=None):
    """Plots an interactive 3D view of a tree list.

    Parameters
    -----------
    trees (TreeListDataFrameModel): a validated dataframe or geodataframe
    dem : path to elevation raster
        raster readable by rasterio, will be used to calculate elevation on
        a grid and produce
    """
    spp = pd.unique(trees.species)
    palette = sns.color_palette("colorblind", len(spp))

    # get elevation raster to display as surface underneath trees
    if dem is not None:
        # calculate z locations of the tree stems based on the dem
        trees["stem_z"] = get_elevation(dem, trees["stem_x"], trees["stem_y"])
        # calculate a dem to display as a surface in the plot
        xs = np.linspace(trees.stem_x.min(), trees.stem_x.max(), 100)
        ys = np.linspace(trees.stem_y.min(), trees.stem_y.max(), 100)
        xx, yy = np.meshgrid(xs, ys)
        elevation = get_elevation(dem, xx.flatten(), yy.flatten())
        elevation_surface = elevation.reshape(xs.shape[0], ys.shape[0])
    else:
        if "stem_z" not in trees.columns:
            trees["stem_z"] = 0
        else:
            pass

    if sample is not None:
        trees = trees.sample(n=sample)
    else:
        pass

    ipv.figure(width=800)
    for _, row in trees.iterrows():
        # calculate the tree's crown coordinates
        tree = Tree(
            species=row.species,
            dbh=row.dbh,
            top_height=row.top_height,
            stem_x=row.stem_x,
            stem_y=row.stem_y,
            stem_z=row.stem_z,
            crown_ratio=row.crown_ratio,
            crown_radius=row.crown_radius,
        )
        x, y, z = tree.crown
        # find out the spp index to give it a unique color
        spp_idx = np.where(spp == row.species)[0][0]
        # plot the tree crown
        ipv.plot_surface(
            x.reshape((50, 32)),
            y.reshape((50, 32)),
            z.reshape((50, 32)),
            color=[palette[spp_idx]],
        )
    if dem is not None:
        ipv.plot_surface(xx, yy, elevation_surface, color="brown")
    else:
        pass

    ipv.xlim(trees.stem_x.min() - 20, trees.stem_x.max() + 20)
    ipv.ylim(trees.stem_y.min() - 20, trees.stem_y.max() + 20)
    ipv.zlim(trees.stem_z.min(), trees.stem_z.min() + trees.top_height.max() + 20)
    ipv.style.use("minimal")
    ipv.squarelim()
    ipv.show()
