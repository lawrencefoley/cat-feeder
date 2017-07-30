from utils import feed
import schedule
from time import sleep
import logging

if __name__ == "__main__":
    logging.basicConfig(filename='cat-feeder.log', level=logging.INFO, format='%(asctime)s | %(module)s | %(message)s')
    logging.info("Starting up...")

    # Morning
    schedule.every().day.at("09:00").do(feed, quarterCups=1)

    # Evening
    schedule.every().day.at("22:45").do(feed, quarterCups=1)

    #schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        sleep(1)
