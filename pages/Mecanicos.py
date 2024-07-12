import streamlit as st
import os

# Custom CSS
st.markdown("""
    <style>
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
    .description {
        font-size: 20px;
        text-align: center;
        color: #000000;
        padding-bottom: 30px;
    }
    .mechanic-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
    .mechanic-box {
        background-color: #3B3B3B;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 10px;
        text-align: center;
        flex: 1 0 45%; /* Toma 45% del espacio, para asegurar dos por fila */
        box-sizing: border-box;
    }
    .mechanic-photo {
        width: 100%;
        height: auto;
        border-radius: 10px;
    }
    .mechanic-name {
        font-size: 22px;
        font-weight: bold;
        margin-top: 10px;
        color: #ECC52C;
    }
    .mechanic-rating {
        font-size: 18px;
        color: #FFD700;
        margin: 5px 0;
    }
    .mechanic-phone {
        font-size: 18px;
        color: #00FF00;
    }
    </style>
    """, unsafe_allow_html=True)

# Título de la vista
st.markdown('<div class="title">Servicios de Mantenimiento Móvil</div>', unsafe_allow_html=True)

# Descripción
st.markdown('<div class="description">Encuentra mecánicos móviles cerca de ti que pueden ayudarte con el mantenimiento de tus neumáticos. Estos mecánicos ofrecen servicios a domicilio para tu comodidad.</div>', unsafe_allow_html=True)

# Foto de portada
st.image('mecanico.jpg', use_column_width=True)

# Información de los mecánicos
mechanics = [
    {
        "name": "Juan Pérez",
        "description": "Especialista en mantenimiento de neumáticos con 10 años de experiencia.",
        "rating": "⭐⭐⭐⭐⭐",
        "phone": "+123 456 7890"
    },
    {
        "name": "María López",
        "description": "Experta en reparaciones rápidas y eficientes. Servicio a domicilio.",
        "rating": "⭐⭐⭐⭐⭐",
        "phone": "+123 456 7891"
    },
    {
        "name": "Carlos Sánchez",
        "description": "Técnico de neumáticos con más de 15 años de experiencia en el campo.",
        "rating": "⭐⭐⭐⭐",
        "phone": "+123 456 7892"
    },
    {
        "name": "Laura Martínez",
        "description": "Servicio de mantenimiento y cambio de neumáticos, siempre a tiempo.",
        "rating": "⭐⭐⭐⭐",
        "phone": "+123 456 7893"
    },
    {
        "name": "Pedro Gómez",
        "description": "Conocimiento profundo en todos los tipos de neumáticos y servicios.",
        "rating": "⭐⭐⭐⭐⭐",
        "phone": "+123 456 7894"
    },
    {
        "name": "Ana Fernández",
        "description": "Calidad y confianza en cada servicio, a tu puerta.",
        "rating": "⭐⭐⭐⭐⭐",
        "phone": "+123 456 7895"
    }
]

# Contenedor de mecánicos
st.markdown('<div class="mechanic-container">', unsafe_allow_html=True)
cols = st.columns(2)  # Crear dos columnas

for i, mechanic in enumerate(mechanics):
    col = cols[i % 2]  # Alternar entre columnas
    with col:
        st.markdown(f"""
            <div class="mechanic-box">
                <div class="mechanic-name">{mechanic['name']}</div>
                <div class="mechanic-description">{mechanic['description']}</div>
                <div class="mechanic-rating">{mechanic['rating']}</div>
                <div class="mechanic-phone">{mechanic['phone']}</div>
            </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
