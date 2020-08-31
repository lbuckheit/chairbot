from craigslist import CraigslistForSale
from slack import WebClient
import sqlite3
import settings
import os

# Create the SlackClient
slack_bot_token = settings.slack_bot_token
slack_client = WebClient(slack_bot_token)

# Scrape for cheap chairs
def scrapeCheap():
    # Post a message to the general channel just to confirm it's still running
    slack_client.chat_postMessage(channel='general', text='scraping cheap')

    con = sqlite3.connect('./data/chairbot.db')
    con.row_factory = lambda cursor, row: row[0]
    cursor = con.cursor()
    query = "SELECT last FROM cheap;"
    last_message = cursor.execute(query).fetchone()

    cl_fs = CraigslistForSale(site='newyork', filters={'query': 'aeron', 'max_price': settings.MAX_PRICE, 'min_price': settings.MIN_PRICE})
    messages = []
    for result in cl_fs.get_results(sort_by='newest', limit=settings.NUM_RESULTS):
        messages.append(result['price'] + ' - ' + result['url'])

    for message in messages:
        if 'humanscale' in message:
            messages.remove(message)
        if 'knoll' in message:
            messages.remove(message)

    message = "\n".join(messages)
    if not message:
        cursor.close()
        return
    if message != last_message:
        delete_query = 'DELETE FROM cheap;'
        cursor.execute(delete_query)
        update_query = "INSERT INTO cheap('last') values('" + message + "');"
        cursor.execute(update_query)
        con.commit() # Important to commit changes to the DB
        slack_client.chat_postMessage(channel='cheap', text=message)

    cursor.close()

# Scrape for size C chairs
def scrapeSizeC():
    # Post a message to the general channel just to confirm it's still running
    slack_client.chat_postMessage(channel='general', text='scraping size C')

    con = sqlite3.connect('./data/chairbot.db')
    con.row_factory = lambda cursor, row: row[0]
    cursor = con.cursor()
    query = "SELECT last FROM sizeC;"
    last_message = cursor.execute(query).fetchone()

    cl_fs = CraigslistForSale(site='newyork', filters={'query': 'aeron size', 'max_price': settings.MAX_PRICE_C, 'min_price': settings.MIN_PRICE})
    messages = []
    for result in cl_fs.get_results(sort_by='newest', limit=settings.NUM_RESULTS):
        messages.append(result['price'] + ' - ' + result['url'])

    for message in messages:
        if 'humanscale' in message:
            messages.remove(message)
        if 'knoll' in message:
            messages.remove(message)

    message = "\n".join(messages)
    if not message:
        cursor.close()
        return
    if message != last_message:
        delete_query = 'DELETE FROM sizeC;'
        cursor.execute(delete_query)
        update_query = "INSERT INTO cheap('last') values('" + message + "');"
        cursor.execute(update_query)
        con.commit() # Important to commit changes to the DB
        slack_client.chat_postMessage(channel='sizec', text=message)

    cursor.close()