from craigslist import CraigslistForSale
from slack import WebClient
import sqlite3
import settings
import os

# Create the SlackClient
slack_bot_token = settings.slack_bot_token
slack_client = WebClient(slack_bot_token)

# Scrape function to be run at set intervals
def scrape():
    # Post a message to the general channel just to confirm it's still running
    slack_client.chat_postMessage(channel='general', text='scraping')

    con = sqlite3.connect('./data/chairbot.db')
    cursor = con.cursor()
    query = "SELECT * FROM listing_history;"
    last_message = str(cursor.execute(query).fetchall())

    cl_fs = CraigslistForSale(site='newyork', filters={'query': 'aeron', 'max_price': settings.MAX_PRICE, 'min_price': settings.MIN_PRICE})
    messages = []
    for result in cl_fs.get_results(sort_by='newest', limit=settings.NUM_RESULTS):
        messages.append(result['price'] + ' --- ' + result['url'])

    message = str(messages)

    formatted_message = "[('" + message.replace("'", "") + "',)]"
    print("New listings?")
    print(formatted_message != last_message)
    if formatted_message != last_message:
        delete_query = 'DELETE FROM listing_history;'
        cursor.execute(delete_query)
        update_query = "INSERT INTO listing_history('lastfive') values('" + message.replace("'", "") + "');"
        cursor.execute(update_query)
        con.commit() # Important to commit changes to the DB
        slack_client.chat_postMessage(channel=settings.CHANNEL, text=message)

    cursor.close()