import os
import shutil
import random

random.seed(42)

dataset_dir = 'dataset'
images_dir = os.path.join(dataset_dir, 'images')
labels_dir = os.path.join(dataset_dir, 'labels')
classes_file = os.path.join(dataset_dir, 'classes.txt')
notes_file = os.path.join(dataset_dir, 'notes.json')

splits = ['train', 'test']
split_ratio = 0.8  

for split in splits:
    os.makedirs(f'dataset_split/{split}/images', exist_ok=True)
    os.makedirs(f'dataset_split/{split}/labels', exist_ok=True)

image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
random.shuffle(image_files)

total = len(image_files)
train_end = int(split_ratio * total)

split_data = {
    'train': image_files[:train_end],
    'test': image_files[train_end:]
}

for split, files in split_data.items():
    for img_file in files:
        label_file = img_file.replace('.jpg', '.txt')

        src_img_path = os.path.join(images_dir, img_file)
        dst_img_path = os.path.join(f'dataset_split/{split}/images', img_file)
        shutil.copyfile(src_img_path, dst_img_path)

        src_label_path = os.path.join(labels_dir, label_file)
        dst_label_path = os.path.join(f'dataset_split/{split}/labels', label_file)
        if os.path.exists(src_label_path):
            shutil.copyfile(src_label_path, dst_label_path)

shutil.copyfile(classes_file, 'dataset_split/classes.txt')
shutil.copyfile(notes_file, 'dataset_split/notes.json')

print("Dataset successfully split into train and test sets.")
