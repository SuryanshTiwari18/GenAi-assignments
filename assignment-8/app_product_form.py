import streamlit as st 

st.title("Product Form")

name = st.sidebar.text_input("Product Name")
category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Food", "Other"])
price = st.sidebar.number_input("Price", min_value=0.0)

if st.sidebar.button("Add Product"):
    st.success("Product added successfully!")

    st.write("### Product Details")
    st.write(f"Name: {name}")
    st.write(f"Category: {category}")
    st.write(f"Price: ${price:.2f}")