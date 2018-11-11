from boilerboard import Boilerboard
import time
import urandom


b = Boilerboard()
b.screen.lcd.text("Welcome to the", 0, 0)
b.screen.lcd.text("Color Game", 0, 15)
b.screen.lcd.text("Created by SK", 0, 35)
b.screen.lcd.text("and DM", 0, 50)
b.screen.lcd.show()
time.sleep(1)
b.screen.lcd.fill(0)
b.screen.lcd.text("Press the button", 0, 0)
b.screen.lcd.text("that appears on", 0, 15)
b.screen.lcd.text("screen", 30, 30)
b.screen.lcd.show()
time.sleep(2)
b.screen.lcd.fill(0)
time_start = time.time()
wrong_press = 0
number_of_trials = 1
while number_of_trials < 16:
    b.screen.lcd.text("Round", 20, 0)
    b.screen.lcd.text(str(number_of_trials), 25, 10)
    b.screen.show()
    time.sleep(.5)
    b.screen.lcd.fill(0)
    b.screen.show()
    time.sleep(.5)
    random_number = urandom.getrandbits(10)
    random_number = random_number % 10

    if random_number == 0:

        b.screen.lcd.text("UP", 40, 20)

    if random_number == 1:
        b.screen.lcd.text("RIGHT", 40, 20)

    if random_number == 2:
        b.screen.lcd.text("DOWN", 40, 20)

    if random_number == 3:
        b.screen.lcd.text("LEFT", 40, 20)


    if random_number == 4:
        b.screen.lcd.text("Red", 40, 20)

    if random_number == 5:
        b.screen.lcd.text("B", 40, 20)

    if random_number == 6:
        b.screen.lcd.text("A", 40, 20)

    if random_number == 7:
        b.screen.lcd.text("Orange", 40, 20)

    if random_number == 8:
        b.screen.lcd.text("Green", 40, 20)

    if random_number == 9:
        b.screen.lcd.text("Blue", 40, 20)

    b.screen.lcd.show()
   
    """"print("Button Pushed")"""
    "print(str(user_input))"
    print("random number is ", random_number)
    print("Number of wrong presses = ", wrong_press)
    """Time to enter response"""
    time.sleep(1)
    user_input = b.irq.get_pressed_button()
    """Now we check for validity"""
    if user_input is None:
        user_input = 100
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
        if user_input == 0:

            """do nothing"""
        elif user_input == 2:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 8:
        if user_input == 6:
            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    if random_number == 9:
        if user_input == 1:


            """do nothing"""
        elif user_input == 3:

            """do nothing"""
        else:
            wrong_press = wrong_press + 1

    b.screen.lcd.fill(0)
    b.screen.show()
    time.sleep(.5)
    number_of_trials = number_of_trials + 1

time_end = time.time()
print(time_start)
print(time_end)
time_score = (time_end - time_start)
button = None
while button is None:
    b.screen.lcd.fill(0)
    b.screen.lcd.text("Your score is ", 0, 0)
    b.screen.lcd.text(str(15-wrong_press), 0, 20)
    b.screen.lcd.text("out of 15", 0, 40)
    b.screen.show()
    time.sleep(1)
    b.screen.lcd.fill(0)
    b.screen.lcd.text("Your time is", 0, 0)
    b.screen.lcd.text(str(time_score), 0, 20)
    b.screen.lcd.text("seconds", 0, 40)
    b.screen.show()
    time.sleep(1)
    button = b.irq.get_pressed_button()
b.screen.lcd.fill(0)
b.screen.lcd.text("Game Over", 30, 30)
b.screen.show()



