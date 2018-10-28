[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/d-diaz/Lidar_Plot_Registration/master)

# forest3d
Methods for creating 3D visualizations of forest inventory plots and co-registering stem maps with lidar data.

As this project develops, it will support 3D volumetric representations of trees with the ability to incorporate uncertainty/error into field-based measurements and additional rendering parameters.

In addition to the basic value of providing a stochastic 3D visualization option for forest inventory plots, this workflow is intended to support an optimization to co-register lidar-derived data (e.g., canopy surface model or alpha-hulls of trees) with stem-mapped forest inventory data from the field. This is intended to improve the alignment of field data with remotely-sensed data to support the use of field data as training data for predictive models that rely primarily upon remotely-sensed data such as lidar and high-resolution imagery.

The incorporation of prior beliefs about the distributions of 3D forest parameters (e.g., measurement error in location of plot center, distance of trees from plot center, etc.) will be applied in a Bayesian Inverse Modeling approach to identify the values and distributions of parameters which minimize divergence between simulated forest surfaces and lidar-derived surface(s). The outcome of this optimization will include probabilistic insights about the most likely locations of forest inventory plots within a lidar scene.

# Getting Started
This Git repo utilizes the Git Large File Storage (LFS) system. Git LFS is used here to replace large files files (identified in `.gitattributes`) such as shapefiles, point clouds, and rasters with text pointers inside Git, while still storing files not excluded by `.gitignore` on GitHub. Very large geospatial data files such as point clouds (.las, .las) and rasters (.asc, .tif) are currently set up to be ignored by Git entirely because they can easily exceed GitHub storage allowances. Third party solutions for storing and sharing large datasets are used to work around this.

Use the conda package manager to reproduce the computing environment we used in developing this repo. Get [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html) to do so.

1. Install [Git LFS](https://github.com/git-lfs/git-lfs/wiki/Installation)
2. Clone this repo onto your local machine
3. Create a conda environment from the environment.yml file included in this repo:
`conda env create --name viz3d --file environment.yml`
4. Activate this environment to begin working.
`source activate viz3d` (Linux, OSX) or `activate viz3d` (Windows)

# Project Organization
(based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/))
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml   <- The requirements file for reproducing the analysis environment
    │
    ├── setup.py           <- makes project installable (`conda-develop .`) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------
