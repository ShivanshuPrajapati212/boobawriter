from PIL import Image
import os

input_folder = "shivanshu-handwriting"
output_folder = "bw_images"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        img = Image.open(os.path.join(input_folder, filename))
        bw = img.convert("L")
        bw.save(os.path.join(output_folder, filename))

print("Done!")
