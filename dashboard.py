import streamlit as st

st.title("halaman dashboard")

#fungsi untuk menghitung dan menyimpan total nabung 
def total():
    total_nabung = sum(t['Jumlah'] for t in st.session_state ['jumlah'] if t ['Type'] == 'Menabung')

    return f"total menabung kamu {total_nabung}"

st.write(total())