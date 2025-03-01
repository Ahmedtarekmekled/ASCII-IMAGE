import argparse
from PIL import Image
import numpy as np
import os

# Grayscale levels
GSCALE_70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
GSCALE_10 = "@%#*+=-:. "

def load_image(image_path):
    try:
        image = Image.open(image_path) # Convert to grayscale
        return image
    except Exception as e:
        print("Error Loading Image:", e)
        return None

def resize_image(image, fixed_width=200, fixed_height=100, keep_aspect_ratio=False):
    if keep_aspect_ratio:
        aspect_ratio = image.width / image.height
        if fixed_width / fixed_height > aspect_ratio:
            fixed_width = int(fixed_height * aspect_ratio)
        else:
            fixed_height = int(fixed_width / aspect_ratio)
    return image.resize((fixed_width, fixed_height))

def get_average_brightness(image):
    im_array = np.array(image)
    if im_array.size == 0:
        return 127  # Default brightness for empty tiles
    return np.mean(im_array)

def map_brightness_to_ascii(brightness, gscale):
    scale_index = int((brightness / 255) * (len(gscale) - 1))
    return gscale[scale_index]

def generate_ascii(image, cols=200, rows=100, gscale=GSCALE_70):
    image = resize_image(image, cols, rows)
    W, H = image.size
    w, h = W / cols, H / rows
    ascii_art = []
    
    for j in range(rows):
        row_str = ""
        for i in range(cols):
            x1, y1 = int(i * w), int(j * h)
            x2, y2 = min(int((i + 1) * w), W), min(int((j + 1) * h), H)
            tile = image.crop((x1, y1, x2, y2))
            avg_brightness = get_average_brightness(tile)
            row_str += map_brightness_to_ascii(avg_brightness, gscale)
        ascii_art.append(row_str)
    
    return "\n".join(ascii_art)

def save_ascii_to_file(ascii_art, filename):
    with open(filename, "w") as f:
        f.write(ascii_art)
    print("ASCII Art saved to", filename)

def main():
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("image_path", help="Path to the image file.")
    parser.add_argument("-w", "--width", type=int, default=200, help="Width of ASCII output.")
    parser.add_argument("-he", "--height", type=int, default=100, help="Height of ASCII output.")
    parser.add_argument("-s", "--scale", choices=["70", "10"], default="70", help="Grayscale scale to use (70 or 10 characters).")
    parser.add_argument("-a", "--aspect", action="store_true", help="Maintain aspect ratio.")
    parser.add_argument("-o", "--output", help="Output file (default: same as input with .txt extension).")
    
    args = parser.parse_args()
    
    image = load_image(args.image_path)
    if image:
        gscale = GSCALE_70 if args.scale == "70" else GSCALE_10
        ascii_image = generate_ascii(image, cols=args.width, rows=args.height, gscale=gscale)
        
        # Save output
        output_file = args.output if args.output else os.path.splitext(args.image_path)[0] + ".txt"
        save_ascii_to_file(ascii_image, output_file)
        

if __name__ == "__main__":
    main()



# for tile_br in tiles:
#     brightness.append(get_average_brightness(tile_br))

# print(f"Num 1 : {brightness[0]}")

# for infile in os.listdir(convert_folder):
#     input_path = os.path.join(convert_folder, infile)
    
#     try:
#         with Image.open(input_path) as im:
#             print(f"File: {input_path}, Format: {im.format}, W: {im.size[0]}, Mode: {im.mode}")
#             W, H = im.size[0], im.size[1]
            
            
#     except OSError:
#         print(f"Skipping non-image file: {input_path}")