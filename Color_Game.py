"""start up code needed here"""
print("Hello World")
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
        print("UP")

    if random_number == 1:
        print("RIGHT")

    if random_number == 2:
        print("DOWN")

    if random_number == 3:
        print("LEFT")

    if random_number == 4:
        print("Red")

    if random_number == 5:
        print("B")

    if random_number == 6:
        print("A")

    if random_number == 7:
        print("Orange")

    if random_number == 8:
        print("Green")

    if random_number == 9:
        print("Blue")

    user_input = 0
    """Need the users input = user_input"""

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
    print(number_of_trials)
    number_of_trials = number_of_trials + 1


print("Your score is ", (15-wrong_press), " out of 15")

