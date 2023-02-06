import pandas as pd
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st

cred = credentials.Certificate("D:\Aditya\data\Quotes\quotes-904b2-firebase-adminsdk-vrxkf-36da48f48b.json")
admin.initialize_app(cred)
ref = db.reference('', url='https://quotes-904b2-default-rtdb.firebaseio.com/')

st.write("quotes")
