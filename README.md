# MESA Stellar Modeling
This notebook shows how to extract information from a MESA code run. It is detailed and verbose (prints a lot of stuff out). It is based on a tutorial from University of Wisconson Astronomy.

The notebook requires (imports) the `mesa_web.py` module, which can be downloaded from [here](http://user.astro.wisc.edu/~townsend/resource/teaching/astro-310-F19/python-lab/mesa_web.py) (there is also a copy in this repo).  Put that module in the same directory as this notebook file. The mesa_web.py module was provided by the same group who developed MESA-Web, however, there should be no difference in the output from the installed version of MESA vs. MESA-Web.

For users of Conda, there is a .yml environment file that installs all dependencies.  Use is as follows in Conda:  
conda env create --name mesa --file=mesa.yml  
conda activate mesa  

If your Jupyter notebook does not show the mesa kernel, use conda (after shutting down the notebook with ^C):  
conda activate mesa (if not already in the environment)  
python -m ipykernel install --user --name=mesa --display-name="Mesa Kernel"  

Restart jupyter and you should see "Mesa Kerne" as a choice under Kernel > Change Kernel . . .   
