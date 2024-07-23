# Q&A Chatbot

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load model and get responses
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash-001')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

# Add CSS for styling including background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('ai img.jpeg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
        z-index: 1;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #444;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 10px;
    }
    .stFileUploader>label {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 10px;
        cursor: pointer;
    }
    .stFileUploader>label:hover {
        background-color: #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

st.header("Image to Text translation using Gemini Pro")

# Input prompt
input = st.text_input("Input Prompt: ", key="input")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Submit button
submit = st.button("Generate and Translate image to text")

# Display response if button is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is :")
    st.write(response)
