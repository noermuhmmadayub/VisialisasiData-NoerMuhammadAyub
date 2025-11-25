import streamlit as st
import matplotlib.pyplot as plt

# Buat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

#Layout Streamlit
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visalisasi", ("Singgle Line Plot",
                                                        "Multiple & Customization",
                                                        "Jenis Garis Untuk Menunjukan Tren",
                                                        "Subplot"))

#Identitas kelompok
st.caption("Praktikum 3 - Matplotlib Line Chart")
st.markdown("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

#Single Line Plot
def line_plot():
    fig, ax =plt.subplots()
    ax.plot(months, product_A_sales, label="Product A")
    ax.set_title('Penjualan Product A dan B Perbulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    
    
#Multiple Line Plot & Customizations
def customize_lineplot():
    fig, ax =plt.subplots()
    ax.plot(months, product_A_sales, label="Product A", color="blue", linestyle='--', marker='o')
    ax.plot(months, product_A_sales, label="Product B", color="pink", linestyle='-', marker='x')
    
    ax.set_title('Product Penjualan Perbulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    
    
# Jenis garis untuk tren
product_C_sales = [18,22,25,28,32,38,42,45,48,52,56,60]
product_D_sales = [7,9,11,13,16,18,20,23,25,28,30,33]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_C_sales, label="Product C", color="green", linestyle='--', marker='d')
    axs.plot(months, product_D_sales, label="Product D", color="purple", linestyle='-', marker='s')
    axs.set_title('Product Penjualan Perbulan')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Penjualan')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)
    
#Subplot
def subplots():
    fig, axs = plt.subplots(2,1, figsize=(10,8))
    
    # plot pertama untuk product C
    axs[0].plot(months, product_C_sales, label='Product C', linestyle=":", color='green', marker='d')
    axs[0].set_title('Penjuala Product C Perbulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Penjualan')
    axs[0].legend()
    axs[0].grid('True')

#plot pertama untuk product D
    axs[1].plot(months, product_D_sales, label='Product D', linestyle=":", color='purple', marker='s')
    axs[1].set_title('Penjuala Product D Perbulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Penjualan')
    axs[1].legend()
    axs[1].grid('True')
    
    plt.tight_layout()
    st.pyplot(fig)
    
#Logika untuk menampilkan visualisasi sesuai menu
if option == "Singgle Line Plot":
    line_plot()
elif option == "Multiple & Customization":
    customize_lineplot()
elif option == "Jenis Garis Untuk Menunjukan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()