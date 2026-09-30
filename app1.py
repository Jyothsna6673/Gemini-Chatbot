

import streamlit as st

import os
from google import genai

# Load environment variables

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="✨",
    layout="centered"
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    /* Main background and font styling */
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Inter', sans-serif;
    }

    /* Title styling */
    h1 {
        color: #1a73e8;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0px;
    }

    /* Subtitle/description styling */
    .subtitle {
        text-align: center;
        color: #5f6368;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }

    /* Text area styling */
    div.stTextArea > label {
        font-weight: 600;
        color: #3c4043;
    }

    div.stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #dadce0;
        padding: 12px;
        font-size: 1rem;
    }

    div.stTextArea textarea:focus {
        border-color: #1a73e8;
        box-shadow: 0 0 0 2px rgba(26, 115, 232, 0.2);
    }

    /* Button styling */
    .stButton > button {
        width: 100%;
        background-color: #1a73e8;
        color: white;
        font-weight: 600;
        padding: 0.75rem;
        border-radius: 12px;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #1557b0;
        box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
    }

    /* Success box styling */
    .stSuccess {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP UI ---
st.title("Gemini AI Chatbot")
st.markdown('<p class="subtitle">Ask Gemini anything and get instant, intelligent answers!</p>', unsafe_allow_html=True)

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="e.g., Explain AI in simple words..."
)

if st.button("Generate Response"):
    if prompt:
        with st.spinner("✨ Gemini is thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash", # Note: Updated to a stable standard model name, change back if needed
                    contents=prompt
                )
                st.success("Response generated successfully!")
                st.markdown("### Answer:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a prompt before generating a response.")
