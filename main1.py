import studentgrade
import pandas
import streamlit as st


studentgrade.print_mult_table(5, 20)



data = pandas.read_csv("products.csv")
# print(data)
# st.write(data)

st.title ("Dashboard")
st. write ("this application is abount displaying product sales")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Sales", "1,200", "12%")
with col2:
    st.metric("Revenue", "$ 50,000", "5%")
with col3:
    st.metric("User", "$ 15,000", "8%")



st.header ("Sales table")
st.subheader ("This is a sales table")
st.write (data)

st.line_chart(data["sales"])
if st.checkbox("Show table"):
    st.subheader("This is a table")
    st.write(data)