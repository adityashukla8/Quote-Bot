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
current_auth = None

def main():
    st.write(authors)

# # def get_record(author):
# #     url = 'https://api.airtable.com/v0/appimdoShD63eN3Zc/Sheet1?api_key=' + api_key + "&filterByFormula=author='" + author + "'"
# #     response = requests.get(url)
# #     data = response.json()
# #     records = data['records']
# #     quote = random.choice(records)
# #     return quote['fields']['quote']

# # def change_author():
# #     global current_auth
# #     current_auth  = random.choice(authors)

# def generate_more(current_auth):
#     st.write("Current author:", current_auth)
    
#     url = 'https://api.airtable.com/v0/appimdoShD63eN3Zc/Sheet1?api_key=' + api_key + "&filterByFormula=author='" + current_auth + "'"
#     response = requests.get(url)
#     data = response.json()
#     records = data['records']
#     quote = random.choice(records)
    
#     record = quote['fields']['quote']
# #     get_record(current_auth)
#     st.write("Record:", record)


# def main():
# #     current_author = change_author()
#     current_auth  = random.choice(authors)
    
#     st.title("Author Random Record Generator")
#     st.write(current_auth)
    
#     if st.button("Generate More"):
#         generate_more(current_auth)

#     if st.button("Change Author"):
#         current_author = change_author()
#         generate_more(current_author)

if __name__ == "__main__":
    main()
