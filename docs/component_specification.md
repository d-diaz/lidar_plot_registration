# Component Specification

## Software components
### Data Loading and Pre-Processing Components
| Component | Tree List Pre-Processors |
| :-------- | :----------------------- |
| What it does | Transforms plot data from different formats into a consistent format. |
| Input | Tree data from external sources are currently in two formats: text files, and a shapefile. |
| Output | A text file (CSV or TXT) for each plot containing consistently formatted tree measurements from that plot. |

| Component | Tree List Format Checker |
| :-------- | :----------------------- |
| What it does | Checks to see whether a user-provided tree list conforms with format being used for 3D modeling. |
| Input | A text file or Pandas DataFrame containing information about a single tree on each line/row. |
| Output | True/False indication of whether user-specified treelist conforms to our format requirements. |

### Geometry Components
| Component | Point Cloud Mesher |
| :-------- | :----------------- |
| What it does | Reads a lidar point cloud, defines geographic coordinate system, generates a Poisson surface mesh. |
| Input | Path to a lidar point cloud in LAS or LAZ format. |
| Output | A Poisson surface mesh saved to hard drive in PLY format. |

| Component | 3D Tree Modeler / Simulator |
| :-------- | :-------------------------- |
| What it does | A `TreeModel` class which has at least two simulator methods: `generate_hull()` and `generate_volume()` to generate 3D point clouds depicting the trunk and crown of a tree. Modeled off of [`skimage.draw.ellipsoid`](https://github.com/scikit-image/scikit-image/blob/master/skimage/draw/draw3d.py#L5). |
| Input | `TreeModel` class is initialized with parameters describing the location, size, and shape of the tree. |
| Output | An instance of the `TreeModel` class which has simulator methods that can be called to generate Numpy arrays of shape (N, 3) containing N 3D points representing the tree. |

### Co-registration / Optimization Components
| Component | Point Cloud Distance Array Generator |
| :-------- | :----------------------------------- |
| What it does | Reads a PLY formatted Poisson surface mesh, and calculates the distance from that mesh to each point on a regular 3D grid (Numpy meshgrid). |
| Input | Path to a Poisson surface mesh in PLY format which contains (x,y,z) coordinates of each point in the mesh; specification of desired grid resolution/spacing in x, y, and z dimensions; and specification of distance metric (e.g., 'euclidean', 'squared euclidean') and whether or not that metric is signed (+/-). |
| Output | `distance_array`, a Numpy array (meshgrid) containing the distance from each point on the regular 3D grid to the Poisson surface mesh. |

| Component | Point Cloud Distance Calculator / Interpolator |
| :-------- | :--------------------------------------------- |
| What it does | Estimates a distance metric for an array of 3D points (e.g., a simulated tree) from a another array of 3D points (e.g., a lidar point cloud surface mesh) using [`scipy.interpolate.RegularGridInterpolator`](https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.interpolate.RegularGridInterpolator.html). |
| Input | `query_points`, a Numpy array with shape (N, 3) for which distances will be calculated; and distance_array, a Numpy meshgrid containing values of a distance metric estimated at each point of a regular 3D grid. |
| Output | `distances`, a Numpy array with shape (N, 1) containing calculated distances for N queried points. |

| Component | Optimization Routine |
| :-------- | :------------------- |
| What it does | Given a list of trees, simulates a point cloud using 3D modeling parameters, calculates a distance metric, and iteratively modifies the 3D modeling parameters to minimize that distance metric. |
| Input | A list of trees as a text file or Pandas DataFrame, optional keyword arguments for optimization settings (e.g., number of steps). |
| Output | `OptimizationResult` object, with attributes including optimized parameter values, the optimal distance metric achieved, a trace (array) for each simulation parameter showing how that parameter evolved during the optimization, and a trace (array) showing how the distance metric evolved over the optimization. This object will also have a class method which generates a summary report in tabular form describing the optimization results. |

### Visualization Components
| Component | Single Tree Visualizer |
| :-------- | :--------------------- |
| What it does | Produces an interactive visualization of a tree in 3D. Allows the user to modify parameters using widgets. |
| Input | A Numpy array with shape (N, 3) containing 3D points, such as the output of a `TreeModel` simulator method. |
| Output | A Plotly Graph Object FigureWidget containing 3D graph objects (e.g., Scatter3D, Scattergl, and/or Mesh3D) representing the point cloud of a single tree and slider widgets for adjusting TreeModel parameters.

| Component | Plot (Multi-Tree) Visualizer |
| :-------- | :--------------------------- |
| What it does | Produces an interactive visualization of multiple trees in 3D. Allows users to zoom in/out and shift the angle to see the model. |
| Input | A list-like collection of Numpy arrays with shape (N, 3), such as a list of outputs from multiple `TreeModel` simulations. |
| Output | A Plotly Graph Object FigureWidget containing 3D Graph Objects (e.g., Scatter3D, Scattergl, and/or Mesh3D) representing the simulated point clouds from multiple trees. |

| Component | Dynamic OptimizationResult Visualizer |
| :-------- | :------------------------------------ |
| What it does | Visualizes the progression of the optimization routine showing how the 3D points from simulated trees evolve during the optimization. |
| Input | An `OptimizationResult` object. |
| Output | A Plotly Graph Object FigureWidget which animates or allows the user to use a slider widget to step through optimization steps to visualize how simulated tree point clouds moved during the optimization. |


## Interactions to Accomplish Use Cases.
1. By using Tree List Pre-processor to transform data into the same format and using the Tree List Format Checker to check and raise an exception when minimum requirements for data are not satisfied, the software are able to preprocessing the data with reminding of failure and abnormal status.
2. To accomplish the task of "Drawing trees", Trees Assembler assembles the single tree models created by 3D Tree Modeler and using Assembled Visuailzer to generate a graph object which take the Plotly graph object created by Tree Visulizer as an significant graphic component.


## Preliminary Plan.
1. Scripts/functions for pre-processing field-measured forest inventory data into consistent format
2. Classes/functions for generating a 3D point cloud for a single tree from field-measured attributes
3. Classes/functions for combining multiple trees into a single point cloud
4. Functions for plotting 3D point clouds
5. Process for generating a Poisson Surface mesh from lidar data
6. Process for calculating the distance of points on a regular 3D grid from the lidar-derived mesh
7. Function for querying this distance array with a set of simulated points, based on interpolation of query points using the regular 3D grid with pre-calculated distances from the lidar mesh.
8. Implementation of an optimization algorithm which adjusts tree simulation parameters, calculates the distance of the simulated points from the lidar-derived mesh, and iteratively minimizes this distance function.
