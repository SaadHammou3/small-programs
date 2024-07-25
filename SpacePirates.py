# A fun, but ultimately failed experiment. 



import time
import os
import msvcrt

# get the character typed by the player for movement

def getch():
	return msvcrt.getch()

# the player

player = "                                          -^-"

# welcome message
welcome = """  

			    		      # ========== ~ ~ ~ ~ ~ ~ ========= #
				            		SPACE PIRATES !	

				            	  programmed by Saad Hammou	 


				            	  press 'D' to play!

				            	 	CONTROLS:
				            	'Q' = left
				            	'D' = right
				            	'Z' = shoot

				           	to pause, simply stop pushing buttons.

				           	THE GAME LOOPS TO INFINITY!

				
				
"""
story = """ 
THE STORY : 
2280 A.D. The golden age of space exploration is here! and with it a new golden age of piracy. Equipped with the most powerful
weapon in the universe, with the ability to destory entire rows of pirate spaceships, you set out to free the galaxy of the
pirate menace once and for all...
"""

# counter for how many move commands have been issued

move_count = 20

# empty string for input

direction = ""

# the row of pirates

pirate = "=(P)  "

# counter is set to 40 to start at the middle of the screen

counter = 10

# game speed, for dictating how fast the pirates move across the screen, the lower the number, the faster they move.

game_speed = 0.21

# turn counter one turn depends on the speed of the game
looping_num = 6

turn = 0

dead_pirates = 0
# Welcoming the dear player

print(welcome)
print(story)


# PHASE ONE : Top of the screen, low speed

while True:
	if dead_pirates > 3:
		print("More pirates!!")
		time.sleep(1)

		looping_num = 6
		dead_pirates = 1
		counter = 15
	turn += 1
	counter += 1
	pushed_row = " "  * counter + pirate + "\n"
	new_row = " " * counter + pirate 
	direction = getch().decode("utf-8")
	if direction.lower() == "d":
		print("Turn: " + str(turn))
		move_count += 1
		space = "\n \n \n \n \n \n \n \n" + " " * move_count + player
		print(space, end="\r", flush= False)
	elif direction.lower() == "q":
		print("Turn: " + str(turn))
		move_count -= 1
		space = "\n \n \n \n \n \n \n \n" + " " * move_count + player
		print(space, end="\r", flush= False)
	elif direction.lower() == "z":
		if move_count - counter <= 3:
			dead_pirates += 1
			space = "\n \n \n \n \n \n \n \n" + " " * move_count + player
			print(space, end="\r", flush= False)
		else:
			print("  " * 2  + "MISS!")
			space = "\n \n \n \n \n \n \n \n" + " " * move_count + player
			print(space, end="\r", flush= False)
	time.sleep(game_speed)
	direction = getch().decode("utf-8")
	if direction.lower() == "d":
		print("Turn: " + str(turn))
		move_count += 1
		space = "\n \n \n \n \n \n \n \n" + " " * move_count + player
		print(space, end="\r", flush= False)
	elif direction.lower() == "q":
		print("Turn: " + str(turn))
		move_count -= 1
		space = "\n \n \n \n \n \n \n \n" + " " * move_count + player
		print(space, end="\r", flush= False)
	elif direction.lower() == "z":
		if move_count - counter <= 3:
			dead_pirates += 1
			space = "\n \n \n \n \n \n \n \n" + " " * move_count + player
			print(space, end="\r", flush= False)
		else:
			print("MISS!")
			space = "\n \n \n \n \n \n \n \n" + " " * move_count + player
			print(space, end="\r", flush= False)
	os.system('cls')
	for rows in range(6):
			print(new_row + pirate * (looping_num - dead_pirates) )
