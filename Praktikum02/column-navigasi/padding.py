import streamlit as st
from PIL import Image

# --- Identitas Kelompok ---
st.title("Padding")
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

img = Image.open("D:/Virtual Code/streamlit/visdat\praktikum/assets/violet.png")
#Defening Padding with columns
col1, padding, col2 = st.columns((10, 2, 10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)