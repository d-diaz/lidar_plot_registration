# Component Specification

## Software components

### Tree List Pre-processors
* **What it does:** Transforms plot data which from different formats into a consistent format.
* **Input:** Tree data from external sources are currently in two formats: text files, and a shapefile.
* **Output:** A text file (CSV or TXT) for each plot containing consistently formatted tree measurements from that plot.

### Tree List Format Checker
* **What it does:** Checks to see whether a user-provided tree list conforms with format being used for 3D modeling.
* **Input:** A text file containing information about a single tree on each line.
* **Output:** True/False indication of whether user-specified treelist conforms to our format requirements.

### Point Cloud Mesher
* **What it does:** Reads a lidar point cloud, defines geographic coordinate system, generates a Poisson surface mesh.
* **Input:** Path to a lidar point cloud in LAS or LAZ format.
* **Output:** A Poisson surface mesh saved to hard drive in PLY format.

### 3D Tree Modeler
* **What it does:** Generates a 3D point cloud depicting the trunk and crown of a tree. Has options to generate exterior crown points alone (e.g., a hull) or a grid of points that fall inside the crown.
* **Input:** Parameters describing the location, size, and shape of the tree.
* **Output:** A numpy array containing 3D points representing the tree.

### Tree Visualizer
* **What it does:** Produces an interactive visualization of a tree in 3D. Allows the user to modify parameters using widgets.
* **Input:** A 3D Tree Model.
* **Output:** A Plotly Graph Object that can be updated with widgets.

### Plot Visualizer
* **What it does:**
* **Input:**
* **Output:**

### Optimization Routine
* **What it does:**
* **Input:**
* **Output:**

### Optimization Visualizer
* **What it does:**
* **Input:**
* **Output:**

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
