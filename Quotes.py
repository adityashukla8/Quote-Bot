import pandas as pd
import random
import firebase_admin as admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st
import dotenv
import os

dotenv.load_dotenv()

cred = os.environ.get("creds")
# cred = credentials.Certificate("D:\Aditya\data\Quotes\quotes-904b2-firebase-adminsdk-vrxkf-36da48f48b.json")
if not firebase_admin._apps:
    admin.initialize_app(cred)
    ref = db.reference('', url='https://quotes-904b2-default-rtdb.firebaseio.com/')
else:
    ref = db.reference('', app=firebase_admin.get_app())

data = ref.get()
df = pd.DataFrame(data)

st.write("quotes")
