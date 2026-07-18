import torch
import clip
from PIL import Image

device = "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)
categories = ["food", "nature", "architecture", "people"]
image = preprocess(Image.open("/Users/bagachukilia/Projectsss/photosorter/sorted/2026-07-13/IMAGE 2026-07-13 21:57:53.jpg")).unsqueeze(0).to(device)
text = clip.tokenize(categories).to(device)

with torch.no_grad():
    logits_per_image, logits_per_text = model(image, text)
    probs = logits_per_image.softmax(dim=-1)

print(probs)
best_index = probs.argmax().item()
best_category = categories[best_index]
print("That's: ", best_category)