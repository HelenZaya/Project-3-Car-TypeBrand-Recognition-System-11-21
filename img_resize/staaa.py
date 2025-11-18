from PIL import Image
import os

# --- Settings ---
input_folder = "./images"          # your original images folder
output_folder = "resized"        # folder to save resized images
new_size = (512, 512)            # width, height

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):

        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize
        img_resized = img.resize(new_size)

        # Save to output folder
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)

        print("Resized:", filename)

print("Done! All images resized.")
