import pandas as pd
import random
from scrapereads import GoodReads
import streamlit as st

goodreads = GoodReads()

quotes = goodreads.search_quotes(34583, top_k=5)
st.write(quotes)
