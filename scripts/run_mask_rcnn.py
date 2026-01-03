import torch
from torchvision import transforms
from torchvision.models.detection import maskrcnn_resnet50_fpn
from PIL import Image

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load pre-trained Mask R-CNN
model = maskrcnn_resnet50_fpn(weights="DEFAULT")
model.eval()
model.to(device)

# Load image
image = Image.open("images/street.jpg").convert("RGB")

# Transform
transform = transforms.Compose([
    transforms.ToTensor()
])

img_tensor = transform(image).to(device)

# Run inference
with torch.no_grad():
    outputs = model([img_tensor])

out = outputs[0]

print("Keys in output:", out.keys())
print("Number of detections:", len(out["boxes"]))

# Inspect first few detections
for i in range(min(3, len(out["boxes"]))):
    box = out["boxes"][i].tolist()
    label = int(out["labels"][i])
    score = float(out["scores"][i])
    mask_pixels = int(out["masks"][i].sum().item())

    print(f"\nDetection {i}")
    print("  Label:", label)
    print("  Score:", round(score, 3))
    print("  Box:", [round(x, 1) for x in box])
    print("  Mask on-pixels:", mask_pixels)