# MSU-Net : A Mamba-Spectral Hybrid U-Net for Breast Tumor Segmentation
<div align="center">

  [[`Paper`](assets/AIxMHC2025_SwinUMamba.pdf)]
  
  This is the official PyTorch implementation of MSU-Net : A Mamba-Spectral Hybrid U-Net (MSU-Net) architecture that combines a State Space Model (SSM) and spectral domain feature representations within a U-Net convolutional network, designed for tumor segmentation in breast DCE-MRI images.

</div>

## Environments  
The following operations are all performed in a Linux environment.  

```
conda env create -f environment.yaml
conda activate msunet 
```
```
cd MSU-Net-main
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

