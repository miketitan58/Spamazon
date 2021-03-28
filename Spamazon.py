# Amazon Review Web Scraper Version 1.01
#
# "Spamazon Scrapers"
# Paul O'bar, Dylan Manuel, Michael Stepp, Aaron Brown
# 

import requests
from bs4 import BeautifulSoup
import json
import os
import cleanup
import starSum
import graph
import URLCleanup
import math as m
from datetime import datetime as dt
# Usage
# python3 Collection.py

# Scrape all Reviews on page, deposit reviews into reviewList
def probeReviews(reviews):
    for item in reviews:
        if len(reviewList) == reviewsToScrape:
            break
        title=""
        try:
            reviewRating = int(item.find('i', {'data-hook': 'review-star-rating'}).text.strip()[:1])
        except:
            reviewRating = int(item.find('i', {'data-hook': 'cmps-review-star-rating'}).text.strip()[:1])
        try:
            title = item.find('a', {'data-hook': 'review-title'}).text.strip()
        except:
            try:
                title = item.find('span', {'data-hook': 'review-title'}).text.strip()
            except:
                title = item.find('span', {'class': 'cr-original-review-content'}).text.strip()

        review = {
            'date': dt.strptime(cleanup.preprocess(item.find('span', {'data-hook': 'review-date'}).text.strip()).replace(" ", "-"), '%Y-%m-%d'),
            'rating': reviewRating,
            'title': title
        }
        reviewList.append(review)
        
    print("\""+review['title']+"\"")

# User pasts in their Amazon URL, if a valid ID cant be found we'll print an error and exit the program
uncleanURL = input("Please paste your Amazon URL and press enter: ")
itemID = URLCleanup.cleanURL(uncleanURL)
if itemID == 'ID Scrape Error':
    print("This URL is not valid!")
    quit()
#topURL = 'https://www.amazon.com/product-reviews/'+itemID+'/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=helpful&pageNumber=1'
recentURL = 'https://www.amazon.com/product-reviews/'+itemID + \
    '/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1'
url = recentURL
r = requests.get('http://localhost:8050/render.html',
                 params={'url': url, 'wait': 1})
mySoup = BeautifulSoup(r.text, 'html.parser')


# We print out product name along with total plottable reviews
print("\nProduct :", mySoup.title.text.replace(
    "Amazon.com: Customer reviews: ", "").strip()+"\n")
totalReviewsText = mySoup.find(
    'div', {'data-hook': 'cr-filter-info-review-rating-count'}).text.strip()
totalReviews = totalReviewsText.split(' ')
totalReviews = totalReviews[4].replace(',', '')
print("Total plottable reviews ", totalReviews)

# This while loop locks the user in a input loop so that they enter valid data
# If the user wishes to not plot a given graph they can enter n, relooping them alowing them to enter a new scraping value
while True:
    try:
        print()
        reviewsToScrape = int(
            input("How many reviews would you like to plot (1-"+totalReviews+"): "))
        if reviewsToScrape != 0 and reviewsToScrape <= int(totalReviews):
            seconds = (reviewsToScrape/10)*2
            minutes = seconds // 60
            seconds %= 60
            print("Approximate time to plot", reviewsToScrape, "Reviews is", minutes, "minutes", round(seconds,2), "seconds")
            choice = input("Would you like to begin? (y/n): ").lower()
            if choice.startswith('y'):
                break
    except ValueError:
        print("Please enter a valid integer! (1-"+totalReviews+")")

# get next button URL
short = mySoup.find('li', {'class': 'a-last'}).find("a", href=True)["href"]
reviewList = []
# Walk through pages using the next button's URL to jump to the next page
while len(reviewList) < reviewsToScrape:
    r = requests.get('http://localhost:8050/render.html',
                     params={'url': url, 'wait': 1})
    mySoup = BeautifulSoup(r.text, 'html.parser')
    reviews = mySoup.find_all('div', {'data-hook': 'review'})
    probeReviews(reviews)
    if mySoup.find('li', {'class': 'a-disabled a-last'}):
        break
    short = mySoup.find('li', {'class': 'a-last'}).find("a", href=True)["href"]
    url = 'https://www.amazon.com'+(short)

# Create MasterList, print length of list, then plot MasterList
masterList = starSum.sumRatings(reviewList)
print("Reviews Collected =", len(reviewList))
graph.plotReviewOverTime(masterList)
