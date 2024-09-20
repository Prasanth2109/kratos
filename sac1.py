import streamlit as st
from streamlit_custom_toggle import st_custom_toggle


st.button("i love you")
st_custom_toggle('Active', active_track_fill="#FF5733", active_thumb_color="#900C3F", key="toggle2")
st.balloons()