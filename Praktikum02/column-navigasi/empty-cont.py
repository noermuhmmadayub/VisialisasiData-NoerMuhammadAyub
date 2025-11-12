import streamlit as st
import time

# --- Identitas Kelompok ---
st.title("Empty Container")
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

with st.empty():
    for second in range(5):
        st.write(f"⏳{second} second have passed")
        time.sleep(1)
        st.write("✅ Times up!")