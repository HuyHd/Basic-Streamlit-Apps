import numpy as np
import streamlit as st
from PIL import Image
from process_image import process_image, annotate_image


def main():
    st.title("Object Detection for Images")

    # Create a file uploader widget that allows users to upload images of type jpg, png, or jpeg
    file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    # Check if a file has been uploaded
    if file is not None:
        st.image(file, caption="Uploaded Image")

        image = Image.open(file)
        image = np.array(image)

        # Process the image to detect objects
        detections = process_image(image)

        # Annotate the image with the detection results
        processed_image = annotate_image(image, detections)
        st.image(processed_image, caption="Processed Image")


# Check if the script is being run directly (and not being imported)
if __name__ == "__main__":
    main()
