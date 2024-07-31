#!/bin/bash

NUM_CLASSES=$1

echo "# parameters
number_classes: ${NUM_CLASSES}  # number of classes
depth_multiple: 1.0  # model depth multiple
width_multiple: 1.0  # layer channel multiple

# anchors
anchors:
  - [10,13, 16,30, 33,23]  # P3/8
  - [30,61, 62,45, 59,119]  # P4/16
  - [116,90, 156,198, 373,326]  # P5/32

# Darknet-53 backbone
backbone:
  # [from, number, module, args]
  [[-1, 1, Conv, [32, 3, 1]],  # 0
   [-1, 1, Conv, [64, 3, 2]],  # 1-P1/2
   [-1, 1, Bottleneck, [64]],
   [-1, 1, Conv, [128, 3, 2]],  # 3-P2/4
   [-1, 2, Bottleneck, [128]],
   [-1, 1, Conv, [256, 3, 2]],  # 5-P3/8
   [-1, 8, Bottleneck, [256]],
   [-1, 1, Conv, [512, 3, 2]],  # 7-P4/16
   [-1, 8, Bottleneck, [512]],
   [-1, 1, Conv, [1024, 3, 2]], # 9-P5/32
   [-1, 4, Bottleneck, [1024]],  # 10
  ]

# YOLOv3 head
head:
  [[-1, 3, Bottleneck, [1024, False]],  # 11

   [-1, 1, Conv, [256, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, \"nearest\"]],
   [[-1, 8], 1, Concat, [1]],  # concat backbone P4
   [-1, 1, Bottleneck, [512, False]],
   [-1, 2, Bottleneck, [512, False]],  # 16

   [-1, 1, Conv, [128, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, \"nearest\"]],
   [[-1, 6], 1, Concat, [1]],  # concat backbone P3
   [-1, 1, Bottleneck, [256, False]],
   [-1, 2, Bottleneck, [256, False]],  # 21

   [[21, 16, 11], 1, Detect, [number_classes, anchors]],   # Detect(P3, P4, P5)
  ]
" >> yolov4-custom.yaml