# Project 9: Build a Python Website in 15 Minutes With Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Simple Data Dashboard')

uploaded_files = st.file_uploader("Upload Your CSV Files", type = 'csv')

if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    
    # Create a line chart for the first column
    st.subheader("Data Preview")
    st.write(df.head())
    
    # create a Summary Statistics section
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file upload...")