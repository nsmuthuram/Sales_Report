import streamlit as st
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



st.dataframe(   df,
             column_order=("Product line", "Branch", "Unit price"),
            )

# HIDE STREAMLIT STYLE
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)
