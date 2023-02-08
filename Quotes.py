import pandas as pd
import random
import firebase_admin as admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st
import dotenv
import os

dotenv.load_dotenv()

cred = os.environ.get("cred")
admin.initialize_app(cred)
ref = db.reference('', url='https://quotes-904b2-default-rtdb.firebaseio.com/')

data = ref.get()
# df = pd.DataFrame(data)

st.write("quotes")
