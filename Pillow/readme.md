The Pillow library (also known as PIL or Python Imaging Library) is a popular image processing library in Python. It provides extensive file format support, an efficient internal representation, and powerful image processing capabilities.

You can find the official documentation for Pillow [here](https://pillow.readthedocs.io/en/stable/).

### Basic Usage
Here's a quick example of how to use Pillow to open an image, display it, and save it in a different format:

```python
from PIL import Image

# Open an image file
with Image.open('example.jpg') as img:
    # Display image
    img.show()

    # Save image in a different format
    img.save('example.png')
```

### Common Functions
1. **Opening an image**:
   ```python
   img = Image.open('path_to_image.jpg')
   ```

2. **Saving an image**:
   ```python
   img.save('path_to_save_image.png')
   ```

3. **Resizing an image**:
   ```python
   img = img.resize((width, height))
   ```

4. **Rotating an image**:
   ```python
   img = img.rotate(45)  # Rotate 45 degrees
   ```

5. **Cropping an image**:
   ```python
   cropped_img = img.crop((left, upper, right, lower))
   ```

6. **Converting image modes (e.g., to grayscale)**:
   ```python
   gray_img = img.convert('L')
   ```

### Installation
You can install Pillow using pip:
```bash
pip install Pillow
```

### Advanced Features
Pillow also supports more advanced image processing tasks such as filtering, enhancing, drawing, and much more. For detailed examples and the full API, refer to the [Pillow documentation](https://pillow.readthedocs.io/en/stable/).

If you have any specific questions or need examples for particular tasks, feel free to ask!
