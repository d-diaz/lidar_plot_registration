# Lidar Plot Registration
Methods for creating 3D visualizations of forest inventory plots and co-registering stem maps with lidar data.

As this project develops, it will support 3D volumetric representations of trees with the ability to incorporate uncertainty/error into field-based measurements and additional rendering parameters.

In addition to the basic value of providing a stochastic 3D visualization option for forest inventory plots, this workflow is intended to support an optimization to co-register lidar-derived data (e.g., canopy surface model or alpha-hulls of trees) with stem-mapped forest inventory data from the field. This is intended to improve the alignment of field data with remotely-sensed data to support the use of field data as training data for predictive models that rely primarily upon remotely-sensed data such as lidar and high-resolution imagery.

The incorporation of prior beliefs about the distributions of 3D forest parameters (e.g., measurement error in location of plot center, distance of trees from plot center, etc.) will be applied in a Bayesian Inverse Modeling approach to identify the values and distributions of parameters which minimize divergence between simulated forest surfaces and lidar-derived surface(s). The outcome of this optimization will include probabilistic insights about the most likely locations of forest inventory plots within a lidar scene.
