import streamlit as st
from st_files_connection import FilesConnection
import pandas as pd

st.set_page_config(
    page_title="Product",
    page_icon="👋",
)

st.title('Product Report')

# Create connection object and retrieve file contents.
conn = st.connection('s3', type=FilesConnection)

# Specify input format is a csv and to cache the result for 600 seconds.
df = conn.read("msawsbuckets3/supermarkt_sales.csv", input_format="csv", usecols=["Product line", "Branch", "Unit price"], ttl=600)

st.data_editor(df, use_container_width=True, hide_index=True)
#st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
#st.data_frame(df, use_container_width=True, hide_index=True)

# HIDE STREAMLIT STYLE
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)
