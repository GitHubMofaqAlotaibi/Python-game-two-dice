from random import randint

#roll a die
#input: number of sides on the die
#return: random integer that is at least 1 and no more than the number of sides
def roll_die(num_sides):
	return randint(1,num_sides)

#
# player plays one turn
# input: player number
# return the turn points
#
def take_turn_pig_game(player):
	#turn points 
	turn_points = 0
	#rolling flag 
	rolling_flag = 1
	
	print ("==================================================")
	print ("Player " + str(player) + " press enter to begin your turn.")
	
	#wait for the enter key to be pressed
	input("")
	
	#while the user can and wants to keep rolling
	while rolling_flag == 1:
		#roll
		value = roll_die(6)
		print ("You rolled a " + str(value))
		
		#if the roll was a 1, set turn points to 0 and exit
		if value == 1:
			turn_points = 0
			rolling_flag = 0
			print ("Turn over.")
		else:
			turn_points = turn_points + value
			print ("Your turn points are now " + str(turn_points) + ".")
			
			#ask the user if they want to continue
			asking = input(("Continue rolling (0=no,1=yes)? "))
			if asking == "0":
				rolling_flag = 0
				print ("Turn over.")
			else:
				print ("")
	print ("==================================================")
	return turn_points

#
# play pig game
# 2 players take turn to play pig game until
# win_scores scores archived
def play_pig_game(win_scores):
	first_score = 0
	second_score = 0
	current_turn = 1
	
	#run until win scores
	while first_score < win_scores and second_score < win_scores:
		#take turn
		turn_scores = take_turn_pig_game(current_turn)
		
		if current_turn == 1:
			first_score = first_score + turn_scores
			print ("Total point is " + str(first_score))
			current_turn = 2 #swap turn
		else:
			second_score = second_score + turn_scores
			print ("Total point is " + str(second_score))
			current_turn = 1 #swap turn
		print()	
	if first_score >= win_scores:
		print ("Congratulation. The player 1 won. The score is " + str(first_score))
	else:
		print ("Congratulation. The player 2 won. The score is " + str(second_score))
	print()
	

#
# player plays one turn
# input: player number
# return the turn points
#
def take_turn_fifty_game(player):
	#turn points 
	turn_points = 0
	
	print ("==================================================")
	print ("Player " + str(player) + " press enter to begin your turn.")
	
	#wait for the enter key to be pressed
	input("")
	#roll
	value1 = roll_die(6)
	value2 = roll_die(6)
	print ("You rolled a " + str(value1) + " and a " + str(value2))

	#if the roll was a 1, set turn points to 0 and exit
	if value1 == value2:
		turn_points = 0
		if value1 == 6:
			turn_points = 25
		elif value1 == 3:
			turn_points = 0
		else:
			turn_points = 5
	
	print ("==================================================")
	
	return turn_points

#
# play fifty game
# 2 players take turn to play fifty game until
# win_scores scores archived
def play_fifty_game(win_scores):
	first_score = 0
	second_score = 0
	current_turn = 1
	
	#run until win scores
	while first_score < win_scores and second_score < win_scores:
		
		#take turn
		turn_scores = take_turn_fifty_game(current_turn)
		
		if current_turn == 1:
			first_score = first_score + turn_scores
			print ("Total point is " + str(first_score))
			current_turn = 2 #swap turn
		else:
			second_score = second_score + turn_scores
			print ("Total point is " + str(second_score))
			current_turn = 1 #swap turn
		print()	
	if first_score >= win_scores:
		print ("Congratulation. The player 1 won. The score is " + str(first_score))
	else:
		print ("Congratulation. The player 2 won. The score is " + str(second_score))
	print()
	
#main function displays menu for user to choose a game to play
if __name__ == "__main__":
	
	#define constants
	win_scores_pig = 100 #win scores in pig game
	win_scores_fifty = 50 #win scores in fifty game
	
	choice = "1"
	
	#run until user wants to exit
	while (str(choice) != "0"):
		
		#display menu
		print("Mofaq Alotaibi_April 07,2017_Programming Languages_524-02")
		print("Welcome to dice games")	
		print("You can play Fifty or Pig")	
		print("Fifty: You need to reach 50 points to win")	
		print("All doubles except 3s and 6s score 5 points.")
		print("Double 6s are worth 25 points.")
		print("Double 3s wipe out the player's entire score, and the player must start again at 0.")
		print("Non-double rolls are 0 points")
		print("Pig: You need to reach 50 points to win")	
		print("You can roll the die as many times")
		print("The value of each throw is added to the current player's score")
		print("If the player rolls a 1, the player's score goes back to 0, and the turn ends.")
		print("You can choose the game from the following menu to continue")
		print("")
		print("1. Fifty game")
		print("2. Pig game")
		print("0. Quit")
		choice = input("Your choice? ")
 
		if str(choice) == "1":
			play_fifty_game(win_scores_fifty)
		elif str(choice) == "2":
			play_pig_game(win_scores_pig)
		elif str(choice) == "0":
			pass
		else:
			print ("Invalid choice")
		print("")	
	#good bye
	print ("Thank you for using the program")
