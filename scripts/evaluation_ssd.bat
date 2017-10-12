set DATASET_DIR=C:/Projects/Medical_image/Endoscopic/DATA_edit/data1010
set TRAIN_DIR=./logs/ssd_300_vgg_medical
set EVAL_DIR=%TRAIN_DIR%/eval
python eval_ssd_network.py ^
    --eval_dir=%EVAL_DIR% ^
    --dataset_dir=%DATASET_DIR% ^
    --dataset_name=medical ^
    --dataset_split_name=validation ^
    --model_name=ssd_300_vgg ^
    --checkpoint_path=%TRAIN_DIR% ^
    --wait_for_checkpoints=True ^
    --batch_size=1