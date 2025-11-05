# Import liblary
import streamlit as st
import pandas as pd # untuk mengelola data dalam bentuk tabel (dataframe)
import numpy as np # untuk membuat data numerik acak
import altair as alt # untuk membuat chat interaktif

#menampilkan
st.title("Praktikum 1: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Data Element")

st.markdown("""
Kelompok 1:
- Noer Muhammad Ayub - 0110222142
- Saski - 011
- Rahmi atika - 011
""")


# Dataframe: stuktur data berbentuk tabel (baris dan kolom) yang disediakaan oleh liblary pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

# Menampilkan dataframe
st.dataframe(df)

# Higlight
st.subheader("Highlight Minimum value di DataFrame")

# Highlight nilai terkecil disetiap kolom dataframe
# axis=0 berkerja perkolom
st.dataframe(df.style.highlight_min(axis=0))

# Tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

# Menampilkan tabel statis
st.table(df)

# Matrics: Komponen tampilan angka penting
st.subheader("Matrics")
st.metric (label="Temperature", value="31 °C", delta="1.2 °C")#kenaikan 1.2 °C

# Matrics sesuai delta_color
#delta_color digunakan untuk memberi sesuai warna arah perubahan
# - "normal" (default): naik = hijau, turun = merah
# - "inverse": Kenalikannya (naik = merah)
# off: tidak menampilkan warna perubahan

# definisikan variabel metrics
col1, col2, col3 = st.columns(3)

# menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") #naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off") # netral (tidak baik, tidak buruk)

#Menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value="none", delta=0) #kosong, naik baik
st.metric("Tress", "91456", "-1132649") # turun buruk akrena disetting default
