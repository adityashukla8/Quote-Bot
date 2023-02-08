import pandas as pd
import random
import firebase_admin as admin
from firebase_admin import credentials
from firebase_admin import db
from google.cloud import firestore
import streamlit as st
import dotenv
import os

import airtable

api_key = 'keyf0HCILmsc89SOu'
db_key = 'appimdoShD63eN3Zc'
table = 'Sheet1'
view = 'Grid view'

url = 'https://api.airtable.com/v0/appimdoShD63eN3Zc/Sheet1?api_key=' + api_key + '&offset=itrMhDF4VD1pxm7W2/rec0PDQhir08dBp1L'

res = requests.get(url)

# dotenv.load_dotenv()

# db = firestore.Client.from_service_account_json('quotes-904b2-firebase-adminsdk-vrxkf-36da48f48b.json')
# doc_ref = db.reference('', url='https://quotes-904b2-default-rtdb.firebaseio.com/')
# data = doc_ref.get()

# cred = credentials.Certificate('quotes-904b2-firebase-adminsdk-vrxkf-36da48f48b.json')
# admin.initialize_app(cred, name = "abcdefadsd")
# ref = db.reference('', url='https://quotes-904b2-default-rtdb.firebaseio.com/')

# data = ref.get()
# df = pd.DataFrame(data)

st.write("quotes")
