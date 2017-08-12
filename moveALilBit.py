from gpiozero import OutputDevice
from time import sleep

motor = OutputDevice(2)

# Moves the motor a small amount to adjust it before running the feeder app
def move():
    try:
        motor.on()
        sleep(0.2)
        motor.off()
    except KeyboardInterrupt:
        motor.off()
        motor.close()

if __name__ == "__main__":
    move()
