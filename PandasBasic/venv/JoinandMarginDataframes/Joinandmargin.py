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
    'Unemployment':[7,8,9,6],
    'Low_tier_HPI':[50,55,50,53]},
    index=[2001,2002,2003,2004])

df10 = pd.DataFrame({
    'Year':[2001,2002,2003,2004],
    'Int_rate':[2,3,2,2],
    'US_GDP_THousands':[50,55,65,55]})

df20 = pd.DataFrame({
    'Year':[2001,2003,2004,2005],
    'Int_rate':[2,3,2,2],
    'US_GDP_THousands':[50,55,65,55]})


df1.set_index('HPI',inplace=True)
df3.set_index('HPI',inplace=True)

joined = df1.join(df3)
print(joined)

merged = pd.merge(df10,df20, on = 'Year', how='left')
merged.set_index('Year',inplace=True)
merged1 = pd.merge(df10,df20, on = 'Year', how='right')
merged1.set_index('Year',inplace=True)
merged2 = pd.merge(df10,df20, on = 'Year', how='outer')
merged2.set_index('Year',inplace=True)
merged3 = pd.merge(df10,df20, on = 'Year', how='inner')
merged3.set_index('Year',inplace=True)


print(merged)
print(merged1)
print(merged2)
print(merged3)

# print(pd.merge(df1,df2, on=['HPI','Int_rate']))