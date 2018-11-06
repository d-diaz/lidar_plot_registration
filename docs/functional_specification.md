# Functional Specification

## Background.
The problem being addressed.

## User profile.
The user is a forest manager interested in forest inventory or forest stand mensuration. The user is suppose to have a basic uunderstanding of parameters that are usually measured during field campains of forest inventory in the USA. The user is required to know the minimum set of parameters usually used to describe a tree. Those parameters are the height of the crown, the diameter at breast height, the width of the crown and etc.<br>

The user will have the ability to load their data if they do not wish to use the default dataset. There will be widgets allowing them to modify the parameters accordingly until satisfaction.The user is required to be able to lunch a python codebase without necessarily having programming skills. <br>

Who uses the system. What they know about the domain and computing (e.g., can browse the web, can program in Python)

## Data sources.
What data you will use and how it is structured.

## Use cases.

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
