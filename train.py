from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(
    data="data.yaml",
    epochs=100,
    imgsz=640,
    device=0,
    workers=0
)