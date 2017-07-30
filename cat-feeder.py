from utils import feed
import schedule
from time import sleep
import logging
from gpiozero import PWMLED

if __name__ == "__main__":
    logging.basicConfig(filename='cat-feeder.log', level=logging.INFO, format='%(asctime)s | %(module)s | %(message)s')
    logging.info("Starting up...")

    led = PWMLED(4)
    led.blink(on_time=0, off_time=5, fade_in_time=0.25, fade_out_time=0.25, n=None, background=True)

    # Morning
    schedule.every().day.at("09:00").do(feed, quarterCups=1)

    # Evening
    schedule.every().day.at("22:45").do(feed, quarterCups=1)

    #schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        sleep(1)
