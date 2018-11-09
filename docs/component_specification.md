# Component Specification

## Data Loading and Pre-Processing Components
### Tree List Pre-Processors
| Aspect | Description |
| :------| :-----------|
| What it does | Transforms plot data from different formats into a consistent format. |
| Input | Tree data from external sources are currently in two formats: text files, and a shapefile. |
| Output | A text file (CSV or TXT) for each plot containing consistently formatted tree measurements from that plot. |

### Tree List Format Checker
| Aspect | Description |
| :------| :-----------|
| What it does | Checks to see whether a user-provided tree list conforms with format being used for 3D modeling |
| Input | A text file (CSV or TXT) or Pandas DataFrame containing information about a single tree on each line/row. |
| Output | True/False indication of whether user-specified treelist conforms to our format requirements. |

### Tree List Within Lidar Bounds Checker
| Aspect | Description |
| :------| :-----------|
| What it does | Checks to see whether the locations of trees within a user-provided tree list fall within the bounding box of a user-provided lidar point cloud file |
| Input | A text file (CSV or TXT) or Pandas DataFrame containing information about a single tree on each line/row, path to a lidar point cloud in LAS or LAZ format. |
| Output | True/False indication of whether user-specified treelist falls entirely within the bounds of the point cloud. |

## Geometry Components
### Point Cloud Mesher
| Aspect | Description |
| :------| :-----------|
| What it does | Reads a lidar point cloud, defines geographic coordinate system, generates a Poisson surface mesh. |
| Input | Path to a lidar point cloud in LAS or LAZ format. |
| Output | A Poisson surface mesh saved to hard drive in PLY format. |

