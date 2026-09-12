import streamlit as st

st.set_page_config(
    page_title="IPL Analytics",
    page_icon="🏏",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("IPL Analytics")
st.subheader("Login / Sign In")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "250200078" and password == "1234":
        st.session_state.logged_in = True
        st.success("Login successful!")

        st.switch_page("pages/1_About_Project.py")
    else:
        st.error("Invalid username or password.")