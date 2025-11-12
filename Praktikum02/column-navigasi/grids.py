import streamlit as st
from PIL import Image

# --- Identitas Kelompok ---
st.title("Grids")
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

img = Image.open("D:/Virtual Code/streamlit/visdat\praktikum/assets/violet.png")
#Defening no ofrows
for a in range(4):
#Defening no. of columns with size
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)