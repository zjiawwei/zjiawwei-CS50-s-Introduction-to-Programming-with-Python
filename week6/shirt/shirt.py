import sys
import os
from PIL import Image,ImageOps

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

shirt_1 = sys.argv[1]
shirt_2 = sys.argv[2]
valid = (".jpg",".jpeg",".png")

input_ext = os.path.splitext(shirt_1)[1].lower()
if input_ext not in valid:
    sys.exit("Invalid input file extension")

output_ext = os.path.splitext(shirt_2)[1].lower()
if output_ext not in valid:
    sys.exit("Invalid input file extension")

if input_ext != output_ext:
    sys.exit("Input and output must have the same extension")

try:
    input_image = Image.open(shirt_1)
    shirt_image = Image.open("shirt.png")
    shirt_size = shirt_image.size
    fitted_image = ImageOps.fit(input_image,shirt_size)
    fitted_image.paste(shirt_image,shirt_image)
    fitted_image.save(shirt_2)
except FileNotFoundError:
    sys.exit(f"Input file {input_ext} does not exist")