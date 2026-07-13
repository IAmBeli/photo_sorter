import os
import shutil

source_folder = input("Enter path to photos folder: ")
output_folder = "sorted"

files = os.listdir(source_folder)
images = []
for f in files:
    if f.lower().endswith((".jpg", ".jpeg", ".png")):
        images.append(f)
for name in images:
    parts = name.split(" ")
    if len(parts) >= 2:
        date = parts[1]
    else:
        date = "no date"
    src = os.path.join(source_folder, name)
    dst_folder = os.path.join(output_folder, date)
    os.makedirs(dst_folder, exist_ok=True)
    shutil.copy(src, dst_folder)
    print(name, "->", date)