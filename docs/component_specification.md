# Component Specification

## Software components
High level description of at least 3 software components, specifying:
* what it does;
* inputs it requires; and
* outputs it provides.

Example software components:
* **data manager**, which provides a simplified interface to your data and provides application specific features (e.g., querying data subsets); and
* **visualization manager**, which displays data frames as a plot.

## Interactions to accomplish use cases.
Describe how the above software components interact to accomplish at least one of your use cases.

## Preliminary plan.
1. Scripts/functions for pre-processing field-measured forest inventory data into consistent format
2. Classes/functions for generating a 3D point cloud for a single tree from field-measured attributes
3. Classes/functions for combining multiple trees into a single point cloud
4. Functions for plotting 3D point clouds
5. Process for generating a Poisson Surface mesh from lidar data
6. Process for calculating the distance of points on a regular 3D grid from the lidar-derived mesh
7. Function for querying this distance array with a set of simulated points, based on interpolation of query points using the regular 3D grid with pre-calculated distances from the lidar mesh.
8. Implementation of an optimization algorithm which adjusts tree simulation parameters, calculates the distance of the simulated points from the lidar-derived mesh, and iteratively minimizes this distance function.
