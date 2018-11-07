# Functional Specification

## Background
Natural resource assessments, such as inventory or monitoring campaigns, typically involve sampling a relatively limited portion of the landscape of interest. Traditionally, these samples are statistically extrapolated across a landscape based on a simple random or stratified random sampling design. However, the emergence of remote sensing systems has fueled a growing interest in imputation models built to use remotely-sensed data and field plots as training examples. The models, which are increasingly applying machine learning algorithms for the task, can be applied to generate wall-to-wall maps that “fill in the gaps” between forest plots measured on the ground based on remotely-sensed predictor variables.

Misalignment between field-measured plots and remote sensing data introduces error into predictive models trained to classify or quantify forest conditions. More precise and accurate co-registration of field plots with remotely sensed data can thus help reduce the error introduced into predictive models approach and increase the precision with which varying forest conditions across the landscape can be distinguished.

The primary goals of this project are:
* Providing a set of functions that generate 3D point clouds representing trees based on tree measurements that are commonly collected in the field
* Interactive 3D visualization of a list of measured trees
* Implementation of an optimization algorithm which minimizes misalignment of trees simulated from ground-based measurements with a point cloud collected by an airborne laser scanner (lidar)
* Reporting goodness-of-fit and corresponding model parameters from the optimization
* 3D visualization of the optimization process

## User Profile
The user is a forest manager interested in forest inventory or forest stand mensuration. They understand parameters usually measured during forest inventories, including tree species, diameter at breast height, height to live crown, etc. They also have an intuition for reasonable forms of trees and common differences between different species and sizes of trees.

The user knows how to browse the web, and can download, install, and run software packages if a clear set of reproducible instructions are provided. They probably cannot program in Python. They would probably be able to execute a Jupyter Notebook if the setup of the computing environment can be handled for them (e.g., using Binder to host a Jupyter Notebook).

## Data Sources
There are two types of data used in this project:
1. Field-based measurements of forest plots and trees, identifying plot location, stem location, tree diameter, tree height, species, etc. These will be formatted as text files containing lists of trees with associated parameters, and list of plots with associated parameters. Example plot data (stem maps and associated tree measurements) have been gathered from publicly-available sources for the Wind River Experimental Forest and HJ Andrews Experimental Forest. 
2. Lidar point clouds collected from airborne laser scanning which overlap the forests where field measurements have been collected. These point clouds are generally formatted as LAS (or compressed as LAZ) files produced by lidar vendors. Example lidar point clouds from publicly-available sources have been gathered from the HJ Andrews and Wind River forest areas.

## Use Cases
### Checking Format of a User-Provided Data
**Objective:** The user wants to check whether a treelist they have prepared conforms with formatting requirements for 3D modeling and optimization using this package.  

**Interactions:**  
1. The user opens a Jupyter Notebook named `01_Check Data Formats.ipynb`. 
2. The user reads instructions in the Notebook directing them to execute cells one-at-a-time in the Notebook.
3. Into a Jupyter Notebook cell, the user types in a path to the treelist saved as a textfile or stored in memory as a Pandas DataFrame. (Optional ->) The user types in a path to the lidar point cloud file saved as a LAS or LAZ file). These are assigned to Python objects when the user executes this cell.
4. The user executes the next Jupyter Notebook cell which calls a function that loads the inputs and checks their formatting, including whether coordinates of trees in the tree list fall entirely within the footprint of the lidar point cloud. The function returns a message indicating whether the user's tree list (and point cloud) conform to the formatting requirements for this package.
5. If the user-provided tree list (and/or point cloud) did not meet specifications, the function returns an error message indicating the source of non-compliance and documentation or links to documentation with formatting requirements including field names and formats. 

### Inspecting Parameters of the 3D TreeModel, Visualizing a Single Tree
**Objective:** The user wants to see which parameters are involved in the generation of the 3D TreeModel, and manipulate those parameters interactively to change the shape of a tree.  

**Interactions:**  
1. The user opens a Jupyter Notebook named `02_Visualize a Single Tree in 3D.ipynb`. 
2. The user reads instructions in the Notebook directing them to run all the cells in the Notebook.
3. The user executes all cells in the Notebook.
4. The user is presented with a 3D graphic using default 3D TreeModel parameter settings. Slider widgets are laid out with the graphic labeled for each 3D TreeModel parameter.
5. The user moves a slider widget for a 3D TreeModel parameter.
6. The graphic reacts to user inputs, updating the 3D TreeModel (near-)instantaneously.
6. The user grabs, rotates, etc. the 3D graphic to visually inspect the tree's shape.

### Drawing a Forest Plot in 3D
**Objective:** The user wants to visualize a list of several measured trees in 3D.  Optionally, they may also want to see how this visualization of their tree list compares with a lidar point cloud.

**Interactions:**  
1. The user opens a Jupyter Notebook named `03_Visualize a Forest Plot in 3D.ipynb`.
2. The user reads instructions in the Notebook directing them to execute cells one-at-a-time in the Notebook.
3. In a Jupyter Notebook cell, the user types in a path to a text file containing a list of trees or the name of a Pandas DataFrame containing a list of trees. (Optional ->) The user also types in a path to a lidar point cloud file saved as a LAS or LAZ file. The treelist (and optionally, point cloud) are assigned to Python objects when the user executes this cell.
4. The user executes the next Jupyter Notebook cell, which calls a function that checks if the tree list (and lidar point cloud) is formatted correctly, returning an appropriate error message if not. If the input data are formatted correcly, the cell returns an  interactive graphic showing the 3D model of the tree list, optionally overlaid with a lidar point cloud. 
5. The user grabs, rotates, etc. the 3D graphic to visually inspect the plot. 

### Co-registering a Tree List with a Lidar Point Cloud
**Objective:** The user wants to estimate the location of a field-measured tree list within a lidar point cloud covering the same area.  
**Interactions:**  
1. The user opens a Jupyter Notebook named `04_Co-register a Tree List with a Lidar Point Cloud.ipynb`. 
2. The user reads instructions in the Notebook directing them to execute cells one-at-a-time in the Notebook.
3. In a Jupyter Notebook cell, the user types in a path to the tree list text file or the name of a Pandas DataFrame, as well as a path to the lidar point cloud file. These are assigned to Python objects when the user executes this cell.
4. The user executes a Jupyter Notebook cell which runs a function to check the input formatting and begins the optimization routine if the inputs are formatted correctly. The optimization routine provides graphical or text updates during the optimization process, such as the number of simulations to be conducted and the value of the objective function at periodic increments.
5. When the optimization is completed, the user executes another Jupyter Notebook cell, which produces a table output summary of the optimization results.
6. The user executes another Jupyter Notebook cell, which produces a 3D visualization showing the optimal co-registration of the simulated 3D TreeModels for their treelist and the point cloud they provided.
7. (Optional) The user executes another Jupyter Notebook cell, which produces a 3D visualization where they can see how the simulated 3D TreeModels changed over time during the optimization.
