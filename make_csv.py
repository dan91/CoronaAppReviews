import pandas as pd
import json

df = pd.read_json('data/googlePlayReviews.json')
df.to_csv('data/googlePlayReviews.csv')

