import time
import sys
import traceback
import settings
import scraper

# Start up and scrape at a given interval
SCRAPE_INTERVAL = settings.SCRAPE_INTERVAL_MINS * 60
if __name__ == "__main__":
    while True:
        print("{}: Starting scrape cycle".format(time.ctime()))
        print("Checking last " + str(settings.NUM_RESULTS) + " listings")
        try:
            scraper.scrape()
            time.sleep(SCRAPE_INTERVAL)
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished scraping".format(time.ctime()))

