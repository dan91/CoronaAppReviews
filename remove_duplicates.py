from os import listdir
from os.path import isfile, join
import pandas as pd
import json

# we get the reviews from the app store in files of 500 each, every hour. this script removes the overlapping (= duplicate) reviews 

mypath  = 'data/seafile_download'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

dfs = []
for f in files:
    print(f)
    with open('data/seafile_download/' + f) as json_file:
        data = json.load(json_file)
        reviews = []
        for r in data:
            for r2 in r:
                # while we're at it, also remove other unnecessary fields
                del r2['updated_parsed'], r2['link'], r2['guidislink'], r2['title_detail'], r2['content'], r2['im_contenttype'], r2['authors'], r2['author_detail'], r2['href'], r2['links']
                reviews.append(r2)
    curr_df = pd.DataFrame(reviews)
    dfs.append(curr_df)

con = pd.concat(dfs)
print(con.columns)

# some AppStore duplicate reviews have different IDs, that's why duplicates are now detected by date and text
con = con.drop_duplicates(subset=['updated', 'summary']).sort_values('updated')
con.reset_index(inplace=True)
con.to_json('data/appStoreReviews.json')
