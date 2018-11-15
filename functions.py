from boilerboard import Boilerboard


def screen_info(determiner, board):
    if determiner == 0:
        board.screen.lcd.text("Up", 40, 20)
    if determiner == 1:
        board.screen.lcd.text("Right", 40, 20)
    if determiner == 2:
        board.screen.lcd.text("Down", 40, 20)
    if determiner == 3:
        board.screen.lcd.text("Left", 40, 20)
    if determiner == 4:
        board.screen.lcd.text("Red", 40, 20)
    if determiner == 5:
        board.screen.lcd.text("B", 40, 20)
    if determiner == 6:
        board.screen.lcd.text("A", 40, 20)
    if determiner == 7:
        board.screen.lcd.text("Orange", 40, 20)
    if determiner == 8:
        board.screen.lcd.text("Green", 40, 20)
    if determiner == 9:
        board.screen.lcd.text("Blue", 40, 20)
    board.screen.lcd.show()


def user_answer(input, random_number, wrong_press):
    if random_number == 0:
        if input != 0:
            wrong_press = wrong_press + 1
    if random_number == 1:
        if input != 1:
            wrong_press = wrong_press + 1
    if random_number == 2:
        if input != 2:
            wrong_press = wrong_press + 1
    if random_number == 3:
        if input != 3:
            wrong_press = wrong_press + 1
    if random_number == 4:
        if input != 5:
            wrong_press = wrong_press + 1
    if random_number == 5:
        if input != 5:
            wrong_press = wrong_press + 1
    if random_number == 6:
        if input != 6:
            wrong_press = wrong_press + 1
    if random_number == 7:
        if input != 0 and input != 2:
            wrong_press = wrong_press + 1
    if random_number == 8:
        if input != 6:
            wrong_press = wrong_press + 1
    if random_number == 9:
        if input != 1 and input != 3:
            wrong_press = wrong_press + 1
    return wrong_press