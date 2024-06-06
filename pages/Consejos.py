
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