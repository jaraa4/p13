import streamlit as st

#sidebar sirectory
dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title ="Nabung")
penarikan = st.Page("./fitur/penarikan.py", title="Penarikan")

pg = st.navigation(
    {
        "Menu Utama":[dashboard],
        "Nabung":[nabung],
        "Penarikan":[penarikan],
    }
)



if 'jumlah' not in st.session_state:
    st.session_state['jumlah'] = []

#menjalankan navigasi
pg.run()

    