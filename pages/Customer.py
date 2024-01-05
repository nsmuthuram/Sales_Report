import streamlit as st
from st_files_connection import FilesConnection
import pandas as pd



st.set_page_config(
    page_title="Customer",
    page_icon="👋",
)


st.title('Customer Report')


df= pd.read_excel(
      io='supermarkt_sales.xlsx',
      #engine='openpyxl',
      sheet_name='Sales',
      skiprows=3,
      usecols='E, F, D',
      nrows=1000,
    )



st.dataframe(   df
            )

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('s3', type=FilesConnection)
df1 = conn.read("msawsbuckets3/supermarkt_sales.csv", input_format="csv", ttl=600)


# Print results.
for row in df1.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")

# HIDE STREAMLIT STYLE
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)
