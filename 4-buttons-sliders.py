import streamlit as st
import time

# --- Identitas Kelompok ---
st.title("Kelompok 28 - Visualisasi Data")
st.write("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

st.title ('Creating a Button')
#Defining a Button
button = st.button ('click Here')
if button:
    st.write('You have clicked th Button')
else:
    st.write('You have not clicked the Button')
    
#Defening Radio Button
st.subheader("Creating Radio Button")
role = st.radio(
    "Select Your Role",
    ('Roam', 'GoldLane', 'MidLane', 'ExpLane', 'Jungle'))
if role == 'Roam':
    st.write('You have select Roam')
elif role == 'GoldLane':
    st.write('You have select GoldLane')
elif role == 'MidLane':
    st.write('You have select MidLane')
elif role == 'ExpLane':
    st.write('You have select ExpLane')
elif role == 'Jungle':
    st.write('You have select Jungle')
else:
    st.write('You have select Others')
    
#Check Boxes
st.subheader("Creating Checkboxes")
st.write('Select Your Hobies:')
#Defening Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Sports')
check_3 = st.checkbox('Movie')

#Drop-Downs
st.subheader("Creating Dropdowns")
#Defening Dropdown
hobby = st.selectbox('Choose your hobby:',
('Books', 'Sports', 'Movie'))

#Multi Select
st.subheader("Creating Multi-Select")
#Defening Multi-Seelct
hobbies = st.multiselect(
'What are your Hobbies',
['Reading', 'Cooking','Whact Movie', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Hiking']) 

#Downlaod Buttons
st.subheader("Download Buttons")
#Defening Download Buttons
down_btn = st.download_button(
label = "Download Image",
 data=open(r"C:\Users\LENOVO\OneDrive\Pictures\1065466.png", "rb"),
file_name="cadis.jpg",
mime="image/jpg"
)

#Progress Bars
st.subheader("Progress Bars")
#Defening Progress Bars
download= st.progress(0)
for percentage in range (100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write ('Download Complate')

#Spinners
st.subheader('Spinner')
#Defening Spinner
with st.spinner('Loading...'):
    time.sleep (5)
st.write ('Hello Cadis')