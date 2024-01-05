import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Product",
    page_icon="👋",
)


st.title('Product Report')

df= pd.read_excel(
      io='supermarkt_sales.xlsx',
      #engine='openpyxl',
      sheet_name='Sales',
      skiprows=3,
      usecols='G, C, H',
      nrows=1000,
    )

st.dataframe(   df,
                #width = 200,
                use_container_width = True,
                #height = 1000,
                hide_index=True, 
                column_order=("Product line", "Branch", "Unit price"))

# HIDE STREAMLIT STYLE
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)