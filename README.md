# color_detection_api_using_fastapi

## Target acquisition through color tone detection in embedded settings via server off-loading

### Alternate title:
## Utilizing Color Tone Analysis with Server-Based Processing for Target Detection in Embedded Environments

This group project was by me along with my fellow batchmates and our respected trainer at Hypertag Solutions Ltd. The server is a FastAPI application hosted using Deta Space at `https://fastapi-1-g8913155.deta.app`. The main.py file is the code of the API, and the test.py makes API calls using the requests library.

Here's how the API works:

1. Import necessary libraries and modules.
2. Load an image using the PIL library.
3. Convert the image to a base64-encoded string.
4. Optionally, compress the string using zlib.
5. URL encode the data.
6. Send an HTTP GET request to the FastAPI server, including the encoded and compressed image data, as well as some parameters like target color and compression flag.
7. Print the length of the URL-encoded string and the JSON response from the server.

# Synopsis:

Our primary task here is to detect the location of a target by identifying its color within the image by using a color detection algorithm which runs on the server. We at first take the image data as input and pass it to the API using a GET request. We also take other parameters such as the RGB values of the target color, the color threshold (acceptable variations of the color), the box threshold (for adjusting the bounding box which highlights the target), and whether compressed image data is sent to the API. The image is passed to the API by either sending a base64 encoded string or by sending a zlib-compressed string. After the image is received by the API, the server processes the passed string and converts it to a binary image. Afterwards, an analysis is done to isolate the target color from the image; and after successful analysis the API returns the input image's information, and the boundary where the target was found.

# Color Detection API

An API for detecting color from an image

**Base URL:** `https://fastapi-1-g8913155.deta.app`

## Process Image Data

### Endpoint: `/data`

#### GET /data

- **Summary:** Process image data
- **Description:** Endpoint for processing image data with specified parameters.

##### Parameters

- `imageData` (query, required): Base64-encoded image data
- `targetColorRed` (query, required): Red component of the target color
- `targetColorGreen` (query, required): Green component of the target color
- `targetColorBlue` (query, required): Blue component of the target color
- `inputColorThreshold` (query, required): Threshold for input color
- `boxThreshold` (query, required): Threshold for box
- `compressed` (query, required): Flag indicating whether the image data is compressed

