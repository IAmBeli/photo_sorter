import os
import shutil
import torch
import clip
from PIL import Image

def classify_photo(path, model, preprocess, categories, device):
    image = preprocess(Image.open(path)).unsqueeze(0).to(device)
    text = clip.tokenize(categories).to(device)
    with torch.no_grad():
        logits_per_image, logits_per_text = model(image, text)
        probs = logits_per_image.softmax(dim=-1)
    best_index = probs.argmax().item()
    return categories[best_index]

device = "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)
categories = ["food", "nature", "architecture", "people"]

source_folder = input("Enter path to photos folder: ")
output_folder = "sorted"
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

files = os.listdir(source_folder)
images = []
for f in files:
    if f.lower().endswith((".jpg", ".jpeg", ".png")):
        images.append(f)
for name in images:
    path = os.path.join(source_folder, name)
    category = classify_photo(path, model, preprocess, categories, device)
    dst_folder = os.path.join(output_folder, category)
    os.makedirs(dst_folder, exist_ok=True)
    shutil.copy(path, dst_folder)
    print(name, "->", category)