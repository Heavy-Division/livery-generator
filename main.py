import os
import shutil
import sys

# Check if the source directory path is provided as a command line argument
if len(sys.argv) < 2:
    print('Usage: python3 main.py <source_directory>')
    sys.exit(1)

# Get the source directory path from the command line argument
src_dir = sys.argv[1]

# Check if the source directory exists
if not os.path.exists(src_dir):
    print(f'The source directory "{src_dir}" does not exist.')
    sys.exit(1)

# Get the parent directory of the source directory
parent_dir = os.path.dirname(src_dir)

# Define the destination directory as a subdirectory of the parent directory with the same name as the source directory
dst_dir = os.path.join(parent_dir, os.path.basename(src_dir) + '_heavy_division')

# Check if the destination directory already exists
if os.path.exists(dst_dir):
    overwrite = input(f'The destination directory "{dst_dir}" already exists. Do you want to overwrite it? [y/n] ')
    if overwrite.lower() != 'y':
        print('Directory copy cancelled.')
        sys.exit(1)
    shutil.rmtree(dst_dir)

# Copy the contents of the source directory to the destination directory
shutil.copytree(src_dir, dst_dir)

# Traverse the copied directory and modify the base_container and interior lines in the aircraft.cfg and model.cfg files
for dirpath, dirnames, filenames in os.walk(dst_dir):
    for filename in filenames:
        if filename.lower() in ('aircraft.cfg', 'model.cfg', 'model.CFG'):
            cfg_file = os.path.join(dirpath, filename)
            with open(cfg_file, 'r') as f:
                lines = f.readlines()
            with open(cfg_file, 'w') as f:
                for line in lines:
                    if 'base_container' in line:
                        line = 'base_container = "..\Heavy-Division-B78XH-mod"\n'
                    elif 'interior' in line.lower():
                        line = line.replace('Asobo_B787_10', 'Heavy-Division-B78XH-mod').replace('.XML', '.xml')
                    f.write(line)

print('Directory copied and configuration files modified successfully!')