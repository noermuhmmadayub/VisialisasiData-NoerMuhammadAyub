import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# --- Identitas Kelompok ---
st.title("Bar Chart")
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

#data
data = {
    'Jurusan' : ['Ilmu komputer', 'Sistem Informatika', 'Teknik Informatika', 'Data Sciense'],
    'Jumlah Mahasiswa': [120, 80, 60, 40]
}
df = pd.DataFrame(data)

# streamlit bar chart
st.title("Bar Chart - Jumlah Mahasiswa Perjurusan")
st.bar_chart(df.set_index('Jurusan'))

st.title("Basic Bar Chart Menggunakan Matplotlib")
fig, ax = plt.subplots()
ax.bar(df['Jurusan'], df['Jumlah Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa Perjurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('jumlah Mahasiswa')

st.pyplot(fig)

st.title("Kustomisasi barChart")
fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange', 'red']
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa Perjurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('jumlah Mahasiswa')
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
            str(bar.get_height()), ha='center')

st.pyplot(fig)

#Multiple Bar Chart
st.title("Multiple Bar Chart")

#data tambahan
data_2023 = [120, 150, 100, 80]
data_2024 = [140, 160, 110, 90]

x = range(len(data['Jurusan']))
width = 0.4

fig, ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023', color='skyblue')
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')

ax.set_title('Jumlah Mahasiswa Perjurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(data['Jurusan'])
ax.legend()

st.pyplot(fig)

                            
# Data jumlah mahasiswa per jurusan selama 5 tahun
data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [120, 125, 135, 145, 160],
    'Teknik Informatika': [90, 95, 100, 105, 110],
    'Data Science': [70, 75, 80, 85, 90]
}

# Membuat dataframe untuk visualisasi
df = pd.DataFrame(data)

# Streamlit App
st.title("Visualisasi Tren Jumlah Mahasiswa Memilih Jurusan Komputer (5 Tahun Terakhir)")

# Menambahkan filter tahun
filter_tahun = st.multiselect("Pilih Tahun:", df['Tahun'], default=df['Tahun'])

# Menambahkan filter jurusan
jurusan_list = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
filter_jurusan = st.multiselect("Pilih Jurusan:", jurusan_list, default=jurusan_list)

# Filter data berdasarkan input pengguna
filtered_data = df[df['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jurusan]

# Menampilkan data tabel
st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

# Membuat Bar Chart dengan filter
st.subheader("Bar Chart dengan Filter")
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat Bar Chart berdasarkan data yang difilter
x = range(len(filtered_data['Tahun']))
width = 0.2

for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

# Menyesuaikan sumbu dan judul
ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([p + width * len(filter_jurusan) / 2 - width / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'])
ax.legend()

# Menampilkan plot di Streamlit
st.pyplot(fig)
