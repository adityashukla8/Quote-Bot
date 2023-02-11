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

st.button('HOLA')
