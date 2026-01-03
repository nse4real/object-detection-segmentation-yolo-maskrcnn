import torch
from torchvision import transforms
from torchvision.models.detection import maskrcnn_resnet50_fpn
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model
model = maskrcnn_resnet50_fpn(weights="DEFAULT")
model.eval().to(device)

# Reduce proposal counts (big VRAM saver)
model.rpn.pre_nms_top_n_test = 200
model.rpn.post_nms_top_n_test = 100

# Load + resize image (big VRAM saver)
image = Image.open("images/street.jpg").convert("RGB")
resize = transforms.Resize((480, 320))  # (H, W) smaller than 640x480
to_tensor = transforms.ToTensor()
img = to_tensor(resize(image)).to(device)

# Inference with mixed precision (VRAM saver)
with torch.no_grad():
    if device == "cuda":
        with torch.autocast(device_type="cuda", dtype=torch.float16):
            out = model([img])[0]
    else:
        out = model([img])[0]

print("Detections:", len(out["boxes"]))
print("Keys:", list(out.keys()))

for i in range(min(3, len(out["boxes"]))):
    box = out["boxes"][i].tolist()
    label = int(out["labels"][i])
    score = float(out["scores"][i])
    mask_on = int(out["masks"][i].sum().item())
    print(f"\n{i}: label={label}, score={score:.3f}, box={[round(x,1) for x in box]}, mask_on_pixels={mask_on}")