import streamlit as st
from read_webp import convert_webp
import json

with open('content.json', 'r') as file:
    content = json.load(file)

col1, col2 = st.columns(2)
with col1:
    st.title('Inevitable Elephant')
with col2:
    st.write('01012003')

for i in content:
    image = convert_webp(i['image'])
    st.image(image,width=500)
    st.write(i['content'])