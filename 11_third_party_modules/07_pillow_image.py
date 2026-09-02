# Install first: pip install pillow
from PIL import Image, ImageDraw

image = Image.new("RGB", (300, 150), "white")
draw = ImageDraw.Draw(image)
draw.rectangle((30, 30, 270, 120), fill="lightblue", outline="navy")
draw.text((85, 65), "Python Example", fill="black")
image.save("python_example.png")
print("Image saved")
