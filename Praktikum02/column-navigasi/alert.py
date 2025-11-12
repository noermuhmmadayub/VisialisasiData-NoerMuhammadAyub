import streamlit as st
# --- Identitas Kelompok ---
st.title("🚨 Alert & Notification Panel")
st.write("Kelompok 28 - Visualisasi Data")

st.markdown("""
**👥 Nama Kelompok:**
- 🧑‍💻 Muhammad Ayub (NIM: 12345678)
- 👩‍💻 Rahmi Atika (NIM: 0110222279)
- 👩‍💻 Saskia Putri Ananda (NIM: 0110222159)
---
""")

# --- ALERT STYLISH ---
st.subheader("🔔 Notifikasi Sistem")

st.success("✅ **Berhasil!** Data berhasil diproses tanpa error.")
st.warning("⚠️ **Peringatan!** Periksa kembali format data sebelum melanjutkan.")
st.info("ℹ️ **Informasi:** File CSV telah diunggah ke sistem.")
st.error("❌ **Kesalahan:** Gagal menghubungkan ke server database.")

# --- EXCEPTION DENGAN GAYA ---
st.subheader("💥 Simulasi Exception")

try:
    # Contoh error buatan
    result = 10 / 0
except Exception as e:
    st.exception(e)

st.markdown("---")
st.caption("✨ Dibuat oleh CADIS ✨")
