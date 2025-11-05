import streamlit as st
import datetime
import pandas as pd

# --- Identitas Kelompok ---
st.title("Kelompok 28 - Visualisasi Data")
st.write("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

st.title('Text Box')

#Creating Text Box
st.subheader("Text Box")
name = st.text_input ('Enter your Name')
st.write("Your Name is", name)

#Text Area
st.subheader("Text Area")
input_text = st.text_area ('Enter your Riview')
#Printing Entered Text
st.write("""You entered:\n""", input_text)

#Number Input
st.subheader("Number Input")
st.number_input('Enter your Number')
num = st.number_input ('Enter your Number', 0, 10, 5, 2)
st.write("Min. value is 0. \n Max. value is 10")
st.write("Default value is 5, \n Step size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

#TIME
st.subheader("TIME")
st.time_input (" Select your Time")

#DATE
st.subheader("DATE")
st.date_input ("Select yout Date", value=datetime.date (1989, 12, 25 ),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))

#COLOR
st.subheader("COLOR")
color_code = st.color_picker ("Select your Color")
st.header (color_code)

#Dataset Upload
st.subheader("CSV Data")
data_file = st.file_uploader ("Upload CSV", type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file name" :data_file.name, "file_type": data_file.type,
        "file_size": data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV file uploaded")

#Submit Button
st.subheader("Submit Button")
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
#Defening Submit Button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)