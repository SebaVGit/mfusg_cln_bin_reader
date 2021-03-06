# MODFLOW-USG CLN Binary Reader
This is a python script that reads CLN´s binary files and It uses Flopy and Pandas.
## Required packages
**flopy version:** `3.2 or later`\
You can search more information about it [here](https://flopy.readthedocs.io/en/3.3.2/)\
You can install it by using **Conda**: `conda install -c conda-forge flopy`\
or by using **pip**: `pip install flopy`.
## Example
I used MODFLOW-USG packages created with Groundwater Vistas 7.\
Here you can download a student version of the software: [GWV](http://www.groundwatermodels.com/)\
Also you have the entire project of GWV in the `MODFLOW_Files`. It is a simple model that runs flow and transport in order to create 3 binary files.\
You can find the MODLOFW-USG with Transport executable [here](https://www.gsi-net.com/en/software/free-software/modflow-usg.html)

## Capabilities
You can read head, cell by cell and concentration files of the CLN.\
Here you will find in the `Bin_Reader_Example` file 3 binary data to test the script and its output wich is a **.csv** file.
## Running test
You can run the script in windows by using the batch file `Executable.bat`\
and then change it as you like:
```bash
@echo on
call activate base
python ..\Read_Binary_CLN_v1_git.py
pause
```
I use `call activate base` in order to activate the conda environment where I have installed flopy.\
Finally you can run the script with your favorite text editor like VSCode or Spyder if you like.

## Contact

If you want to improve the code, please feel free to contact me or just make a pull request.\
email: `sebastian.vazquez@ug.uchile.cl`\
[Linkedin](https://www.linkedin.com/in/sebasti%C3%A1n-v%C3%A1zquez-gasty-952121181/)