### 3D Tree Modeler / Simulator
| Aspect | Description |
| :------| :-----------|
| What it does | A `TreeModel` class which has at least two simulator methods: `generate_hull()` and `generate_volume()` to generate 3D point clouds depicting the trunk and crown of a tree. Modeled off of [`skimage.draw.ellipsoid`](https://github.com/scikit-image/scikit-image/blob/master/skimage/draw/draw3d.py#L5). |
| Input | `TreeModel` class is initialized with parameters describing the location, size, and shape of the tree. |
| Output | An instance of the `TreeModel` class which has simulator methods that can be called to generate Numpy arrays of shape (N, 3) containing N 3D points representing the tree. |

### 3D Plot Modeler
| Aspect | Description |
| :------| :-----------|
| What it does | Generates a collection of 3D Tree Models from a list of trees |
| Input | A text file (CSV or TXT) or Pandas DataFrame containing information about a single tree on each line/row. |
| Output | A list or array of instances of the `TreeModel` class initiated with the values of each tree in the tree list. |

## Co-registration / Optimization Components
### Point Cloud Distance Array Generator
| Aspect | Description |
| :------| :-----------|
| What it does | Reads a PLY formatted Poisson surface mesh, and calculates the distance from each point on a regular 3D grid (Numpy meshgrid) to the nearest point on the mesh. |
| Input | Path to a Poisson surface mesh in PLY format which contains (x,y,z) coordinates of each point in the mesh; specification of desired grid resolution/spacing in x, y, and z dimensions; and specification of distance metric (e.g., 'euclidean', 'squared euclidean') and whether or not that metric is signed (+/-). |
| Output | `distance_array`, a Numpy array (meshgrid) containing the distance from each point on the regular 3D grid to the Poisson surface mesh. |

### Point Cloud Distance Calculator / Interpolator
| Aspect | Description |
| :------| :-----------|
| What it does | Estimates a distance metric for an array of 3D points (e.g., a simulated tree) from another array of 3D points (e.g., a lidar point cloud surface mesh) using [`scipy.interpolate.RegularGridInterpolator`](https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.interpolate.RegularGridInterpolator.html). |
| Input | `query_points`, a Numpy array with shape (N, 3) for which distances will be calculated; and `distance_array`, a Numpy meshgrid containing values of a distance metric estimated at each point of a regular 3D grid. |
| Output | `distances`, a Numpy array with shape (N, 1) containing calculated distances for N queried points. |

### Optimization Routine
| Aspect | Description |
| :------| :-----------|
| What it does | Given a list of trees, simulates a point cloud using 3D modeling parameters, calculates a distance metric, and iteratively modifies the 3D modeling parameters to minimize that distance metric. |
| Input | A list of trees as a text file or Pandas DataFrame, optional keyword arguments for optimization settings (e.g., number of steps). |
| Output | `OptimizationResult` object, with attributes including optimized parameter values, the optimal distance metric achieved, a trace (array) for each simulation parameter showing how that parameter evolved during the optimization, and a trace (array) showing how the distance metric evolved over the optimization. This object will also have a class method which generates a summary report in tabular form describing the optimization results. |

## Visualization Components
### Single Tree Visualizer
| Aspect | Description |
| :------| :-----------|
| What it does | Produces an interactive visualization of a tree in 3D. Allows the user to modify parameters using widgets. |
| Input | A Numpy array with shape (N, 3) containing 3D points, such as the output of a `TreeModel` simulator method. |
| Output | A Plotly Graph Object FigureWidget containing 3D graph objects (e.g., Scatter3D, Scattergl, and/or Mesh3D) representing the point cloud of a single tree and slider widgets for adjusting TreeModel parameters.

### Plot (Multi-Tree) Visualizer
| Aspect | Description |
| :------| :-----------|
| What it does | Produces an interactive visualization of multiple trees in 3D. Allows users to zoom in/out and shift the angle to see the model. |
| Input | A list-like collection of Numpy arrays with shape (N, 3), such as a list of outputs from multiple `TreeModel` simulations. |
| Output | A Plotly Graph Object FigureWidget containing 3D Graph Objects (e.g., Scatter3D, Scattergl, and/or Mesh3D) representing the simulated point clouds from multiple trees. |

### Dynamic OptimizationResult Visualizer
| Aspect | Description |
| :------| :-----------|
| What it does | Visualizes the progression of the optimization routine showing how the 3D points from simulated trees evolve during the optimization. |
| Input | An `OptimizationResult` object. |
| Output | A Plotly Graph Object FigureWidget which animates or allows the user to use a slider widget to step through optimization steps to visualize how simulated tree point clouds moved during the optimization. |


## Interactions to Accomplish Use Cases.

### Use Case A: Checking format of raw user-provided data 
`Tree List Format Checker` and `Tree List Within Lidar Bounds Checker` will be called to check if the format of the pre-processed data conform to the formatting requirements and if the tree list falls within the bounds of the user-provided lidar data.

### Use Case B: Visually Inspecting a 3D Tree Model
An instance of the `TreeModel` class is initialized with default values and displayed using the `Single Tree Visualizer` component.

### Use Case C: Drawing a Forest Plot in 3D
The `3D Plot Modeler` reads in a treelist, utilizes the `Tree List Format Checker` to ensure it meets formatting requirements, instantiates a `TreeModel` object for each tree in the treelist and simulates a 3D point cloud of it, generating a list-like collection of 3D point clouds of simulated trees. The `Plot (Multi-Tree) Visualizer` is then called with this list of trees, and an interactive graphic with several trees is produced.

### Use Case D: Co-registering a Tree List with a Lidar Point Cloud
Before optimization commences, the `Tree List Format Checker` and `Tree List Within Lidar Bounds Checker` will be called to check if the format of the pre-processed data conform to the formatting requirements and if the tree list falls within the bounds of the user-provided lidar data. Also before any optimization begins, the `Point Clouder Mesher` will convert the user-provided point cloud file into a 3D surface mesh, and the `Point Cloud Distance Array Generator` will be used to compute the distance between each points on the regular 3D grid from the points on the Poisson surface mesh of the lidar point cloud. 

The `Optimization Routine` is initialized with the user-provided treelist parameters. The `3D Plot Modeler` will read the tree list and generate 3D models of all the trees in it. The `Point Cloud Distance Calculator` will be used to calculate the distance of the simulated trees from the mesh. This distance metric is the objective function that the `Optimization Routine` seeks to minimize. An  `OptimizationResult` object is returned which contains multiple attributes and traces related to the process of optimization. This object allows the user to execute methods including generation of a tabular report summarizing the optimization results. TheThe `OptimizationResult` object can also be submitted as input to the `Dynamic OptimizationResult Visualizer` to produce a interactive Plotly Graph Object to visualize the process of optimization.

## Preliminary Plan.
1. Scripts/functions for pre-processing field-measured forest inventory data into consistent format
2. Classes/functions for generating a 3D point cloud for a single tree from field-measured attributes
3. Classes/functions for combining multiple trees into a single point cloud
4. Functions for plotting 3D point clouds
5. Process for generating a Poisson Surface mesh from lidar data
6. Process for calculating the distance of points on a regular 3D grid from the lidar-derived mesh
7. Function for querying this distance array with a set of simulated points, based on interpolation of query points using the regular 3D grid with pre-calculated distances from the lidar mesh.
8. Implementation of an optimization algorithm which adjusts tree simulation parameters, calculates the distance of the simulated points from the lidar-derived mesh, and iteratively minimizes this distance function.
