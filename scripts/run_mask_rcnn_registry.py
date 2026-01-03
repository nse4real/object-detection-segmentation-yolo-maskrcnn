import torch
from torchvision import transforms
from torchvision.models.detection import get_model
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

# Version-safe: load by name via registry
model = get_model("maskrcnn_resnet50_fpn", weights="DEFAULT")
model.eval().to(device)

# Make it lighter: reduce proposals
model.rpn.pre_nms_top_n_test = 120
model.rpn.post_nms_top_n_test = 60

# Smaller input
image = Image.open("images/street.jpg").convert("RGB")
img = transforms.Compose([
    transforms.Resize((320, 240)),  # smaller again
    transforms.ToTensor()
])(image).to(device)

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