from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st 
import os
import pandas as pd

# Custom CSS
st.markdown("""
    <style>
    p{
        color: #ffffff;
    }
    h2{
        color:#ffffff;
    }
    .main {
        background-color: #757975;  
    }
    .stApp {
        background-color: #757975;  
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        padding-top: 30px;
        padding-bottom: 10px;
        color: #000000;
    }
    .subtitle {
        font-size: 35px;
        text-align: center;
        font-weight: bold;
        color: #ECC52C;
        margin-top: 20px;
    }
    .description {
        font-size: 20px;
        text-align: center;
        color: #000000;
        padding-bottom: 30px;
    }
    .feature-container {
        display: flex; 
        justify-content: space-around; 
        width: 100%;
        margin: 0 auto;
    }
    .feature-box {
        background-color: #3B3B3B;
        color: #000000;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 10px;
        text-align: center;
        flex: 1;
    }
    .footer {
        text-align: center;
        color: #000000;
        padding: 10px;
    }
    .cta-button {
        background-color: #ECC52C;
        color: #000000;
        border: none;
        padding: 15px 30px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
    }
    .stButton > button {
        background-color: #ECC52C;
        color: #000000;
        border: none;
        padding: 15px 30px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
    }
    .center-logo {
        display: flex;
        justify-content: center;
    }
    .center-video {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .center-button {
        display: flex;
        justify-content: center;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="center-logo">', unsafe_allow_html=True)
    st.image('brigestone.png', caption=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">Tutoriales en Video</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="description">
        Nos enorgullece colaborar con Bridgestone, una marca de alta confianza en el mundo de los neumáticos. 
        En los siguientes videos, los expertos de Bridgestone te mostrarán cómo realizar varias tareas de 
        mantenimiento y cambio de neumáticos.
    </div>
    """, unsafe_allow_html=True)

    
# Lista de videos tutoriales
videos_tutoriales = [
    {"titulo": "Cómo cambiar una rueda", "url": "https://www.youtube.com/embed/M1gVuAmXNVI"},
    {"titulo": "Cómo conocer la presión adecuada para mis llantas", "url": "https://www.youtube.com/embed/7IJkSZjSfLs"},
    {"titulo": "Cuáles son los cuidados básicos de mi llanta", "url": "https://www.youtube.com/embed/qFrWymyBxZg"}
]

# Mostrar los videos en la aplicación
for video in videos_tutoriales:
    st.markdown(f"### {video['titulo']}")
    st.markdown(f'<div class="center-video"><iframe width="480" height="270" src="{video["url"]}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>', unsafe_allow_html=True)
