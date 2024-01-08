from PIL import Image
import os

def resize_compress_images(folder):
  for filename in os.listdir(folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
      image = Image.open(os.path.join(folder, filename))
      width, height = image.size
      if width > 500 or height > 500
        # Resize image
        image = image.resize((500, 500), Image.ANTIALIAS)
        image.save(os.path.join(folder, filename), optimize=True, quality=70)
        resize_compress_images("/path/to/image/folder")