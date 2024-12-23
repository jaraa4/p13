import streamlit as st

st.title("halaman Menabung")

#halaman menabung

with st.form("Menabung"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    submit_button = st.form_submit_button(label="Menabung")
    if submit_button:
        st.session_state['jumlah'].append({
            "Type" : "Menabung",
            "Nama" : nama,
            "Jumlah" : jumlah
        })
        st.success("anda berhasil menabung")
    else :
        st.error("anda gagal menabung")
