import pymongo
import twitch_hearthstone_scrape.ipynb

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.hearthstone

#twitch data web scrape
collection = db.twitch_data
collection.insert_many(twitch_stats)

#tempo storm data web scrape
collection = db.tempo_data
collection.insert_many(tier_one_decks)

#hearthstone json api
collection = db.card_info
collection.insert_many(decks_with_cards)



print("Data Uploaded!")
