import os
import shutil
from pathlib import Path
from PIL import Image
import numpy as np
from tqdm import tqdm
import random

def convert_label_to_01(src_path, dst_path):
    label_img = Image.open(src_path).convert("L")
    label_data = np.array(label_img)
    label_data[label_data == 255] = 1
    label_img_fixed = Image.fromarray(label_data.astype(np.uint8))
    label_img_fixed.save(dst_path)

def collect_all_image_label_pairs(base_dir):
    """
    收集 train, val, test 中所有的 image/label 路徑對。
    """
    all_pairs = []
    for phase in ["train", "val", "test"]:
        image_dir = base_dir / phase / "images"
        label_dir = base_dir / phase / "labels"
        for image_file in sorted(os.listdir(image_dir)):
            label_file = image_file  # 預設影像與標註檔名相同
            all_pairs.append((image_dir / image_file, label_dir / label_file))
    return all_pairs

def split_and_copy(pairs, dst_root, train_ratio=0.8):
    random.shuffle(pairs)
    split_idx = int(len(pairs) * train_ratio)
    train_pairs = pairs[:split_idx]
    test_pairs = pairs[split_idx:]

    for i, (img_path, lbl_path) in enumerate(tqdm(train_pairs, desc="Copying Training Data")):
        case_id = f"case_{i:04d}"
        img_dst = dst_root / "imagesTr" / f"{case_id}_0000.png" # _0000.png 是 nnUNet 的要求。由於沒有要在分割同時進行辨識良、惡性所以統一設為0 https://blog.csdn.net/m0_68239345/article/details/128886376
        lbl_dst = dst_root / "labelsTr" / f"{case_id}.png"
        Image.open(img_path).convert("RGB").save(img_dst)
        convert_label_to_01(lbl_path, lbl_dst)

    for i, (img_path, lbl_path) in enumerate(tqdm(test_pairs, desc="Copying Testing Data")):
        case_id = f"case_{i:04d}"
        img_dst = dst_root / "imagesTs" / f"{case_id}_0000.png"
        lbl_dst = dst_root / "labelsTs" / f"{case_id}.png"
        Image.open(img_path).convert("RGB").save(img_dst)
        convert_label_to_01(lbl_path, lbl_dst)

if __name__ == "__main__":
    src_root = Path("/home/msp/data/BreastDM")
    """
    dataset/
    ├── train
    │   ├── images
    │   └── labels
    ├── test
    │   ├── images
    │   └── labels
    └── val
        ├── images
        └── labels
    """
    dst_root = Path("/home/msp/data/nnUNet_raw/Dataset002_BreastDM_v2")
    """
    dataset/
    ├── imagesTr
    ├── labelsTr
    ├── imagesTs
    └── labelsTs
    """

    # 建立目標資料夾
    for sub in ["imagesTr", "labelsTr", "imagesTs", "labelsTs"]:
        (dst_root / sub).mkdir(parents=True, exist_ok=True)

    # 收集並分割資料
    all_pairs = collect_all_image_label_pairs(src_root)
    split_and_copy(all_pairs, dst_root, train_ratio=0.8)

    # 統計資料夾檔案數量
    print("\n資料夾中檔案數量統計 : ")
    train_num = 0
    test_num=0
    for subdir in ["imagesTr", "labelsTr", "imagesTs", "labelsTs"]:
        if subdir == "imagesTr":
            folder = dst_root / subdir
            count = len(list(folder.glob("*.png")))
            train_num = count
        if subdir == "imagesTs":
            folder = dst_root / subdir
            count = len(list(folder.glob("*.png")))
            test_num = count
        else:
            folder = dst_root / subdir
            count = len(list(folder.glob("*")))
        print(f"{subdir:<10}: {count} 個檔案")

    print(f"train_num: {train_num}")
    print(f"test_num: {test_num}")
    print(f"train_num + test_num: {train_num + test_num}")
    print(f"Train / Test Ratio: {train_num / (train_num + test_num):.2f} / {test_num / (train_num + test_num):.2f}")
    

    print("\n全部完成 !")
