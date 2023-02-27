![Heavy Division](https://github.com/Heavy-Division/branding/blob/main/src/svg/Logo%20Dark.svg#gh-dark-mode-only)
![Heavy Division](https://github.com/Heavy-Division/branding/blob/main/src/svg/Logo%20Light.svg#gh-light-mode-only)
# Livery Generator 

Script for creating B78XH soft fork compatible liveries from Asobo default 787 ones.

# Instructions 

This script can be run from the source code or via the downloadable executable.

### Running from Source:

You will need to have [Python](https://www.python.org) installed on your machine to run the source code.

Download the source code as a `zip` file and extract it. Run the script by running the following command in the terminal:

`python3 livery_generator/main.py --clone single --dir <path to livery>` replacing the <path to livery> 
with the relative or absolute path of the livery.

### generate multiple liveries 

Group all of your Default B787 liveries into one directory, and run 

`python3 livery_generator/main.py --clone multi --dir <path to liveries directory>` 
and the script will create b78xh liveries from all liveries in the directory.

The new Heavy Division 787 livery will be present in the same directory 
as the original livery, with a '_heavy_division_b78xh' suffix.

### Running the executable 
Download the .exe from the releases tab. Open the `command prompt` and run

`<path to exe> `