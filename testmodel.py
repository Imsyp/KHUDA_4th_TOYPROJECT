import ultralytics
from ultralytics import YOLO

model = YOLO('/data/tkddud386/repos/best.pt')

model.predict('/data/tkddud386/repos/test2.jpg', save=True)

