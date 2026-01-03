from ultralytics import YOLO

# Load pre-trained YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Run inference
results = model("images/street.jpg")

# There is one Results object per image
r = results[0]

print("Number of detections:", len(r.boxes))
print()

# Inspect first few detections
for i, box in enumerate(r.boxes[:5]):
    cls_id = int(box.cls.item())
    conf = float(box.conf.item())
    xyxy = box.xyxy.tolist()[0]

    print(f"Detection {i}")
    print("  Class ID:", cls_id)
    print("  Confidence:", round(conf, 3))
    print("  Box [x1, y1, x2, y2]:", [round(x, 1) for x in xyxy])
    print()