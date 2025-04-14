import streamlit as st
import os
import time
from PIL import Image
from removeBG import remove_bg
from OCR import getText, categorizeText

# App title
st.title("Wine Label OCR & Background Removal")

# Upload wine images
uploaded_files = st.file_uploader("Upload Wine Label Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Display original image
        st.subheader(f"Processing: {uploaded_file.name}")
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_container_width=True)

        # Save uploaded file temporarily
        temp_input_path = os.path.join("temp", uploaded_file.name)
        os.makedirs("temp", exist_ok=True)
        image.save(temp_input_path)

        before = time.time()

        # Background removal using PhotoRoom
        processed_image_bytes_io = remove_bg(temp_input_path)

        # Display processed image
        st.image(processed_image_bytes_io, caption="Image with Background Removed", use_container_width=True)

        # OCR and structuring
        image_for_ocr = Image.open(processed_image_bytes_io)
        ocr_text = getText(image_for_ocr)
        structured_text = categorizeText(ocr_text)

        # Display structured result
        st.text_area("Extracted & Structured Text", structured_text, height=150)

        # Filename generation
        def generate_filename(structured_text):
            # Remove double quotes and replace newline characters with spaces
            cleaned = structured_text.replace('"', '').replace('\n', ' ')
            # Optionally, replace other special characters if needed
            return cleaned.strip()



        output_name = generate_filename(structured_text) + ".jpg"


        # Download button
        st.download_button(
            label="📥 Download Processed Image",
            data=processed_image_bytes_io,
            file_name=output_name,
            mime="image/jpeg"
        )

        after = time.time()
        st.write(f"⏱ Processing Time: {after - before:.2f} seconds")