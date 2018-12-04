# Getting Started

## Option A: For the non-coder
If you don't want to do any coding yourself and instead just want to view and execute the code we've already written using our Jupyter Notebooks, use this link:  [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/d-diaz/Lidar_Plot_Registration/master) and a computing environment will be set up for you in the cloud (for free). This setup process can take several minutes, so be patient. Once that setup is done, you should be able to navigate to the "notebooks" folder of the repository and open and execute the Jupyter Notebooks without having to install anything on your own machine.

## Option B: For the coder
This Git repo utilizes the Git Large File Storage (LFS) system. Git LFS is used here to replace large files files (identified in `.gitattributes`) such as shapefiles, point clouds, and rasters with text pointers inside Git, while still storing files not excluded by `.gitignore` on GitHub. Very large geospatial data files such as point clouds (.las, .las) and rasters (.asc, .tif) are currently set up to be ignored by Git entirely because they can easily exceed GitHub storage allowances. Third party solutions for storing and sharing large datasets are used to work around this.

Use the conda package manager to reproduce the computing environment we used in developing this repo. Get [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html) to do so.

1. Install [Git LFS](https://github.com/git-lfs/git-lfs/wiki/Installation)
2. Clone this repo onto your local machine:  
`git clone https://github.com/d-diaz/Lidar_Plot_Registration.git`
3. Create a conda environment from the environment.yml file included in this repo:  
`conda env create --name viz3d --file environment.yml`
4. Activate this new conda environment:
`source activate viz3d` (Linux, OSX) or `activate viz3d` (Windows)
5. Start a Jupyter session:
`jupyter notebook`
6. In your web browser Jupyter session, navigate to the "notebooks" folder in this repo and open up one of the Jupyter Notebooks!
