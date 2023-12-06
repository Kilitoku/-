#!/bin/bash
cd /home/mmdetection/data/coco/test_labels/;
python txt.py;
cd /home/mmdetection/data/coco/annotations/;
python txt-json.py;
cd /home/mmdetection/;
CUDA_VISIBLE_DEVICES=2 python tools/test.py work_dirs/co_dino_5scale_swin_l_lsj_16xb1_3x_coco/co_dino_5scale_swin_l_lsj_16xb1_3x_coco.py work_dirs/co_dino_5scale_swin_l_lsj_16xb1_3x_coco/epoch_36.pth --tta;
cd /home/mmdetection/data/coco/annotations/;
python js-js.py;
python json-txt.py;
rm /home/mmdetection/work_dirs/bdc2310668/classes.txt;
