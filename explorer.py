print("--exercise 1--")
import pandas as pd
df = pd.read_csv('data/retail_sales.csv') 
print(df.head())
print(df.tail())

print("--exercise 2--")
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

print("--exercise 3--")
print(df.sort_values('revenue', ascending=False).head(5))

print("--exercise 4--")
big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(len(big_south))
print(big_south.head())

print("--exercise 5--")
df['per_unit'] = df['revenue'] / df['quantity']
print(df['per_unit'].head())
print(df['per_unit'].mean())

print("--exercise 6--")
print(df['region'].unique())
print(df['region'].value_counts())
print("--exercise 7--")
subset = df[['region', 'revenue', 'quantity']]
print(subset.shape)
print("--exercise 8--")
df.to_csv('data/explored.csv', index=False)

#reflection questions
#1. A bollean filter only includes rows that meet the condition provided.
#2. df['revenue'] creates a series and df[['revenue']] creates a dataframe. This matters because a series is a single column of data while a dataframe is a two-dimensional table of data.
#3. It is much faster to use pandas than to manually filter through data in excel.
