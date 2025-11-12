import streamlit as st

# --- Identitas Kelompok ---
st.title("Column")
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolum pertama")
col1.image(r"D:\Virtual Code\streamlit\visdat\praktikum\assets\violet.png")

col2.write("Ini adalah kolum kedua")
col2.image(r"D:\Virtual Code\streamlit\visdat\praktikum\assets\ramadhan.jpg")
