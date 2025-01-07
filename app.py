import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load your data and similarity matrices
electronics = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommendation(product):
    electronics_index = electronics[electronics['name'] == product].index[0]
    similarity_list = list(enumerate(similarity[electronics_index]))
    top_10_similar_product = sorted(similarity_list, key=lambda x: x[1], reverse=True)[1:11]
    
    similar_product = []
    for idx, similar_score in top_10_similar_product:
        product_info = {
            'name': electronics.loc[idx]['name'],
            'image': electronics.loc[idx]['image'],
        }
        similar_product.append(product_info)
    return similar_product

# Apply custom CSS for styling
st.markdown("""
    <style>
    /* Title box styling */
    .title-box {
        background-color: #f7f7f7;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
    }
    /* Center the search button */
    .search-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 12px;
        color: #808080;
        font-family: 'Arial', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Title with box styling
st.markdown("<div class='title-box'><h1>Product Search Engine Using Python</h1></div>", unsafe_allow_html=True)

# Product selection
product_name = st.selectbox('Select a product:', electronics['name'])

# Center the search button
st.markdown("<div class='search-button'>", unsafe_allow_html=True)
if st.button('Search'):
    st.markdown("</div>", unsafe_allow_html=True)  # Close the div for the search button
    search_product = recommendation(product_name)
    st.write(f"### Top 10 Recommendations for **{product_name}**")

    # Display products in a clean, professional format
    for rec in search_product:
        st.image(rec['image'], width=150)
        st.write(f"**{rec['name']}**")

# Footer
st.markdown("<div class='footer'>Developed by <b>Asmita Chavan</b></div>", unsafe_allow_html=True)

