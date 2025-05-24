import os
import numpy as np
from PIL import Image
from tqdm import tqdm  # 匯入tqdm

# 設定資料夾路徑
input_folder = '/Users/anguschen/Downloads/case'  # 修改為儲存inference結果的資料夾路徑
output_folder = '/Users/anguschen/Downloads/case_1'  # 修改為儲存結果圖片的資料夾路徑

# 如果output資料夾不存在，創建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 讀取資料夾中所有圖片，進行處理
filenames = [f for f in os.listdir(input_folder) if f.endswith('.png')]

# 使用tqdm顯示進度條
for filename in tqdm(filenames, desc="Processing images"):
    # 載入圖片
    img_path = os.path.join(input_folder, filename)
    img = Image.open(img_path).convert('L')  # 轉為灰階模式

    # 轉換為NumPy陣列並將[0, 1]轉為 [0, 255]
    img_array = np.array(img)
    img_array = (img_array * 255).astype(np.uint8)

    # 將1的部分變為紅色，黑色部分保持不變
    img_rgb = np.zeros((img_array.shape[0], img_array.shape[1], 3), dtype=np.uint8)
    img_rgb[img_array == 255] = [255, 255, 255]  # 將1的部分變為紅色
    img_rgb[img_array == 0] = [0, 0, 0]  # 黑色部分保持

    # 將處理過的圖片儲存到新的資料夾
    output_path = os.path.join(output_folder, filename)
    Image.fromarray(img_rgb).save(output_path)

print("處理完成，圖片已儲存至新的資料夾中。")