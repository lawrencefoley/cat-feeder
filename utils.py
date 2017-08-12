from gpiozero import OutputDevice, Buzzer, PWMLED, LED
from time import sleep
import logging
import sys
import os

motor = OutputDevice(2)
buzzer = Buzzer(3)
cameraLight = LED(26)
DEBUG = False

def takePicture():
    """
    Takes a picture of the food bowl using a web cam to make sure it's feeding the cat the correct amount
    """
    # Turn on white LED to illuminate up the bowl
    cameraLight.on()
    # Saved to a directory which is viewable via nginx
    os.system('fswebcam -r 640x480 -p YUYV -S 3 --jpeg 50 --save /home/cat/cat-feeder/html/%Y-%m-%d_%H-%M-%S.jpg')
    cameraLight.off()

def feed(quarterCups):
    logging.info("Feeding " + str(quarterCups) + " quarter cups")
    # Create Pavlov response to beep
    beep()
    # Dispense each quarter cup of food
    for i in range(1, quarterCups + 1):
        try:
            if not DEBUG:
                motor.on()
	        # 2.867 seconds is the theoretical time (1/6th of a rotation at 3.5 rpm)
                # In reality it takes a little time for the motor to begin turning
                sleep(2.9)
            if not DEBUG:
                motor.off()
        except KeyboardInterrupt:
            motor.off()
            motor.close()
        # Pause between quarter cups for accurate measurments
        if i != quarterCups:
            sleep(0.5)
    logging.info("Taking picture")
    takePicture()


def beep():
    buzzer.beep(0.2, 0.2, 3, background=False)

if __name__ == "__main__":
    feed(1)
