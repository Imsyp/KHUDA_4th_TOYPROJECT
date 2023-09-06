from ultralytics import YOLO
import os
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(torch.cuda.is_available())

PATH = '/data/tkddud386/repos/datasets2'

model = YOLO('yolov8n.pt')
model.train(data=PATH + '/data.yaml', epochs=500,
            patience=10, batch=64, imgsz=608, device=device)

print(len(model.names), model.names)