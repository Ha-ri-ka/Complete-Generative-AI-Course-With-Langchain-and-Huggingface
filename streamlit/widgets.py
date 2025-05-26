import streamlit as st 
import pandas as pd

st.title("Widgets in streamlit")
name = st.text_input("First name:")

if name:
    st.write(f"hello {name}, how are you?")

experince = st.slider("How many years of experince do you have?",0,25,1)
st.write(f"wow! {experince} years? nice!")

options=["overnight oats","cereal","aloo paratha","idli sambhar"]
bfast=st.selectbox("What's your favourite breakfast?",options)
st.write(f"{bfast}, good choice!")

uploaded_file= st.file_uploader("Resume tiiiiimeeeee",type="pdf")
if uploaded_file:
    # st.write(uploaded_file)
    st.write("nice resume dawg")
