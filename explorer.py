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