#!/bin/bash

# 設定資料集的 ID
DATASET_ID=002

# 執行預處理命令，並加上資料集完整性檢查
echo "Starting preprocess data with dataset ID: $DATASET_ID"
nnUNetv2_plan_and_preprocess -d $DATASET_ID --verify_dataset_integrity
