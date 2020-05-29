import pandas as pd

df = pd.read_pickle('data/combined.pkl')
df.to_csv('data/combined.csv')

