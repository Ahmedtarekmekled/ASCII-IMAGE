import os, sys
from PIL import Image

img_folder = "img"
convert_folder = "converted"

for infile in os.listdir(img_folder):
    input_path = os.path.join(img_folder,infile)
    f,e = os.path.splitext(infile)
    output_path = os.path.join(convert_folder, f+".jpg")
    try:
        with Image.open(input_path) as im:
            im = im.convert("L")
            im.save(output_path, "JPEG")
    except Exception as e:
        print(f"❌ Error converting {infile}: {e}")

print("✅ All conversions complete!")
        