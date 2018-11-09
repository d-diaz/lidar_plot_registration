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
| Input | A text file or a CSV file or Pandas DataFrame containing information about a single tree on each line/row. |
| Output | True/False indication of whether user-specified treelist conforms to our format requirements. |

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

## Co-registration / Optimization Components
### Point Cloud Distance Array Generator
| Aspect | Description |
| :------| :-----------|
| What it does | Reads a PLY formatted Poisson surface mesh, and calculates the distance from that mesh to each point on a regular 3D grid (Numpy meshgrid). |
| Input | Path to a Poisson surface mesh in PLY format which contains (x,y,z) coordinates of each point in the mesh; specification of desired grid resolution/spacing in x, y, and z dimensions; and specification of distance metric (e.g., 'euclidean', 'squared euclidean') and whether or not that metric is signed (+/-). |
| Output | `distance_array`, a Numpy array (meshgrid) containing the distance from each point on the regular 3D grid to the Poisson surface mesh. |

### Point Cloud Distance Calculator / Interpolator
| Aspect | Description |
| :------| :-----------|
| What it does | Estimates a distance metric for an array of 3D points (e.g., a simulated tree) from another array of 3D points (e.g., a lidar point cloud surface mesh) using [`scipy.interpolate.RegularGridInterpolator`](https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.interpolate.RegularGridInterpolator.html). |
| Input | `query_points`, a Numpy array with shape (N, 3) for which distances will be calculated; and distance_array, a Numpy meshgrid containing values of a distance metric estimated at each point of a regular 3D grid. |
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

### Use Case A

Pre-processing: In this use cases, user could access to the raw data, transform the data format and check the availablity of using the data after reading the instructions, and following condition would appear after a simple input checking:
  1. User's input is a path linking to a treelist text file. Then the **`Tree List Preprocessor`** will be called to transform the data to a formatted .txt or .csv file.
  2. User's input is a path linking to a lidar point cloud file (a LAS or LAZ file). Then the **`Point Cloud Mesher`** will be called to transfrom linked data into a PLY file.
  3. User's input is a Pandas dataframe stored in memory. No operations are required for now.
  4. An exception will be raised if user's input can not be recognized as a valid path or dataframe.
 
Format checking: When the pre-processing completed, the **`Tree List Format Checker`** will be called to check if the format of the pre-processed data conform to the formatting requirements.
  - If the format of the pre-processed data conform to the requirements, return a message indicating that the data is ready for modeling.
  - If the user-provided dataframe or tree list (and/or point cloud) did not meet specifications, an error message indicating the source of non-compliance and documentation or links to documentation with formatting requirements including field names and formats should be raised.

### Use Case B

1. In this use cases, a `TreeModel` class was created by **`3D Tree Modeler`** using the pre-processed data. 
2. The **`Single Tree Visualizer`** will be called to present the user with a 3D graphic using the `TreeModel` class created in **`3D Tree Modeler`** and its default parameter settings. Slider widgets are laid out with the graphic labeled for each 3D TreeModel parameter. 
3. The user can moves a slider widget for a 3D TreeModel parameter. Also the user will be able to input the modification of the parameter and the graphic will react to user's inputs and update the 3D TreeModel (near-)instantaneously.
4. The user grabs, rotates, etc. the 3D graphic to visually inspect the tree's shape.

### Use Case C

1. In this use cases, a `TreeModel` class was created by **`3D Tree Modeler`** using the preprocessed tree list data such as a text file or a shapefile (optional: or a PLY file generated from LAS or LAZ files). The **`3D Tree Modeler`** may be called mutiple times to generate several tree model for different trees. 
2. The **`Plot (Multi-Tree) Visualizer`** will be used to generate an interactive graphic object containing several tree model (optional: and the merging with lidar points cloud ). 
3. The user grabs, rotates, etc. the 3D graphic to visually inspect the plot. 

### Use Case D

1. In this use cases, after checking format of the tree list data using the **`Tree List Format Checker`**, the **`3D Tree Modeler`** will be called to read the tree list data in and use it to create a `TreeModel` class with the location, shape and size of the tree.
2. Generate a PLY file which contains a Possion surface mesh using **`Point Clouder Mesher`** from a LAS or LAZ file.
3. Through **`Point Cloud Distance Array Generator`**, the distance between each points on the regular 3D grid and the points on the Poisson surface mesh is calculated and output into a numpy array called `distance_array`.
4. With `distance_array` from the **`Point Cloud Distance Array Generator`**, we can estimate distance metric for the `TreeModel` from the Poisson surface mesh using the **`Point Cloud Distance Calculator`** and obtain the estimated `distances`, a Numpy array containing calculated distances for N queried points.
5. By repeating the step 3&4 above, we will get a series of tree models. The **`Optimization Routine`** allow us to take mutiple tree models in and get `OptimizationResult` objects which contains multiple attributes and traces related to the process of optimization. The `OptimizationResult` can even generate a summary report in tabular describing the optimization result.
6. The `OptimizationResult` can be visualized by **`Dynamic OptimizationResult Visualizer`** to get a interactive Plotly Graph Object to show the process of optimization.

## Preliminary Plan.
1. Scripts/functions for pre-processing field-measured forest inventory data into consistent format
2. Classes/functions for generating a 3D point cloud for a single tree from field-measured attributes
3. Classes/functions for combining multiple trees into a single point cloud
4. Functions for plotting 3D point clouds
5. Process for generating a Poisson Surface mesh from lidar data
6. Process for calculating the distance of points on a regular 3D grid from the lidar-derived mesh
7. Function for querying this distance array with a set of simulated points, based on interpolation of query points using the regular 3D grid with pre-calculated distances from the lidar mesh.
8. Implementation of an optimization algorithm which adjusts tree simulation parameters, calculates the distance of the simulated points from the lidar-derived mesh, and iteratively minimizes this distance function.
