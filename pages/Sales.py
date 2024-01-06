import streamlit as st
from st_files_connection import FilesConnection
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title=":bar_chart: Sales Dashboard",
    page_icon=":bar_chart:",
)

st.title('Sales Report')

# Create connection object and retrieve file contents.
conn = st.connection('s3', type=FilesConnection)

# Specify input format is a csv and to cache the result for 600 seconds.
df = conn.read("msawsbuckets3/supermarkt_sales.csv", input_format="csv", ttl=600)

# SIDEBAR
st.sidebar.header("Please Filter Here:")

var_city= st.sidebar.multiselect(
  "Select the City:",
  options=df["City"].unique(),
  default=df["City"].unique()
)

var_customer_type= st.sidebar.multiselect(
  "Select the Customer Type:",
  options=df["Customer_type"].unique(),
  default=df["Customer_type"].unique()
)

var_gender= st.sidebar.multiselect(
  "Select the Gender:",
  options=df["Gender"].unique(),
  default=df["Gender"].unique()
)

df_selection=df.query(
  "City== @var_city & Customer_type== @var_customer_type & Gender == @var_gender"
)

# TOP KPI's
total_sales= int(df_selection["Total"].sum())
average_rating =round(df_selection["Rating"].mean(),1)
star_rating=":star:" * int(round(average_rating,0))
average_sale_by_transaction=round(df_selection["Total"].mean(),2)


# KPI's COLUMNS
left_column,middle_column,right_column=st.columns(3)


with left_column:
  st.subheader("Total Sales:")
  st.subheader(f"US $ {total_sales:,}")
with middle_column:
  st.subheader("Average Rating:")
  st.subheader(f"{average_rating}")
  st.write(f"{star_rating}")
with right_column:
  st.subheader("Average Sales Per Transaction:")
  st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("---")

# BARCHARTS

# SALES BY PRODUCT LINE [BAR CHART]

sales_by_product_line=(
  #df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
  df_selection.groupby(["Product line"])[["Total"]].sum()
)

fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#6fa8dc"] * len(sales_by_product_line),
    template="plotly_white",
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# SALES BY HOUR [BAR CHART]

# Add 'hour' column to dataframe for second barchart
    #df["hour"]=pd.to_datetime(df["Time"],format="HH:MM:SS").dt.hour
    #return df

#sales_by_hour=df_selection.groupby(["hour"])[["Total"]].sum()



#fig_hourly_sales=px.bar(

#)


#fig_hourly_sales.update_layout(
 
 #)


# SALES BY PAYMENT [BAR CHART]

sales_by_payment=df_selection.groupby(["Payment"])[["Total"]].sum()

fig_payment_sales=px.bar(
    sales_by_payment,
    x=sales_by_payment.index,
    y="Total",
    title="<b>Sales by Payment</b>",
    color_discrete_sequence=["#6fa8dc"] * len(sales_by_payment),
    template="plotly_white",
)


# Displaying charts
left_column,right_column=st.columns(2)
left_column.plotly_chart(fig_product_sales,use_container_width=True)
#right_column.plotly_chart(fig_hourly_sales,use_container_width=True)
right_column.plotly_chart(fig_payment_sales,use_container_width=True)


# HIDE STREAMLIT STYLE
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)
