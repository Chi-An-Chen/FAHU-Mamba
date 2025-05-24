# MSU-Net : A State Space-Inspired U-Net with Linear Attention for Breast Tumor Image Segmentation  
<div align="center">

  [[`Paper`](assets/AIxMHC2025_TumorSeg_Sean.pdf)]
  
  This is the official PyTorch implementation of SSIU-Net: a State Space-Inspired U-Net that integrates a State Space Model (SSM) with a Mamba-Inspired Linear Attention Block (MILA) for breast tumor image segmentation.  

</div>

## Environments  
The following operations are all performed in a Linux environment.  

```
conda env create -f environment.yaml
conda activate ssiunet 
```
```
cd SSIU-Net-main
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

