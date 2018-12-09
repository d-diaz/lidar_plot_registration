[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/d-diaz/Lidar_Plot_Registration/master)
[![Build Status](https://travis-ci.org/d-diaz/lidar_plot_registration.svg?branch=master)](https://travis-ci.org/d-diaz/lidar_plot_registration)
[![Documentation Status](https://readthedocs.org/projects/lidar-plot-registration/badge/?version=latest)](https://lidar-plot-registration.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/d-diaz/lidar_plot_registration/badge.svg?branch=master)](https://coveralls.io/github/d-diaz/lidar_plot_registration?branch=master)

# forest3d
Methods for creating 3D visualizations of forest inventory plots and co-registering stem maps with lidar data.

As this project develops, it will support 3D volumetric representations of trees with the ability to incorporate uncertainty/error into field-based measurements and additional rendering parameters.

In addition to the basic value of providing a stochastic 3D visualization option for forest inventory plots, this workflow is intended to support an optimization to co-register lidar-derived data (e.g., canopy surface model or alpha-hulls of trees) with stem-mapped forest inventory data from the field. This is intended to improve the alignment of field data with remotely-sensed data to support the use of field data as training data for predictive models that rely primarily upon remotely-sensed data such as lidar and high-resolution imagery.

The incorporation of prior beliefs about the distributions of 3D forest parameters (e.g., measurement error in location of plot center, distance of trees from plot center, etc.) will be applied in a Bayesian Inverse Modeling approach to identify the values and distributions of parameters which minimize divergence between simulated forest surfaces and lidar-derived surface(s). The outcome of this optimization will include probabilistic insights about the most likely locations of forest inventory plots within a lidar scene.

# Getting Started

## Option A: For the non-coder
If you don't want to do any coding yourself and instead just want to view and execute the code we've arleady written using our Jupyter Notebooks, use this link:  [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/d-diaz/Lidar_Plot_Registration/master) and a computing environment will be set up for you in the cloud (for free). This setup process can take several minutes, so be patient. Once that setup is done, you should be able to navigate to the "notebooks" folder of the repository and open and execute the Jupyter Notebooks without having to install anything on your own machine.

## Option B: For the coder
This Git repo utilizes the Git Large File Storage (LFS) system. Git LFS is used here to replace large files files (identified in `.gitattributes`) such as shapefiles, point clouds, and rasters with text pointers inside Git, while still storing files not excluded by `.gitignore` on GitHub. Very large geospatial data files such as point clouds (.las, .las) and rasters (.asc, .tif) are currently set up to be ignored by Git entirely because they can easily exceed GitHub storage allowances. Third party solutions for storing and sharing large datasets are used to work around this.

Use the conda package manager to reproduce the computing environment we used in developing this repo. Get [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html) to do so.

1. Install [Git LFS](https://github.com/git-lfs/git-lfs/wiki/Installation)
2. Clone this repo onto your local machine:  
`git clone https://github.com/d-diaz/Lidar_Plot_Registration.git`
3. Create a conda environment from the environment.yml file included in this repo:  
`conda env create --name forest3d --file environment.yml`
4. Activate this new conda environment:
`source activate forest3d` (Linux, OSX) or `activate forest3d` (Windows)
5. Start a Jupyter session:
`jupyter notebook`
6. In your web browser Jupyter session, navigate to the "notebooks" folder in this repo and open up one of the Jupyter Notebooks!

# Project Organization
(based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/))

    ├── LICENSE
    ├── README.md          <- You're reading it
    ├── data
    │   ├── raw            <- Raw lidar and tree list data
    │   ├── interim        <- Intermediate data that has been transformed
    │   └── processed      <- Processed data sets used for modeling/analysis
    │
    ├── docs               <- Documentation, generated using Sphinx hosted at Read the Docs.
    │  
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         and a short description, e.g. `01_Initial Data Exploration`
    │
    ├── references         <- Relevant references and other explanatory materials
    │
    ├── reports            <- Generated analysis as HTML, PDF, etc.
    │   └── figures        <- Graphics and figures used in reports
    |
    ├── setup.py           <- Source code installable as python package (`python setup.py develop`)
    ├── forest3d           <- Source code for use in this project
    │   ├── validate_data.py    <- To validate conformance of data with our specs
    │   ├── geometry.py    <- To generate 3D geometric models
    │   ├── optimize.py    <- To co-register point clouds with geometric models
    │   ├── visualize.py   <- To create interactive 3D visualizations
    │   │
    │   └── test           <- Scripts for unit testing
    |
    ├── environment.yml    <- Requirements file for reproducing the analysis environment using conda
    |                        (`conda create --name forest3d --file environment.yml`)
    ├── .gitignore         <- Stuff for git to ignore
    ├── .gitattributes     <- File types managed by Git LFS
    └── .travis.yml        <- Settings for running Travis CI
