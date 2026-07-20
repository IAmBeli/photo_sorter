# Photo Sorter

A command-line tool that organizes photos into folders by their **content**,
using OpenAI's CLIP model. It scans a source folder, classifies each image into
a category (food, nature, people, vehicles, and more), and copies the photos into
per-category folders — without touching the originals.

## Features

- Scans a folder and detects image files (`.jpg`, `.jpeg`, `.png`)
- Classifies each photo by content using a pretrained CLIP model
- Sorts photos into per-category folders
- Copies files (originals are never moved or modified)
- Shows progress while processing (`[3/8] photo.jpg -> nature`)
- Categories are easy to customize in the code

## Tech

- Python 3
- PyTorch + OpenAI CLIP (content classification)
- Pillow (image reading)

## Installation

This project needs a few libraries. Install them with pip:

```bash
pip3 install torch pillow ftfy regex tqdm
pip3 install git+https://github.com/openai/CLIP.git
```

## Usage

```bash
git clone https://github.com/IAmBeli/photo_sorter.git
cd photo_sorter
python3 main.py
```

When prompted, enter the full path to the folder containing your photos:

```
Enter path to photos folder:
```

On the first run, the CLIP model (~340 MB) is downloaded automatically and cached
for later runs. Sorted copies are written to a `sorted/` folder next to the script,
organized by category.

## Customizing categories

The categories live in one line in `main.py`:

```python
categories = ["plate of food", "nature", "architecture",
              "group of people", "vehicles", "clothes", "drinks"]
```

Edit this list to match your own photos. Short descriptive phrases
(e.g. `"plate of food"` instead of just `"food"`) tend to classify more accurately.

## Roadmap

- Detect duplicate and blurry photos
- Optional sorting by date (from photo metadata)