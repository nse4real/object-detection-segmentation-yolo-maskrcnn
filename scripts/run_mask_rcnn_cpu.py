import time
import torch
from torchvision import transforms
from torchvision.models.detection import maskrcnn_resnet50_fpn
from PIL import Image

t0 = time.time()
print("Loading model...")

device = "cpu"
model = maskrcnn_resnet50_fpn(weights="DEFAULT")
model.eval().to(device)

print("Loading image...")
image = Image.open("images/street.jpg").convert("RGB")

img = transforms.Compose([
    transforms.Resize((320, 240)),
    transforms.ToTensor()
])(image).to(device)

print("Running inference (CPU)... this can take a bit.")
with torch.no_grad():
    out = model([img])[0]

print("Done.")
print("Elapsed seconds:", round(time.time() - t0, 2))
print("Output keys:", list(out.keys()))
print("Detections:", len(out["boxes"]))

for i in range(min(3, len(out["boxes"]))):
    box = out["boxes"][i].tolist()
    label = int(out["labels"][i])
    score = float(out["scores"][i])
    mask_on = int(out["masks"][i].sum().item())
    print(f"\n{i}: label={label}, score={score:.3f}, box={[round(x,1) for x in box]}, mask_pixels={mask_on}")