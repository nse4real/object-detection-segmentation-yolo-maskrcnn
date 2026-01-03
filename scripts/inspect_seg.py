from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")
results = model("images/street.jpg")

r = results[0]

print("Detections (post-NMS):", len(r.boxes))
print("Has masks:", r.masks is not None)

# Boxes
print("\nFirst 3 boxes:")
for i, box in enumerate(r.boxes[:3]):
    cls_id = int(box.cls.item())
    conf = float(box.conf.item())
    xyxy = box.xyxy.tolist()[0]
    print(f"  {i}: cls={cls_id}, conf={conf:.3f}, box={[round(x,1) for x in xyxy]}")

# Masks
if r.masks is not None:
    masks = r.masks.data  # (N, H, W) boolean-ish tensor
    print("\nMask tensor shape (N, H, W):", tuple(masks.shape))

    # How many pixels are "on" in the first few masks?
    for i in range(min(3, masks.shape[0])):
        on_pixels = int(masks[i].sum().item())
        print(f"  mask {i}: on_pixels={on_pixels}")