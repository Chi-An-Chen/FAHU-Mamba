# FAHU-Mamba : A Frequency-Aware Hybrid U-Mamba for Breast Tumor Segmentation

[Research guide: dataset paths, trainer, and evaluation](RESEARCH_GUIDE.md)
[Project page](https://chi-an-chen.github.io/FAHU-Mamba/) · [Paper](https://ieeexplore.ieee.org/document/11326816)

<div align="center">
  
  This is the official implementation of FAHU-Mamba : a frequency-aware hybrid U-Mamba (FAHU-Mamba) model architecture, which integrates a state space model (SSM) and a frequency-aware module (FAM) for breast tumor segmentation.  
  
</div>

## Environments  
Run these commands on Linux from the repository root, which contains `environment.yaml` and `setup.py`.  

```
conda env create -f environment.yaml
conda activate msunet 
```
```
pip install -e .
```
sanity test: Enter python command-line interface and run
```
import torch
import mamba_ssm
```

## Prepare dataset for Training and Testing 
Format your dataset in accordance with the nnU-Net format then run :   
```
bash 003_data.sh
```  

## Training
Set your dataset id and other config in 004_run.sh then run :  
```
bash 004_run.sh
```

## Inference 
Set your dataset id and other config in 005_inference.sh then run :  
``` 
bash 005_inference.sh
```

## Citation： 
```
@INPROCEEDINGS{11326816,
  author={Chen, Chi-An and Alessia Bosshart, Sara Katharina and Ke, Liang-Ying and Hsia, Chih-Hsien},
  booktitle={2025 Second International Conference on Artificial Intelligence for Medicine, Health and Care (AIxMHC)}, 
  title={A Frequency-Aware Hybrid U-Mamba for Breast Tumor Segmentation}, 
  year={2025},
  volume={},
  number={},
  pages={262-263},
  keywords={Measurement;Image segmentation;Breast tumors;Databases;Shape;Computational modeling;Resonant frequency;Predictive models;Planning;Medical diagnostic imaging;Computer vision;Image segmentation;State space models;Breast tumor},
  doi={10.1109/AIxMHC65380.2025.00056}}
```

