#!/bin/bash

# 設定 ground truth 資料夾（標註）
GT_FOLDER="/home/msp/data/nnUNet_raw/Dataset002_BreastDM_v2/labelsTs"

# 設定 model 預測結果資料夾
PRED_FOLDER="/home/msp/data/nnUNet_results/Dataset002_BreastDM_v2/nnUNetTrainerSwinUMambaDScratch__nnUNetPlans__2d/inference"

# 設定 dataset.json 路徑
DATASET_JSON="/home/msp/data/nnUNet_raw/Dataset002_BreastDM_v2/dataset.json"

# 設定 plans.json 路徑（對應你用的 trainer 與 fold）
PLANS_JSON="/home/msp/data/nnUNet_results/Dataset002_BreastDM_v2/nnUNetTrainerSwinUMambaDScratch__nnUNetPlans__2d/plans.json"

RESLUTS_JSON="/home/msp/data/nnUNet_results/Dataset002_BreastDM_v2/nnUNetTrainerSwinUMambaDScratch__nnUNetPlans__2d"

# 執行 nnUNet 評估
nnUNetv2_evaluate_folder $GT_FOLDER $PRED_FOLDER -djfile $DATASET_JSON -pfile $PLANS_JSON -o $RESLUTS_JSON/summary.json
echo "Evaluation completed. Results saved to $RESLUTS_JSON/summary.json"