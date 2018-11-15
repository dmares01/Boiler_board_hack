from boilerboard import Boilerboard
import time
import urandom
from functions import *

b = Boilerboard()
button_press = None
b.screen.lcd.text("Welcome to the", 0, 0)
b.screen.lcd.text("Color Game", 25, 15)
b.screen.lcd.show()
time.sleep(1.5)
b.screen.lcd.fill(0)
b.screen.lcd.text("Press the button", 0, 0)
b.screen.lcd.text("that appears on", 0, 15)
b.screen.lcd.text("screen", 30, 30)
b.screen.lcd.show()
time.sleep(2)
while button_press is None:
    b.screen.lcd.fill(0)
    b.screen.lcd.text("Press any button", 0, 0)
    b.screen.lcd.text("to start", 0, 15)
    b.screen.lcd.show()
    button_press = b.irq.get_pressed_button()

b.screen.lcd.fill(0)
urandom.seed(time.time())
wrong_press = 0
number_of_trials = 1
time_score = 0
while number_of_trials < 16:
    b.screen.lcd.text("Round", 20, 0)
    b.screen.lcd.text(str(number_of_trials), 25, 10)
    b.screen.lcd.show()
    time.sleep(.5)
    b.screen.lcd.fill(0)
    b.screen.lcd.show()
    time.sleep(.5)
    #Create random number
    random_number = urandom.getrandbits(10)
    random_number = random_number % 10
    time_start = time.time()

    screen_info(random_number, b)
    user_input = None
    while user_input is None:
        user_input = b.irq.get_pressed_button()
    wrong_press = user_answer(user_input, random_number, wrong_press)

    time_end = time.time()
    time_score = time_score + (time_end - time_start)
    b.screen.lcd.fill(0)
    b.screen.lcd.show()
    time.sleep(.5)
    number_of_trials = number_of_trials + 1
    b.irq.clear_buffer()
button = None
b.irq.clear_buffer()
while button is None:
    b.screen.lcd.fill(0)
    b.screen.lcd.text("Your score is ", 0, 0)
    b.screen.lcd.text(str(15-wrong_press), 0, 20)
    b.screen.lcd.text("out of 15", 0, 40)
    b.screen.lcd.show()
    time.sleep(1)
    b.screen.lcd.fill(0)
    b.screen.lcd.text("Your time is", 0, 0)
    b.screen.lcd.text(str(time_score), 0, 20)
    b.screen.lcd.text("seconds", 0, 40)
    b.screen.lcd.show()
    time.sleep(1)
    button = b.irq.get_pressed_button()
b.screen.lcd.fill(0)
b.screen.lcd.text("Game Over", 30, 30)
b.screen.lcd.show()