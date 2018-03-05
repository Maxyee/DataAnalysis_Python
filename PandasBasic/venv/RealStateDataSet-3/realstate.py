# import Quandl
import pandas as pd

api_key = open('quandlapikey.txt','r').read()
df = Quandl.get('ZILLOW/S2_ZRIAH',authtoken=api_key)
print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#this is a list:
print(fiddy_states[0])

# this is a dataframe:
print(fiddy_states[0][0])

