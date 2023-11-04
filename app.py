import cv2
import streamlit as st
import numpy as np

# Adding a title and markdown to the web app.
st.title("First Streamlit Web Application")
st.markdown("This simple web application renders \
the uploaded images into grayscale mode.")

# Adding a sidebar and adding a title to it.(Optional)
st.sidebar.title("First Streamlit Web Application")
st.sidebar.markdown("This simple web application renders \
the uploaded images into grayscale mode.")

# Creating a file uploader widget on the sidebar.
uploaded_file=st.sidebar.file_uploader(label="Upload Image",\
type=["jpg","jpeg","png"],key="i")

# Opening the uploaded image, converting it to grayscale and rendering it on the web app.
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()),\
    dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.subheader("Grayscale Image")
    st.image(image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY),width=400)

