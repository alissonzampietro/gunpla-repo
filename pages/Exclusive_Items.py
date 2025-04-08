import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('data/combined_gunpla_data.csv').drop(['createdAt','updatedAt_x','infoId','createAt','updatedAt_y', 'description'], axis=1)
df = df.groupby('exclusive').size()

labels = {
    True: 'Exclusive',
    False: 'Non-Exclusive'
}
df = df.rename(index=labels)

st.title('Gunpla Exclusive Analysis')

fig, ax = plt.subplots()
ax.pie(df, labels=df.index, autopct='%1.1f%%', startangle=100, radius=1)
ax.set_title('Gunpla Exclusive Distribution')

st.pyplot(fig)