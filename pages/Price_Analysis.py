import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Neerds Gunpla Prices", layout="wide")

st.title('Gunpla Price Analysis')

df = pd.read_csv('data/combined_gunpla_data.csv')

df['price_clean'] = df['price'].str.replace('¥', '').str.replace(',', '').replace('N/A', pd.NA)
df['price_clean'] = pd.to_numeric(df['price_clean'], errors='coerce')

st.subheader('Average Price by Grade')
avg_price = df.groupby('name')['price_clean'].mean().sort_values(ascending=False)
st.bar_chart(avg_price, x_label='Grades', y_label='Average Price (¥)')