import pymongo
import scrape 

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.hearthstone

#twitch data web scrape
collection = db.twitch_data
collection.insert_many(scrape.twitch_stats)

#tempo storm data web scrape
collection = db.tempo_data
collection.insert_many(scrape.tier_one_decks)

#hearthstone json api
collection = db.card_info
collection.insert_many(scrape.decks_with_cards)



print("Data Uploaded!")
