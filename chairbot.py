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
        try:
            print("Checking last " + str(settings.NUM_RESULTS) + " cheap listings")
            scraper.scrapeCheap()
            time.sleep(15) # just trying to avoid anything that might get me rate limited
            print("Checking last " + str(settings.NUM_RESULTS) + " size C listings")
            scraper.scrapeSizeC()
            time.sleep(SCRAPE_INTERVAL)
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished scraping".format(time.ctime()))

