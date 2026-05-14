from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolov8n.pt")

# Run prediction
results = model("test.png", save=True)

print("Detection Completed")