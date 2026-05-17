from ultralytics import YOLO

model = YOLO("runs/detect/train-9/weights/best.pt")

results = model.predict(
    source=input("Enter image name: "),
    save=True,
    conf=0.1
)

print("Done")