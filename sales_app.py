import streamlit as st
import pandas as pd

data = {
    "Product": ["Laptop", "Shirt", "Apple", "Orange", "Grapes","Sofa", "Cot","Headphones"],
    "Category": ["Electronics", "Clothing", "Groceries","Groceries","Groceries","Furniture","Furniture", "Electronics"],
    "Sales": [75000, 1500, 300, 200, 100, 25000, 8500, 5000]
}

df = pd.DataFrame(data)

st.title("Sales Dashboard")
st.subheader("This dashboard is about sales")

category = st.selectbox("Choose the category",df["Category"].unique())
category = st.sidebar.selectbox("Choose the category",df["Category"].unique())
filtered = df[df["Category"] == category]

st.dataframe(filtered)
st.subheader("Sales Trend")
chart_data = filtered.set_index("Product")
st.line_chart(chart_data["Sales"])

