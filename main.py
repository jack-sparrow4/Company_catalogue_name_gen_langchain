import streamlit as st
from brand_flavour_name_idea_generation import gen_name_catalog

st.title("Catalogue generator")

sector = st.sidebar.selectbox("Pick an Industry", ("Beverage", "Packaged food", "Breakfast food", "Bakery", "Diary food"))

if sector:
    response = gen_name_catalog(sector)
    st.header(response['company_name'].strip())
    menu_items = response['catalogue'].strip().split(",")
    st.write("**Product catalogue**")
    for item in menu_items:
        st.write("-", item)
