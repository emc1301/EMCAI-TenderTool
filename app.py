import streamlit as st
import pandas as pd

st.set_page_config(page_title = "EMCAI")
st.header ("EMCAI Review Tool")
st.write("🏗️ Please upload your tender and our tool will do the rest 🏗️")

upload = st.file_uploader(label='')
    
if upload:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(upload)
    
    # Calculate the expected total cost
    df['calculated total'] = df['count'] * df['cost']

    # Check if the calculated total matches the provided total
    df['discrepancy'] = df['total'] != df['calculated total']

    # Display the full DataFrame
    st.dataframe(df)

    # Filter and display rows with discrepancies
    if df['discrepancy'].any():
        st.write("⚠️ Discrepancies found in the following rows:")
        st.dataframe(df[df['discrepancy']])
    else:
        st.write("✅ All totals are correct.")