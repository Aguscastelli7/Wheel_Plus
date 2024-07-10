from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st 
import os
import pandas as pd
from datetime import datetime
import webbrowser

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Function to classify the tire condition
def classify_tire(img):
    np.set_printoptions(suppress=True)
    model_path = os.path.join(script_dir, "modelo_IA", "keras_model.h5")
    model = load_model(model_path, compile=False)
    labels_path = os.path.join(script_dir, "modelo_IA", "labels.txt")
    class_names = open(labels_path, "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name, confidence_score

# Function to save the prediction result
def save_prediction(image_name, label, confidence_score):
    csv_path = os.path.join(script_dir, "historial_predicciones.csv")
    df = pd.DataFrame([[datetime.now(), image_name, label, confidence_score]], columns=["Fecha", "Imagen", "Condicion", "Confianza"])
    if not os.path.isfile(csv_path):
        df.to_csv(csv_path, index=False)
    else:
        df.to_csv(csv_path, mode='a', header=False, index=False)

# Function to save the maintenance date
def save_maintenance_date(date):
    csv_path = os.path.join(script_dir, "mantenimiento.csv")
    df = pd.DataFrame([[datetime.now(), date]], columns=["Fecha de Registro", "Fecha de Mantenimiento"])
    if not os.path.isfile(csv_path):
        df.to_csv(csv_path, index=False)
    else:
        df.to_csv(csv_path, mode='a', header=False, index=False)

# Streamlit App

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

# Center the logo image using Streamlit's container
with st.container():
    st.markdown('<div class="center-logo">', unsafe_allow_html=True)
    st.image('logo1.png', caption=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">Revisa la condición de tus neumáticos en cuestión de segundos</div>', unsafe_allow_html=True)
st.markdown('<div class="description">La seguridad es lo primero. Con Wheel+, carga una foto de tus neumáticos y obtén un análisis instantáneo de su estado. Nuestra aplicación te dirá si tus neumáticos están en condiciones seguras para circular o si necesitan ser reemplazados.</div>', unsafe_allow_html=True)

# Feature section
st.markdown("""
    <div class="feature-container">
        <div class="feature-box">
            <h2>Características</h2>
            <p>Analiza la condición de tus neumáticos en segundos</p>
        </div>
        <div class="feature-box">
            <h2>Beneficios</h2>
            <p>Seguridad y tranquilidad al conducir</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="description">A continuación carga una imagen de tu neumático.</div>', unsafe_allow_html=True)

input_img = st.file_uploader("Elegir imagen", type=['jpg', 'png', 'jpeg'])

if input_img is not None:
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button("Determinar estado del neumático"):
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            st.markdown('<div class="column-box">', unsafe_allow_html=True)
            st.info("Imagen cargada")
            st.image(input_img, use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="column-box">', unsafe_allow_html=True)
            st.info("Resultado")
            image_file = Image.open(input_img)

            with st.spinner('Analizando imagen...'):
                label, confidence_score = classify_tire(image_file)

                # Extraer el nombre de la etiqueta sin el número
                label_description = label.split(maxsplit=1)[1]  # Divide la etiqueta por el primer espacio y toma el segundo elemento
                label2 = label_description  # Guarda la descripción en label2

                st.success(label2)  # Muestra la etiqueta sin el número

                # Save the prediction to the CSV file
                save_prediction(input_img.name, label2, confidence_score)
                
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="column-box">', unsafe_allow_html=True)
            st.info("Confianza de la predicción")
            st.success(f"{confidence_score * 100:.2f}%")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)


# Mostrar mapa con gomerías cercanas
st.markdown('<div class="subtitle">Gomerías Cercanas</div>', unsafe_allow_html=True)

with st.expander("Busca las gomerías Cercanas 🗺️"):
    user_location = st.text_input("Ingrese su dirección:")

if user_location:
    st.write(f"Ubicación ingresada: {user_location}")
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button("Ver gomerías cercanas en Google Maps"):
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query=gomerias+cercanas+{user_location}"
    webbrowser.open_new_tab(google_maps_url)
    st.markdown('</div>', unsafe_allow_html=True)

# Testimonials section
st.markdown("""
    <div class="feature-container">
        <div class="feature-box">
            <h2>Testimonios</h2>
            <p>"Wheel+ me ayudó a detectar que mis neumáticos necesitaban ser reemplazados. ¡Una herramienta imprescindible!" - Juan Pérez</p>
        </div>
        <div class="feature-box">
            <h2>Fácil de usar</h2>
            <p>Carga una foto y obtén resultados instantáneos</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Sección de Tutoriales en Video
st.markdown('<div class="subtitle">Tutoriales en Video</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="description">
        Nos enorgullece colaborar con Bridgestone, una marca de alta confianza en el mundo de los neumáticos. 
        En los siguientes videos, los expertos de Bridgestone te mostrarán cómo realizar varias tareas de 
        mantenimiento y cambio de neumáticos.
    </div>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="center-logo">', unsafe_allow_html=True)
    st.image('brigestone.png', caption=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.markdown('</div>', unsafe_allow_html=True)

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

# Calendario de Mantenimiento
st.markdown('<div class="subtitle">Calendario de Mantenimiento</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="description">
        Planifica el mantenimiento de tus neumáticos para asegurarte de que siempre estén en óptimas condiciones.
        Selecciona una fecha para tu próximo mantenimiento.
    </div>
    """, unsafe_allow_html=True)

maintenance_date = st.date_input("Selecciona una fecha para el mantenimiento", datetime.now())

st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button("Guardar fecha de mantenimiento"):
    save_maintenance_date(maintenance_date)
    st.success(f"Fecha de mantenimiento guardada: {maintenance_date}")
    st.info("Tu fecha se ha guardado automáticamente en el calendario de tu teléfono.")
st.markdown('</div>', unsafe_allow_html=True)
