# ETL-Project
hearthstone twitch viewership (Scrape found in twitch_hearthstone_scrape)

In this project I aimed to pair Twitch viewship data with data on most popular deck at a specific time. 

I had three sources for this data, a web scrape of twitch hearthstone statistics, a web scrape of the best deck of the week from the website Tempostorm, and a Hearthstone API that held all the card information.

The Twitch viewship data would relate to the most popular deck on the month category. The most popular deck would relate to  the card data on its deck_list (a list with each unique card within the deck). In this way I hoped to create a database that could be used to analyze if certain deck archytypes, classes, or cards might have an affect on the twitch viewership.

To scrape through the twitch stats was a simple iteration through a table on a single page. The scraping of the best performing deck was a bit harder, as I needed to iterate through many pages of archived articles that discussed the best decks of the week. The hearthstone API was easy to query against, as it was one long list of dictionaries, with each dictionary being one specific card from the game.



