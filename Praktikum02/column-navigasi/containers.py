import streamlit as st
import numpy as np

# --- Identitas Kelompok ---
st.title("Container")
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

with st.container():
    st.write("Element inside container")
    #Defenig Chart Element
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside Container")
    
st.title("Out of order Containers")
#Defening Contaners
container_one = st.container()
container_one.write("Element One Inside Containers")
st.write("Element Outside Containers")
#Now insert few more elements in the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 2))