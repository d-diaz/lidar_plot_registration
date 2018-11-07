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

## User profile
The user is a forest manager interested in forest inventory or forest stand mensuration. They understand parameters usually measured during forest inventories, including tree species, diameter at breast height, height to live crown, etc. They also have an intuition for reasonable forms of trees and common differences between different species and sizes of trees.

The user knows how to browse the web, and can download, install, and run software packages if a clear set of reproducible instructions are provided. They probably cannot program in Python. They would probably be able to execute a Jupyter Notebook if the setup of the computing environment can be handled for them (e.g., using Binder to host a Jupyter Notebook).

## Data sources
There are two types of data used in this project:
1. Field-based measurements of forest plots and trees, identifying plot location, stem location, tree diameter, tree height, species, etc. These will be formatted as text files containing lists of trees with associated parameters, and list of plots with associated parameters.
2. Lidar point clouds collected from airborne laser scanning which overlap the forests where field measurements have been collected. These point clouds are generally formatted as LAS (or compressed as LAZ) files produced by lidar vendors.

## Use cases

### Preprocessing data

The component allows the user to load data from different formats and transform it into
a consistent format that is readable by the software

- The software presents to the user a button / or a variable to specify the input.
- The software reads the input and checks if it meets the minimum requirement as being a supported format
- The software informs the user of its evaluation (data meets requirement, or data failed to load must try a different set)
- In case of failure, the software waits for a new input.

### Drawing trees

The software draw a tree based on the data provided and wait for the user to adjust parameter accordingly

- The software displays the output from the list of trees and widgets for changing parameters such as the lean of the
tree, the height of the tree and depth of the crown.
- The user adjust the widgets by moving them left to right or right to left
- The software responds by displaying the updated shape of the trees

### Reading Lidar data

The objective is to allow a user to upload Lidar data stored in a compressed or non compressed format.

- The user clicks on add lidar data button
- The software responds by allowing the user to scroll to their data folder
- The user points the software to the folder containing Lidar data
- The software checks if the folder contains any of its supported format data. If it does then it reads it otherwise prompt the user
to specify a valid folder]
- The software reads the data and stored it to the memory

### Dynamically updating trees parameters

The objective of this use case is to order the software to Dynamically try to match parameters of the tree list provided in advance
using Lidar data as reference.

- The user request alignment of tree list parameters to lidar data.
- The software checks if the tree list is provided and if Lidar data is provided as well
- If conditions are satisfied, the software build trees from the tree list and fits a mesh
- The software tries to align trees to Lidar dataset
- The software presents the results to the user

Describing at least two use cases. For each, describe:
* The objective of the user interaction (e.g., withdraw money from an ATM); and
* The expected interactions between the user and your system.
