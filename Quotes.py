#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scrapereads import GoodReads
import random
import pandas as pd

goodreads = GoodReads()

quotes = goodreads.search_quotes(34583, top_k=5)
st.write(quotes)

