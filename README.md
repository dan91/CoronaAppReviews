# CoronaAppReviews
Analysing Corona App reviews from the Play Store and App Store. 


RKI Website: https://corona-datenspende.de

App Store: https://apps.apple.com/de/app/corona-datenspende/id1504705422

Play Store: https://play.google.com/store/apps/details?id=de.rki.coronadatenspende

## View the reviews
Check out googlePlayReviews.csv in the data folder. The CSV is currently only available for Play Store reviews.

## View the notebook
Open NLP.ipynb on Github.

## Run the notebook
Install Jupyter and run
    
    jupyter notebook
    
## Scraping the data
Run the scripts in the folder 'scraper' to get the latest data:
    
    python appstorescraper.py
    
    python playscraper.py

Note that we can only retrieve that newest 500 reviews from the App Store, but all reviews from Google Play.

## Make a CSV file to open data in Excel etc.
This takes all the Play Store reviews from the .json file and puts them into a .csv file.
    
    python make_csv.py
