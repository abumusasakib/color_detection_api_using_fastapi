import urllib.parse
import base64
from fastapi import FastAPI

from io import BytesIO
from PIL import Image
import numpy as np

import zlib

app = FastAPI()

@app.get("/data/")
def save_image_data(imageData: str, targetColorRed: int, targetColorGreen: int, targetColorBlue: int, inputColorThreshold: int, boxThreshold: int, compressed: int):
    # URL decode the parameter
    url_decoded_string = urllib.parse.unquote(imageData)

    # Base64 decode the URL-decoded string
    base64_decoded_data = base64.b64decode(url_decoded_string)

    if compressed == 1: #compressed
        # Decompress the data using zlib
        decompressed_data = zlib.decompress(base64_decoded_data)

        # Base64 decode the decompressed data
        data = base64.b64decode(decompressed_data)
    elif compressed == 0: #not compressed
        # Base64 decode the decompressed data
        data = base64.b64decode(base64_decoded_data)
    else:
         raise Exception("Invalid parameter")

    # Create a binary stream in memory
    image_stream = BytesIO(data)

    # Read the image from the binary stream using PIL
    image = Image.open(image_stream)

    # Check if the image format is recognized
    if image.format not in ["JPEG", "PNG", "GIF"]:
        raise Exception("Unsupported image format")

    # Get image info
    image_file_format = image.format
    image_mode = image.mode
    image_width = image.width
    image_height = image.height

    # Convert the image to RGB mode if it's not already
    if image_mode != "RGB":
        image = image.convert("RGB")

    # Convert the image to a NumPy array
    image_array = np.array(image)

    target_color = np.array([targetColorRed, targetColorGreen, targetColorBlue])
    color_distance = np.linalg.norm(image_array - target_color, axis=2)

    # masking pixels
    output_mask = color_distance <= inputColorThreshold

    # Find the coordinates of pixels by boolean indexing using pink mask
    output_coordinates = np.argwhere(output_mask)

    min_x, min_y = output_coordinates.min(axis=0)
    max_x, max_y = output_coordinates.max(axis=0)

    copy = image_array[min_x:max_x, min_y:max_y]

    image_with_box = np.copy(image)

    height, width, _ = image_with_box.shape

    min_x -= boxThreshold
    min_y -= boxThreshold
    max_x += boxThreshold
    max_y += boxThreshold

    # Calculate boundary limits
    # Ensure min_x, max_x, min_y, and max_y are within bounds
    min_x = np.max(a=min_x, initial=0)
    max_x = np.min(a=max_x, initial=height)
    min_y = np.max(a=min_y, initial=0)
    max_y = np.min(a=max_y, initial=width)

    # box with green color
    if min_x < max_x and min_y < max_y:
        image_with_box[min_x: max_x, min_y, :] = [0, 255, 0]  # Draw top horizontal line
        image_with_box[min_x: max_x, max_y, :] = [0, 255, 0]  # Draw bottom horizontal line
        image_with_box[min_x, min_y: max_y, :] = [0, 255, 0]  # Draw left vertical line
        image_with_box[max_x - 1, min_y: max_y, :] = [0, 255, 0]  # Draw right vertical line

    # Save the processed image
    processed_image = Image.fromarray(image_with_box)
    processed_image.save("sample_file.jpg")


    return {
        "image file format": image_file_format,
        "image mode": image_mode,
        "image width": image_width,
        "image height": image_height,
        "target color red": targetColorRed,
        "target color green": targetColorGreen,
        "target color blue": targetColorBlue,
        "color threshold": inputColorThreshold,
        "box threshold": boxThreshold,
        "minX": int(min_x),
        "minY": int(min_y),
        "maxX": int(max_x),
        "maxY": int(max_y)
    }
