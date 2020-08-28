from slackeventsapi import SlackEventAdapter
from craigslist import CraigslistForSale
from slack import WebClient
import settings
import sqlite3
import os

# POC For testing a manually triggered scrape
# NOT USED AT PRESENT

# Create the SlackClient
slack_bot_token = settings.slack_bot_token
slack_client = WebClient(slack_bot_token)

# For receiving actions via the Events API
# NOT USED AT PRESENT
slack_signing_secret = settings.slack_signing_secret
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

@slack_events_adapter.on("message")
def handle_message(event_data):
    con = sqlite3.connect('./data/chairbot.db')
    cursor = con.cursor()
    query = "SELECT * FROM listing_history;"
    last_message = str(cursor.execute(query).fetchall())

    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "chairbot engage" in message.get('text'):
        cl_fs = CraigslistForSale(site='newyork', filters={'query': 'aeron', 'max_price': settings.MAX_PRICE, 'min_price': settings.MIN_PRICE})
        messages = []
        for result in cl_fs.get_results(sort_by='newest', limit=settings.NUM_RESULTS):
            messages.append(result['price'] + ' --- ' + result['url'])

        channel = message["channel"]
        message = str(messages)

        formatted_message = "[('" + message.replace("'", "") + "',)]"
        print(formatted_message)
        print(last_message)
        print(formatted_message != last_message)
        if formatted_message != last_message:
            delete_query = 'DELETE FROM listing_history;'
            cursor.execute(delete_query)
            update_query = "INSERT INTO listing_history('lastfive') values('" + message.replace("'", "") + "');"
            cursor.execute(update_query)
            con.commit()
            slack_client.chat_postMessage(channel=channel, text=message)

    cursor.close()