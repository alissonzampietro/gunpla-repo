import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Neerds Gunpla Grades")

st.title('Neerds Gunpla Grades')

df = pd.read_csv('data/combined_gunpla_data.csv').drop(['createdAt','updatedAt_x','infoId','createAt','updatedAt_y', 'description'], axis=1)

df = df.groupby('slug_x').size().reset_index(name='count')

labels = {
    'slug_x': 'Grades',
    'count': 'Total Items',
    'master-grade': 'Master Grade',
    'real-grade': 'Real Grade',
    'super-deformed': 'Super Deformed',
    'high-grade': 'High Grade'
}
df = df.replace(labels)
grades = df['slug_x'].to_list()
counts = df['count'].to_list()

fig, ax = plt.subplots()
ax.pie(counts, labels=grades, autopct='%1.1f%%', startangle=190, radius=1)
ax.set_title('Gunpla Grades Distribution')

st.pyplot(fig)



st.write(df.rename(columns=labels))
# st.plotly_chart(df, use_container_width=True)

# st.dataframe(df)