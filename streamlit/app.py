import streamlit as st
import pandas as pd 
import numpy as np 

#title
st.title("Hello streamlit")

#write some text
st.write("This is text.")

df = pd.DataFrame({
    "col 1": [1,2,3,4],
    "col 2": ["one","two","three","four"]
})
st.write("Your dataframe:")
st.write(df)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)