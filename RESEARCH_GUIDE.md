# From the FAHU-Mamba paper to a segmentation run

The [AIxMHC 2025 paper](https://doi.org/10.1109/AIxMHC65380.2025.00056) is the reference for the published method and results. The shell scripts below describe the configuration shipped in this repository.

## Inputs and working directory

Start in the repository root. Provide the nnU-Net dataset with training images and labels, test images, and `dataset.json`. Read [paths.py](nnunetv2/paths.py) before choosing locations: this checkout derives its raw, preprocessed, and results directories from its own base path. The inference and evaluation launchers also contain machine-specific paths. Keep all of them pointed at the same dataset and trained model.

| Stage | Entry | Inputs and outputs |
|---|---|---|
| Prepare | [003_data.sh](003_data.sh) | Dataset ID `002` → integrity check and preprocessed data. |
| Train | [004_run.sh](004_run.sh) | Preprocessed data → trained weights using `nnUNetTrainerSwinUMambaDScratch`, `2d`, and fold `all` in this checkout. |
| Predict | [005_inference.sh](005_inference.sh) | Trained weights and `imagesTs` → predicted masks under `OUTPUT_FOLDER`. The launcher disables test-time augmentation. |
| Evaluate | [006_evaluated.sh](006_evaluated.sh) | Matching `labelsTs`, predicted masks, `dataset.json`, and model `plans.json` → `summary.json`. Set the prediction path to the output of the preceding step. |

Keep the dataset identity, case split, trainer, fold, and prediction settings with any reported score. Running the shipped example on a different dataset or split yields a separate experiment.
