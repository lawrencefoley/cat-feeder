from utils import feed
import schedule
from time import sleep
import logging
from gpiozero import LED

# Set this number to the number of quarter cups you want your pet fed for each meal
# By default, I have two meals per day
NUMBER_OF_QUARTER_CUPS_PER_FEEDING = 1

VERSION = "0.0.3"
CAT_ART ="""
    _                ___       _.--.
    \`.|\..----...-'`   `-._.-'_.-'`
    /  ' `         ,       __.--'
    )/' _/     \   `-_,   /
    `-'" `"\_  ,_.-;_.-\_ ',
        _.-'_./   {_.'   ; /
       {_.-``-'         {_/
"""

if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(filename='cat-feeder.log', level=logging.INFO, format='%(asctime)s | %(module)s | %(message)s')
    logging.info("Cat Feeder - " + VERSION)
    logging.info(CAT_ART)
    logging.info("Starting up...")

    # Blinking LED to indicate normal operation
    led = LED(4)
    led.blink(on_time=0.05, off_time=3, n=None, background=True)

    # Morning feeding
    schedule.every().day.at("08:00").do(feed, quarterCups=NUMBER_OF_QUARTER_CUPS_PER_FEEDING)

    # Evening feeding
    schedule.every().day.at("20:00").do(feed, quarterCups=NUMBER_OF_QUARTER_CUPS_PER_FEEDING)
    
    # Run scheduled feedings
    while True:
        schedule.run_pending()
        sleep(1)
