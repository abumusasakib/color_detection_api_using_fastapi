# Color Detection API Using FastAPI

## Target Acquisition Through Color Tone Detection in Embedded Settings with Server Off-Loading

### Alternate Title

## Utilizing Color Tone Analysis with Server-Based Processing for Target Detection in Embedded Environments

This group project was completed by me along with my fellow batchmates and our respected trainer at Hypertag Solutions Ltd. The server is a FastAPI application hosted locally for processing image data. The `main.py` file contains the code for the API, and `test.py` makes API calls using the `requests` library.

## How the API Works

1. Import necessary libraries and modules.
2. Load an image using the `PIL` library.
3. Convert the image to a base64-encoded string.
4. Optionally compress the string using `zlib`.
5. URL encode the data.
6. Send an HTTP GET request to the FastAPI server running locally, including the encoded and compressed image data, as well as additional parameters like target color and compression flag.
7. Print the length of the URL-encoded string and the JSON response from the server.

## Synopsis

The primary task of this project is to detect the location of a target within an image by identifying its color using a server-based color detection algorithm. The image data is passed to the API via a GET request, along with parameters such as the RGB values of the target color, the color threshold (to account for acceptable variations in the color), the box threshold (which adjusts the bounding box that highlights the target), and a flag indicating whether the image data is compressed.

The image is either sent to the API as a base64-encoded string or compressed using `zlib`. After the API receives the image, it processes the string, converts it back into a binary image, and analyzes the data to isolate the target color. Upon successful analysis, the API returns the image’s information and the bounding box coordinates where the target color was detected.

## Color Detection API

An API for detecting color from an image.

**Base URL:** `http://127.0.0.1:8000`

### Process Image Data

#### Endpoint: `/data`

##### GET /data

- **Summary:** Process image data
- **Description:** This endpoint processes image data using specified parameters.

##### Parameters

- `imageData` (query, required): Base64-encoded image data.
- `targetColorRed` (query, required): Red component of the target color.
- `targetColorGreen` (query, required): Green component of the target color.
- `targetColorBlue` (query, required): Blue component of the target color.
- `inputColorThreshold` (query, required): Threshold for acceptable variations in the target color.
- `boxThreshold` (query, required): Threshold for adjusting the bounding box around the target.
- `compressed` (query, required): Flag indicating whether the image data is compressed.

---

### Running the Application Locally

1. **Install dependencies:**
   Ensure you have FastAPI and the necessary Python libraries installed.

   ```bash
   pip install fastapi uvicorn pillow numpy
   ```

   OR

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI server:**
   Start the FastAPI application locally.

   ```bash
   uvicorn main:app --reload
   ```

3. **Make API requests:**
   Use `test.py` to send image data to the API.

   ```bash
   python test.py
   ```
