# Boiler Board Hack
#### Drew Mares & Soren Kremer

## Starting at Madhacks
Repository for the 2019 Spring Madhacks Hackathon. For this hackathon we created a project using the provided boiler boards, from one of the sponsors. These boards came with a small LCD screen and 6 buttons sodered on, as well as having the lower level coding done for us. For this project we used micropython and the hardware functionality contained in the boilerboard.py file that comes on each of the boards. 

Looking at these boards we decided we wanted to create some sort of game. We brainstormed a few ideas, but finally settled on a sort of simon says style of game. Each button has a different color, as well as a name. The 6 buttons were A, B, Left, Right, Up, Down. Using these different names and colors we had our idea. The game we created tested the users response time to prompts on screen. There would either be a name or a color that would be shown and the user must press the corresponding button. The user is timed for each press, and at the end of the game their total time is shown.  One of the issues we had with the game was we couldn't seed the random number generator based off of time since the device turned on, since it would take the same amount of time to reach the main menu each time. Our sneaky work around for this was to actually seed the number generator based off of how long it took the user to click start. Each user reads at a slightly different pace, maybe they turned the board on and got sidetracked talking before starting the game. It may not be perfect but it was the best way to randomize the prompts shown on screen.

## What have we done since?
Honestly we haven't done a whole lot with the Color Game since Madhacks. The game has not been improved or changed at all. Besides showing friends and family the game we created and having them play it, the game has sat idle. We both still have our boards and another simplified board we won from the competition as well, but they've stayed in there static proof bags collecting dust. 

## Where will we go? 
From here on out I, Drew, will probably be the only one updating this repo. From here on out unless otherwise stated any further changes or commits are from me and I hope to expand on this game. Make it a little more challanging. Possibly add in different levels or something similar. If I get ambitious I may try to add additional hardware to the board as well.
