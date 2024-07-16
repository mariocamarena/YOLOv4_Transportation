import os
import glob
from tqdm import tqdm

# specify source directory and train.txt directory
source_dir = 'C:/Users/Mario/OneDrive/Desktop/yolov4/pytorch-YOLOv4-master/data/custom/images/'
train_txt_dir = 'C:/Users/Mario/OneDrive/Desktop/yolov4/pytorch-YOLOv4-master/data/custom/'

# find all .png files in the source directory
png_files = glob.glob(source_dir + '/*.png')

# open the train.txt file in write mode
with open(os.path.join(train_txt_dir, 'train.txt'), 'w') as f:
    # write each file path to the train.txt file
    for file_path in tqdm(png_files, desc="Processing files", unit="file"):
        # get the base name of the file
        base_name = os.path.basename(file_path)
        # construct the new file path
        new_path = f'data/custom/images/{base_name}'
        # write the new file path to the file
        f.write(new_path + '\n')

print("All .png file paths have been written to train.txt successfully.")


