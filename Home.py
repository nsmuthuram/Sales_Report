import streamlit as st


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

def main ():

    st.write("# Welcome to Reports HomePage!!! ")

    #Btn_2  = st.button("Customer", type = "primary")
    #Btn_3  = st.button("Products", type = "primary")
    #Btn_1  = st.button("Sales", type = "primary")

# HIDE STREAMLIT STYLE
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

    


#########################-------------------------------------------------------------------------------------#########################

main ()