from google_play_scraper import Sort, reviews
import time, json, datetime

result = reviews(
    'de.rki.coronadatenspende',
    lang='de', # defaults to 'en'
    country='de', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    count=20000 # defaults to 100
)

# timestr = time.strftime("%Y%m%d-%H%M%S")
# path = '../data/GooglePlay/' + timestr + '.json'
path_latest = '../data/googlePlayReviews.json'
def format_date(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

# with open(path, 'w') as outfile:
#     json.dump(result, outfile, default=format_date)
with open(path_latest, 'w') as outfile:
    json.dump(result, outfile, default=format_date)
