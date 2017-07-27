from gpiozero import OutputDevice, Buzzer, LED
from time import sleep

motor = OutputDevice(2)
buzzer = Buzzer(3)
led = LED(4)
def feed(quarterCups):
    try:
        motor.on()
	# 2.867 seconds is the theoretical time
        # sleep(2.857)
        sleep(2.9)
        motor.off()
    except KeyboardInterrupt:
        motor.off()
        motor.close()

def beep():
    buzzer.beep(0.2, 0.2, 3, background=False)

def blink():
    led.blink(n=3)
    
if __name__ == "__main__":
    feed(1)
