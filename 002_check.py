import os
import numpy as np
from PIL import Image

"""
確認 label 符合 dataset.json 中的設定 [0,1]
"labels": {
        "background": 0,
        "tumor ": 1
    }
"""
# 設定資料集的標註資料夾路徑
dst_root = "/home/msp/data/nnUNet_raw/Dataset002_BreastDM_8_2"  # 替換為你的 labelsTr 資料夾路徑
min_label = float('inf')
max_label = float('-inf')

# 瀏覽資料夾中的所有檔案
for subdir in ["labelsTr", "labelsTs"]:
    labels_folder = dst_root + '/' + subdir
    for label_file in os.listdir(labels_folder):
        if label_file.endswith(".png"):
            # 載入標註圖像
            label_path = os.path.join(labels_folder, label_file)
            label_img = Image.open(label_path)
            label_data = np.array(label_img)

            # 更新全域最小最大值
            min_label = min(min_label, label_data.min())
            max_label = max(max_label, label_data.max())

            # 檢查標註類別
            unique_labels = np.unique(label_data)
            if np.any(unique_labels < 0) or np.any(unique_labels > 1):
                print(f"警告: 檔案 {label_file} 包含意外的標註類別！")
            
    print(f"{labels_folder} 類別範圍: [{min_label}, {max_label}]")

# 印出總體範圍
print("所有檔案檢查完成")
