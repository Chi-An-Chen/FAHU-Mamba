import os
from PIL import Image
import numpy as np
from tqdm import tqdm

# def binarize_and_force_save_01(folder_path):
#     file_list = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]

#     for filename in tqdm(file_list, desc="Saving images with values 0 and 1"):
#         image_path = os.path.join(folder_path, filename)
#         image = Image.open(image_path).convert('L')
#         image_np = np.array(image)

#         # 二值化處理：0 或 1
#         binarized = (image_np >= 128).astype(np.uint8)

#         # 強制儲存為 0 和 1 的圖像（實際上會非常暗）
#         binarized_img = Image.fromarray(binarized, mode='L')
#         binarized_img.save(image_path)

# # 使用範例
# folder_path = '/home/msp/data/nnUNet_raw/Dataset001_BreastDM/labelsTr'
# binarized_imgs = binarize_and_force_save_01(folder_path)

# # 印出其中一張圖片的 array 結果
# for name, array in binarized_imgs.items():
#     print(f"{name}:")
#     print(array)
#     print(array.min(), array.max())
#     break  # 只印第一張
