import streamlit as st
import requests

def get_moisture():
    response = requests.get("http://127.0.0.1:5000/get")
    st.write(response.json())

def set_target(level):
    print(level)
    response = requests.post(f"http://127.0.0.1:5000/set/{level}")
    st.write(response.json()) 

st.button("View Moisture Level", on_click=get_moisture);

target = st.text_input("Target Moisture Level")
set_click = st.button("Set Target Moisture Level")
if set_click:
    print(target)
    set_target(target)