# Import the RGBLED component
from picozero import RGBLED, Button, LED, run
from uasyncio import sleep

# Set up RGBLED with correct pin numbers
rgb = RGBLED(red=1, green=2, blue=3)
button2 = Button(22)
led = LED(13)
button1 = Button(18)
button3 = Button(28)

rgb.off()

async def lighting():
    print("Lighting effects!")
    print("Blinking")
    rgb.blink()
    await sleep(6)
    rgb.pulse() # start pulsing    
    await sleep(8)
    rgb.cycle()
    await sleep(6)
    rgb.off()
    print("Finished")

async def light_on_timer():
    print("On")
    led.on()
    await sleep(3)
    led.off()
    print("Off")
    
async def cancel_rgb():
    button2.cancel() # prevent new sequences
    rgb.off() # stops running sequences
    
button1.when_pressed = light_on_timer
button2.when_pressed = lighting
button3.when_pressed = cancel_rgb

print("Ready")

run()
