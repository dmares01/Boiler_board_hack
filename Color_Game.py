"""start up code needed here"""
from boilerboard import Boilerboad
import time

b = Boilerboad()

"""Main starts here"""
wrong_press = 0
number_of_trials = 1
while number_of_trials < 16:
    random_number = 0
    user_input = 0

    import random

    for x in range(1):
        random_number = (random.randint(0, 9))

    if random_number == 0:
        b.screen.lcd.text("UP", 0, 0)

    if random_number == 1:
        b.screen.lcd.text("RIGHT", 0, 0)

    if random_number == 2:
        b.screen.lcd.text("DOWN", 0, 0)

    if random_number == 3:
        b.screen.lcd.text("LEFT", 0, 0)

    if random_number == 4:
        b.screen.lcd.text("Red", 0, 0)

    if random_number == 5:
        b.screen.lcd.text("B", 0, 0)

    if random_number == 6:
        b.screen.lcd.text("A", 0, 0)

    if random_number == 7:
        b.screen.lcd.text("Orange", 0, 0)

    if random_number == 8:
        b.screen.lcd.text("Green", 0, 0)

    if random_number == 9:
        b.screen.lcd.text("Blue", 0, 0)

    b.screen.lcd.show()
    "Get the user pressed Button"
    user_input = b.irq.get_pressed_button()

    """Now we check for validity"""
    if random_number == 0:
        if user_input == 0:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 1:
        if user_input == 1:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 2:
        if user_input == 2:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 3:
        if user_input == 3:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 4:
        if user_input == 5:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 5:
        if user_input == 5:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 6:
        if user_input == 6:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 7:
        if user_input == 0 or 2:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 8:
        if user_input == 6:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 9:
        if user_input == 1 or 3:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1
            """blank"""

    """\/This goes at the very end of the loop \/"""
    number_of_trials = number_of_trials + 1


print("Your score is ", (15-wrong_press), " out of 15")

