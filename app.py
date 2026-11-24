import streamlit as st
import pandas as pd
import time 

st.title('startup dashboard')
st.header("i am learning streamlit")
st.subheader('Salman khan')


st.write('this is a normal text')

st.markdown("""
-Cricket
-Code
-Coffee
"""
)
st.code("""

def square(input):
        return square**2
x = square(2)

""")
st.latex("x^2+y^2+z^2=2")

st.metric('Revenue', 'Rs 3L', '+3%')

bar = st.progress(0)

for i in range (1, 101):
    bar.progress(i)

st.balloons()