from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import time

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)

url = 'https://twitchtracker.com/games/138585'

response = requests.get(url)

soup = bs(response.text, 'html.parser')

results = soup.find_all('tr')[1:28]
print(len(results))

twitch_stats = []

for result in results:
    # Splinter can capture a page's underlying html and use pass it to BeautifulSoup to allow us to scrape the content
    html = browser.html
    soup = bs(html, 'html.parser')
    # Error handling
    try:
        
        month = result.find_all('td')[0].text.strip()
        avg_view = result.find_all('td')[1].text
        avg_chan = result.find_all('td')[2].text
        peak_view = result.find_all('td')[3].text
        peak_chan = result.find_all('td')[4].text
        hours_watch = result.find_all('td')[5].text
        
        twitch_stats.append({"month":month, 
                             "avg_view":avg_view, 
                             "avg_chan":avg_chan, 
                             "peak_view":peak_view, 
                             "peak_chan":peak_chan, 
                             "hours_watch":hours_watch})

            
      
            
    except AttributeError as e:
        print(e)

browser.quit

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)

url = 'https://tempostorm.com/hearthstone/meta-snapshot/standard/2019-02-18'

browser.visit(url)

time.sleep(2)
html = browser.html
soup = bs(html, 'html.parser')

results = soup.find_all('h3', class_='ng-binding')

tier_one_decks = []

for x in range(20):   
    time.sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')
    
    results = soup.find_all('h3', class_='ng-binding')
    tier1 = results[10].text.replace('1. ','')
    
    if tier1 == 'Tier 1':
        tier1 = results[11].text.replace('1. ','')
        
    print(browser.url)
    base_link = browser.url
    print(tier1)
    links_found = soup.find_all('a', class_='big-view-deck-link pull-left ng-binding')
    link = "https://tempostorm.com" + links_found[0]['href']
    
    browser.visit(link)
    print(browser.url)
    time.sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')
    
    
    results2 = soup.find_all('div', class_='db-deck-card-name ng-binding')
    results2 = set(results2)
    deck_list = []
    for result in results2:
        deck_list.append(result.text)
    
    browser.visit(base_link)
    tier_one_decks.append({"deck":tier1,"deck_list":deck_list ,"date":browser.url.replace('https://tempostorm.com/hearthstone/meta-snapshot/standard/','')})

    time.sleep(2)
    button = browser.find_by_css('.btn-pagination-arrow.m-r-xs')    
    button.click()

browser.quit


response =  requests.get("https://api.hearthstonejson.com/v1/28855/enUS/cards.collectible.json")

card_data = response.json()

decks_with_cards = []
for x in range(len(tier_one_decks)):
    
    deck = tier_one_decks[x]['deck']
    
    deck_builder = []
    for card_item in tier_one_decks[x]["deck_list"]:
        deck_builder.append(list(filter(lambda card: card['name']==card_item,card_data)))
        
    decks_with_cards.append({"deck":deck,
                            "card_info":deck_builder})    
    