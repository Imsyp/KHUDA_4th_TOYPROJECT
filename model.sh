#!/bin/bash

#SBATCH --job-name=yolov8
#SBATCH --nodelist=moana-y6
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=32G
#SBATCH --time=1-0
#SBATCH --partition=batch_eebme_ugrad
#SBATCH -o slurm/logs/slurm-%A-%x.out

python model.py

# Letting SLURM know this code finished without any problem
exit 0