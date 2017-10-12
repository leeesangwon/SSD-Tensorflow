set DATASET_DIR=C:/Projects/Medical_image/Endoscopic/DATA_edit/data1010
set TRAIN_DIR=./logs/ssd_300_vgg_medical
set CHECKPOINT_PATH=./checkpoints/ssd_300_vgg.ckpt
python train_ssd_network.py ^
    --train_dir=%TRAIN_DIR% ^
    --dataset_dir=%DATASET_DIR% ^
    --dataset_name=medical ^
    --dataset_split_name=train ^
    --model_name=ssd_300_vgg ^
    --checkpoint_path=%CHECKPOINT_PATH% ^
    --save_summaries_secs=60 ^
    --save_interval_secs=600 ^
    --weight_decay=0.0005 ^
    --optimizer=adam ^
    --learning_rate=0.001 ^
    --batch_size=32 ^
    --max_number_of_steps=1000