import streamlit as st
import pandas as pd
import numpy as np 

## Title of the application
st.title("Hello Streamlit")

## Display a simple text
st.write("This is a simple,text")

## create a simple DataFrame

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}) 

## Display a dataframe
st.write("Here is the DataFrame")
st.write(df)


## create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)