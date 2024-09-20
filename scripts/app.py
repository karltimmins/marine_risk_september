import streamlit as st
import pandas as pd

st.write("Gen AI Marine Risk Assessment:")


# Declare a form and call methods directly on the returned object
form = st.form(key='my_form')
route = form.text_input(label='Shipping Route')
cargo = form.text_input(label='Cargo for Journey')
value = form.text_input(label='Value of Cargo')

submit = submit_button = form.form_submit_button(label='Submit')

if submit:
    st.write(f'route: {route}')
    st.write(f'cargo: {cargo}')
    st.write(f'risk: {value}')
    st.write(pd.DataFrame({
    'route': [route, 2, 3, 4],
    'cargo': [cargo, 20, 30, 40],
    'risk': [value, 20, 30, 40],
}))