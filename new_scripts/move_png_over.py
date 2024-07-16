
import shutil
import glob
from tqdm import tqdm

# specify source and destination directories
source_dir = 'C:/Users/Mario/OneDrive/Desktop/yolov4/pytorch-YOLOv4-Transportation/datasets_3/CS_annotations/train'
dest_dir = 'C:/Users/Mario/OneDrive/Desktop/yolov4/pytorch-YOLOv4-master/data/custom/images'

# find all .png files in the source directory
png_files = glob.glob(source_dir + '/*.png')

# copy each file to the destination directory
for file in tqdm(png_files, desc="Copying files", unit="file"):
    shutil.copy(file, dest_dir)

print("All .png files have been copied successfully.")
