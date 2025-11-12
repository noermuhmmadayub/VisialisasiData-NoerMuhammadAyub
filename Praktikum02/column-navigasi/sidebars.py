import streamlit as st

# --- Identitas Kelompok ---
st.title("Sidebar")
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

#Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are You a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)

