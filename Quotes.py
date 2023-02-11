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
current_quotes = None

current_author = random.choice(authors)

while True:
    # generate the URL based on the current author
    url = 'https://api.airtable.com/v0/appimdoShD63eN3Zc/Sheet1?api_key=' + api_key + "&filterByFormula=author='" + current_author + "'"
    
    # make the API request
    response = requests.get(url)
    data = response.json()
    
    # get a random quote from the response
    quotes = [record['fields']['quote'] for record in data['records']]
    quote = random.choice(quotes)
    st.write(quote)
    st.write(current_author)
    
    # ask the user if they want to change the author
    change_author = input("Change author? y/n: ")
    if st.button('Change Author'):
        current_author = random.choice(authors)
    elif st.button('Generate More'):
        continue
    else:
        break
