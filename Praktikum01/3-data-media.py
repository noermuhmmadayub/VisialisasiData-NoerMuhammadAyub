import streamlit as st

# --- Identitas Kelompok ---
st.title("Kelompok 28 - Visualisasi Data")
st.write("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")


# --- Bagian 3: Data and Media Elements ---
st.header("3. Data and Media Elements")

# 1️ Menampilkan gambar
st.subheader("Menampilkan Gambar")
st.image(r"C:\Users\LENOVO\OneDrive\Pictures\1065466.png", caption="Contoh Gambar", use_container_width=True)

# 2️ Menambahkan background image (opsional)
st.subheader("Menambahkan Background Image (CSS)")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1503264116251-35a269479413");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3️ Mengubah ukuran gambar (Resizing)
st.subheader("Mengubah Ukuran Gambar")
st.image(r"C:\Users\LENOVO\OneDrive\Pictures\1065466.png", caption="Aku dan Dia", width=400)

st.write("Image Courtesy: cadis.com")
