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
import requests

api_key = 'keyf0HCILmsc89SOu'
db_key = 'appimdoShD63eN3Zc'
table = 'Sheet1'
view = 'Grid view'

authors = ['Richard P. Feynman', 'Leo Tolstoy']
current_auth = None
current_quotes = None

current_author = random.choice(authors)
# generate the URL based on the current author
url = 'https://api.airtable.com/v0/appimdoShD63eN3Zc/Sheet1?api_key=' + api_key + "&filterByFormula=author='" + current_author + "'"

# make the API request
response = requests.get(url)
data = response.json()

quotes = [record['fields']['quote'] for record in data['records']]
quote = random.choice(quotes)

def get_quote:
  st.write(quote)
  st.write(current_author)

if st.button('Generate More'):
  get_quote()
