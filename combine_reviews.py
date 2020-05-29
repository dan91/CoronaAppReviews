import pandas as pd

# this script combines reviews from PlayStore and AppStore

appStoreReviews = pd.read_json('data/appStoreReviews.json')
playStoreReviews = pd.read_json('data/googlePlayReviews.json')

appStoreReviews.rename(columns = {'updated': 'date', 'summary': 'content', 'im_rating': 'score', 'im_version': 'version'}, inplace=True)
playStoreReviews.rename(columns = {'userName': 'author', 'at': 'date', 'reviewCreatedVersion': 'version'}, inplace=True)

appStoreReviews['source'] = 'AppStore'
playStoreReviews['source'] = 'PlayStore'
combined = pd.concat([appStoreReviews, playStoreReviews])

combined.to_pickle('data/combined.pkl')
