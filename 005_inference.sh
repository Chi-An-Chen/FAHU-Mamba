#!/bin/bash

# Set dataset's ID
DATASET_ID="002"

# 設定其他訓練參數
MODALITY="2d" # 3d_fullres for 3D images, 2d for 2D images
FOLDS="all"
TRAINER="nnUNetTrainerSwinUMambaDScratch"

INPUT_FOLDER="/home/msp/data/nnUNet_raw/Dataset002_BreastDM_v2/imagesTs"
OUTPUT_FOLDER="/home/msp/data/nnUNet_results/Dataset002_BreastDM_v2/nnUNetTrainerSwinUMambaDScratch__nnUNetPlans__2d/inference"

# 執行訓練指令
echo "Starting inference with dataset ID: $DATASET_ID"
echo "Input folder: $INPUT_FOLDER"
echo "Output folder: $OUTPUT_FOLDER"

nnUNetv2_predict -i $INPUT_FOLDER -o $OUTPUT_FOLDER -d $DATASET_ID -c $MODALITY -tr $TRAINER -f $FOLDS --disable_tta
# nnUNetv2_predict -i INPUT_FOLDER -o OUTPUT_FOLDER -d DATASET_ID -c 2d -tr nnUNetTrainerLightMUNet --disable_tta