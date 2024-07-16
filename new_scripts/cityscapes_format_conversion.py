import json
import os
from tqdm import tqdm
'''
    convert function takes mask coordinate from cityscaoes JSON formats it to YOLOv4 compatiple
    * size of image and mask coordinates  as parameters
    * returns center cordinates, width, height, all normalized between 0 and 1
'''
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
'''
    *opens a JSON file
    *reads the data, and writes the annotations in the YOLOv4 format to a new .txt file.
    *convert function to convert the mask coordinates.
'''
def convert_annotation(json_file, classes, output_dir):
    try:
        with open(json_file) as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Could not do {json_file}. Skipping this file. CHECK ERROR TYPE")
        return


    img_w = data['imgWidth']
    img_h = data['imgHeight']
    objects = data['objects']

    relative_path = os.path.relpath(json_file, root_dir)
    txt_outfile = os.path.join(output_dir, relative_path.replace(".json", ".txt"))
    os.makedirs(os.path.dirname(txt_outfile), exist_ok=True)

    with open(txt_outfile, "w") as out_file:
        for obj in objects:
            cls_id = classes.index(obj['label'])

            points = obj['polygon']
            xmin = min(point[0] for point in points)
            xmax = max(point[0] for point in points)
            ymin = min(point[1] for point in points)
            ymax = max(point[1] for point in points)

            b = (float(xmin), float(xmax), float(ymin), float(ymax))
            bb = convert((img_w, img_h), b)

            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    print(f"Converted {json_file} to {txt_outfile}")

'''
cityscapes = 30 classes split into 13 groups
YOLOv4  trained on COCO == 80 object classes
'''



'''
classes = ["road", "sidewalk", "parking"," rail track", 
          "person", "rider",
          "car","truck","bus", "on rails","motorcycle", "bicycle", "caravan","trailer",
          "building","wall","fence","guard rail","bridge","tunnel",
            "pole","pole group","traffic sign","traffic light",
            "vegetation","terrain",
            "sky",
            "ground","dynamic","static"]
'''
classes = [
    "unlabeled",
    "ego vehicle",
    "rectification border",
    "out of roi",
    "static",
    "dynamic",
    "ground",
    "road",
    "sidewalk",
    "parking",
    "rail track",
    "building",
    "wall",
    "fence",
    "guard rail",
    "bridge",
    "tunnel",
    "pole",
    "polegroup",
    "traffic light",
    "traffic sign",
    "vegetation",
    "terrain",
    "sky",
    "person",
    "rider",
    "car",
    "truck",
    "bus",
    "car",
    "trailer",
    "train",
    "motorcycle",
    "bicycle",
    "license plate"
]



root_dir = "C:/Users/Mario/OneDrive/Desktop/yolov4/pytorch-YOLOv4-Transportation/datasets/gtFine"
output_dir = "C:/Users/Mario/OneDrive/Desktop/yolov4/pytorch-YOLOv4-Transportation/datasets/CS_annotations"

for dir_name in ['train', 'val', 'test']:
    dir_path = os.path.join(root_dir, dir_name)
    json_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))

    for json_file in tqdm(json_files, desc=f"Converting {dir_name}"):
        convert_annotation(json_file, classes, output_dir)
