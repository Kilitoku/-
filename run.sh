#!/usr/bin/env bash

export CUDA_VISIBLE_DEVICES=1
export PYTHONWARNINGS="ignore"
#train
python tools/train.py projects/CO-DETR/configs/codino/co_dino_5scale_swin_l_16xb1_3x_coco.py  \
--work-dir ./work_dirs/co_dino_5scale_swin_l_16xb1_3x_coco  \
