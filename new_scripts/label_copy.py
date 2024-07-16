import os
import shutil
from tqdm import tqdm

# specify the source directory you want to scan
source_directory = 'C:/Users/Mario/OneDrive/Desktop/yolov4/pytorch-YOLOv4-Transportation/datasets_3/CS_annotations/train/'

# specify the destination directory where you want to copy the files
destination_directory = 'C:/Users/Mario/OneDrive/Desktop/yolov4/pytorch-YOLOv4-master/data/custom/labels/'

# get a list of all files in the source directory
files = os.listdir(source_directory)

# iterate over all files in the source directory with a progress bar
for filename in tqdm(files, desc="Processing files"):
    # check if the file is a .png and contains '_gtFine_color' in its name
    if filename.endswith('_gtFine_color.png'):
        # construct the paths to the .png file and the corresponding .txt files
        png_path = os.path.join(source_directory, filename)
        txt_path = os.path.join(source_directory, filename.replace('_gtFine_color.png', '_gtFine_polygons.txt'))
        new_txt_path = os.path.join(destination_directory, filename.replace('.png', '.txt'))

        # check if the corresponding .txt file exists
        if os.path.exists(txt_path):
            # copy the contents of the .txt file to a new .txt file with the same name as the .png file
            shutil.copyfile(txt_path, new_txt_path)
        else:
            print(f'\nNo corresponding .txt file found for {png_path}')
