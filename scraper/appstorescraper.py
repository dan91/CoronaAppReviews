import json
import feedparser
import time
import os

def collect_reviews(entries, page = 1):
    feed = feedparser.parse("http://itunes.apple.com/DE/rss/customerreviews/id=1504705422/page={}/sortby=mostrecent/xml".format(page))
    new_entries = feed.entries
    entries.append(new_entries)
    if(page == 10):
        return entries
    else:
        collect_reviews(entries, page + 1)

entries = []
collect_reviews(entries)

# timestr = time.strftime("%Y%m%d-%H%M%S")
# path = '../data/AppStore/' + timestr + '.json'
path_latest = '../data/appStoreReviews.json'
# with open(path, 'w') as outfile:
#     json.dump(entries, outfile)
with open(path_latest, 'w') as outfile:
    json.dump(entries, outfile)
