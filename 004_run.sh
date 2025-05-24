#!/bin/bash

# Set dataset's ID
DATASET_ID="002"

# 設定其他訓練參數
MODALITY="2d" # 3d_fullres for 3D images, 2d for 2D images
FOLDS="all"
TRAINER="nnUNetTrainerSwinUMambaDScratch" # nnUNetTrainerSwinUMambaDScratch  nnUNetTrainerLightMUNet

# 執行訓練指令
echo "Starting training with dataset ID: $DATASET_ID"
nnUNetv2_train $DATASET_ID $MODALITY $FOLDS -tr $TRAINER
# nnUNetv2_train DATASET_ID 2d all -tr nnUNetTrainerLightMUNet
