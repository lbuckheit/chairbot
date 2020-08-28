import time
import sys
import traceback

if __name__ == "__main__":
    while True:
        print("{}: Starting scrape cycle".format(time.ctime()))
        try:
            print('SCRAPING')
            time.sleep(2)
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished scraping".format(time.ctime()))
