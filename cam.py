import streamlit as st


t = st.text_input("Enter the age")

if t:
    try:
        t = int(t)  
        if t <18:
            st.error("FBI open up!!!")
            st.camera_input("open the damn door")
        elif t >= 18:
            st.success("good to go")
       
        print(t)
    except ValueError:
        st.error("Please enter a valid age")