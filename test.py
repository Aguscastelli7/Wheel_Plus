from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st 
import os

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# List all files in the directory containing the script
directory_files = os.listdir(script_dir)
# st.text("Files in directory: " + ", ".join(directory_files))

def classify_tire(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model_path = os.path.join(script_dir, "modelo_IA", "keras_model.h5")
    model = load_model(model_path, compile=False)

    # Load the labels
    labels_path = os.path.join(script_dir, "modelo_IA", "labels.txt")
    class_names = open(labels_path, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = img.convert("RGB")

    # Resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name, confidence_score

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
        font-size: 30px;
        text-align: center;
        font-weight: bold;
        color: #ECC52C;
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
    </style>
    """, unsafe_allow_html=True)

# Center the logo image using Streamlit's container
with st.container():
    st.markdown('<div class="center-logo">', unsafe_allow_html=True)
    st.image('logo.png', caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
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
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="column-box">', unsafe_allow_html=True)
            st.info("Confianza de la predicción")
            st.success(f"{confidence_score * 100:.2f}%")
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
import streamlit as st 

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
        font-size: 30px;
        text-align: center;
        font-weight: bold;
        color: #ECC52C;
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
    </style>
    """, unsafe_allow_html=True)

# Title of the new view
st.markdown('<div class="title">Consejos de Mantenimiento de Neumáticos</div>', unsafe_allow_html=True)

# Subtitle
st.markdown('<div class="subtitle">Mantén tus neumáticos en buen estado</div>', unsafe_allow_html=True)

# Description
st.markdown('<div class="description">Aquí hay algunos consejos para ayudarte a mantener tus neumáticos en condiciones óptimas y garantizar tu seguridad al conducir.</div>', unsafe_allow_html=True)

# Tips Section
st.markdown("""
    <div class="feature-container">
        <div class="feature-box">
            <h2>Revisa la presión regularmente</h2>
            <p>Verifica la presión de tus neumáticos al menos una vez al mes y antes de viajes largos. Usa un medidor de presión de neumáticos para asegurarte de que están inflados correctamente.</p>
        </div>
        <div class="feature-box">
            <h2>Inspecciona el desgaste</h2>
            <p>Revisa tus neumáticos en busca de signos de desgaste desigual, cortes, perforaciones o protuberancias. Si encuentras algo inusual, considera reemplazarlos.</p>
        </div>
    </div>
    <div class="feature-container">
        <div class="feature-box">
            <h2>Rota tus neumáticos</h2>
            <p>Rota tus neumáticos cada 10,000 km o según las recomendaciones del fabricante para asegurar un desgaste uniforme y prolongar la vida útil de los neumáticos.</p>
        </div>
        <div class="feature-box">
            <h2>Alineación y balanceo</h2>
            <p>Asegúrate de que las ruedas estén alineadas y balanceadas correctamente. La mala alineación puede causar un desgaste desigual y reducir la vida útil de los neumáticos.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Recuerda que un buen mantenimiento de tus neumáticos no solo te ayuda a ahorrar dinero, sino que también garantiza tu seguridad en la carretera.</div>', unsafe_allow_html=True)