import streamlit as st
from streamlit_option_menu import option_menu

# NAVIGASI SIDE BAR
with st.sidebar:
    selected = option_menu('Hitung Luas Bangun',
    ['Hitung Luas Persegi Panjang',
     'Hitung Luas Segitiga',
     'Hitung Luas Persegi',
     'Hitung Luas Lingkaran'],
    default_index=0)  # Menambahkan koma setelah list pilihan

# HALAMAN HITUNG LUAS PERSEGI PANJANG
if selected == 'Hitung Luas Persegi Panjang':
    st.title('Hitung Luas Persegi Panjang')
    panjang = st.number_input('Masukkan Nilai Panjang', 0)
    lebar = st.number_input('Masukkan Nilai Lebar', 0)
    hitung = st.button('Hitung Luas')
    if hitung:
        luas = panjang * lebar
        st.success(f'Luas Persegi Panjang Adalah: {luas}')

# HALAMAN HITUNG LUAS SEGITIGA
elif selected == 'Hitung Luas Segitiga':
    st.title('Hitung Luas Segitiga')
    alas = st.number_input('Masukkan Nilai Alas', 0)
    tinggi = st.number_input('Masukkan Nilai Tinggi', 0)
    hitung = st.button('Hitung Luas')
    if hitung:
        luas = 0.5 * alas * tinggi
        st.success(f'Luas Segitiga Adalah: {luas}')

# HALAMAN HITUNG LUAS PERSEGI
elif selected == 'Hitung Luas Persegi':
    st.title('Hitung Luas Persegi')
    sisi = st.number_input('Masukkan Nilai Sisi Persegi', 0)
    hitung = st.button('Hitung Luas')
    if hitung:
        luas = sisi * sisi
        st.success(f'Luas Persegi Adalah: {luas}')

# HALAMAN HITUNG LUAS LINGKARAN
elif selected == 'Hitung Luas Lingkaran':
    st.title('Hitung Luas Lingkaran')
    jari_jari = st.number_input('Masukkan Nilai Jari-Jari Lingkaran', 0)
    hitung = st.button('Hitung Luas')
    if hitung:
        luas = 3.14 * jari_jari * jari_jari  # Menggunakan 3.14 untuk π
        st.success(f'Luas Lingkaran Adalah: {luas}')