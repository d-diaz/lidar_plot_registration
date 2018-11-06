# Functional Specification

## Background.
Natural resource assessments, such as inventory or monitoring campaigns, typically involve sampling a relatively limited portion of the landscape of interest. Traditionally, these samples are statistically extrapolated across a landscape based on a simple random or stratified random sampling design. However, the emergence of remote sensing systems has fueled a growing interest in imputation models built to use remotely-sensed data and field plots as training examples. The models, which are increasingly applying machine learning algorithms for the task, can be applied to generate wall-to-wall maps that “fill in the gaps” between forest plots measured on the ground based on remotely-sensed predictor variables.

Misalignment between field-measured plots and remote sensing data introduces error into predictive models trained to classify or quantify forest conditions. More precise and accurate co-registration of field plots with remotely sensed data can thus help reduce the error introduced into predictive models approach and increase the precision with which varying forest conditions across the landscape can be distinguished.

The primary goals of this project are:
* Providing a set of functions that generate 3D point clouds representing trees based on tree measurements that are commonly collected in the field
* Interactive 3D visualization of a list of measured trees
* Implementation of an optimization algorithm which minimizes misalignment of trees simulated from ground-based measurements with a point cloud collected by an airborne laser scanner (lidar)
* Reporting goodness-of-fit and corresponding model parameters from the optimization
* 3D visualization of the optimization process

## User profile.
The user is a forest manager interested in forest inventory or forest stand mensuration. They understand parameters usually measured during forest inventories, including tree species, diameter at breast height, height to live crown, etc. They also have an intuition for reasonable forms of trees and common differences between different species and sizes of trees.

The user knows how to browse the web, and can download and install software packages if a clear set of reproducible instructions are provided. They probably cannot program in Python.

## Data sources.
There are two types of data used in this project:
1. Field-based measurements of forest plots and trees, identifying plot location, stem location, tree diameter, tree height, species, etc. These will be formatted as text files containing lists of trees with associated parameters, and list of plots with associated parameters.
2. Lidar point clouds collected from airborne laser scanning which overlap the forests where field measurements have been collected. These point clouds are generally formatted as LAS (or compressed as LAZ) files produced by lidar vendors.

## Use cases.
Describing at least two use cases. For each, describe:
* The objective of the user interaction (e.g., withdraw money from an ATM); and
* The expected interactions between the user and your system.
