import pandas as pd
import random
import firebase_admin as admin
from firebase_admin import credentials
from firebase_admin import db
from google.cloud import firestore
import streamlit as st
import dotenv
import os
import requests
import json
import airtable
import random

api_key = 'keyf0HCILmsc89SOu'
db_key = 'appimdoShD63eN3Zc'
table = 'Sheet1'
view = 'Grid view'

# url = 'https://api.airtable.com/v0/appimdoShD63eN3Zc/Sheet1?api_key=' + api_key + '&offset=itrMhDF4VD1pxm7W2/rec0PDQhir08dBp1L'

# res = requests.get(url)

import random
import requests
import streamlit as st

authors = ['Richard P. Feynman', 'Leo Tolstoy']

def get_record(author):
    url = 'https://api.airtable.com/v0/appimdoShD63eN3Zc/Sheet1?api_key=' + api_key + "&filterByFormula=author='" + author + "'"
    response = requests.get(url)
    data = response.json()
    records = data['records']
    return random.choice(records)

def main():
    st.title("Author Random Record Generator")

    current_author = st.sidebar.selectbox("Select an author", authors, key='unique_author_selectbox')
    st.write("Current author:", current_author)

    record = get_record(current_author)
    st.write("Record:", record)

    if st.button("Generate More"):
        record = get_record(current_author)
        st.write("Record:", record)

    if st.sidebar.button("Change Author"):
        current_author = st.sidebar.selectbox("Select an author", authors, key='unique_author_selectbox')
        st.write("Current author:", current_author)
        record = get_record(current_author)
        st.write("Record:", record)

if __name__ == "__main__":
    main()
