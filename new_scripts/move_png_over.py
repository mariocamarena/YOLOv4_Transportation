import shutil
import glob
import os
from tqdm import tqdm

# specify source and destination directories
source_dir = 'C:/Users/Mario/OneDrive/Desktop/YOLOv4-PyTorch-Transportation/datasets_3/gtFine/val'
dest_dir = 'C:/Users/Mario/OneDrive/Desktop/YOLOv4-PyTorch-Transportation/data/custom/val_images'

# Create the destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# find all .png files in the source directory and its subdirectories that end with "_gtFine_color"
png_files = glob.glob(source_dir + '/**/*_gtFine_color.png', recursive=True)

print(f"Found {len(png_files)} files to copy.")

# copy each file to the destination directory
for file in tqdm(png_files, desc="Copying files", unit="file"):
    print(f"Copying file {file} to {dest_dir}")
    shutil.copy(file, dest_dir)

print("All .png files ending with '_gtFine_color' have been copied successfully.")