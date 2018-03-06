import pandas as pd

df1 = pd.DataFrame({
    'HPI':[80,85,88,85],
    'Int_rate':[2,3,2,2],
    'US_GDP_THousands':[50,55,65,55]},
    index=[2001,2002,2003,2004])

df2 = pd.DataFrame({
    'HPI':[80,85,88,85],
    'Int_rate':[2,3,2,2],
    'US_GDP_THousands':[50,55,65,55]},
    index=[2005,2006,2007,2008])

df3 = pd.DataFrame({
    'HPI':[80,85,88,85],
    'Int_rate':[2,3,2,2],
    'Low_tier_HPI':[50,55,65,55]},
    index=[2001,2002,2003,2004])

s = pd.Series([80,2,50], index = ['HPI','Int_rate','US_GDP_THousands'])
df5 = df1.append(s,ignore_index = True)
print(df5)

df4 = df1.append(df2)
print(df4)

concat = pd.concat([df1,df2,df3])
print(concat)

