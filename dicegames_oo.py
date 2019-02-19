#dice game OOP version

from random import randint

#Player class
class Player:
	#constructor
	def __init__(self, number):
		self.number = number
		self.total_scores = 0
	
	#get total score
	def get_total_scores(self):
		return self.total_scores
	
	#add score to total
	def add_score(self, score):
		self.total_scores = self.total_scores + score
		
	#get number
	def get_number(self):
		return self.number
	
#Dice class
class Dice:
	
	#constructor
	def __init__(self, num_sides):
		self.num_sides = num_sides
		
	#get total score
	def roll(self):
		 return randint(1, self.num_sides)

#Pig game
class PigGame:
	
	 #constructor
	def __init__(self, win_scores):
		self.win_scores = win_scores
		self.dice = Dice(6)
		self.first_player = Player(1)
		self.second_player = Player(2)
		self.current_turn = self.first_player
	#
	# player plays one turn
	# input: player number
	# return the turn points
	#
	def take_turn(self):
		#turn points 
		turn_points = 0
		
		#rolling flag 
		rolling_flag = 1

		print ("==================================================")
		print ("Player " + str(self.current_turn.get_number()) + " press enter to begin your turn.")

		#wait for the enter key to be pressed
		input("")

		#while the user can and wants to keep rolling
		while rolling_flag == 1:
			#roll
			value = self.dice.roll()
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
	def play(self):

		#run until win scores
		while self.first_player.get_total_scores() < self.win_scores and self.second_player.get_total_scores() < self.win_scores:
			
			#take turn
			turn_scores = self.take_turn()

			self.current_turn.add_score(turn_scores)
			print ("Total point is " + str(self.current_turn.get_total_scores()))
			
			#swap turn
			if self.current_turn == self.first_player:
				self.current_turn = self.second_player
			else:
				self.current_turn = self.first_player #swap turn
			print()	
			
		if self.first_player.get_total_scores() >= self.win_scores:
			print ("Congratulation. The player 1 won. The score is " + str(self.first_player.get_total_scores()))
		else:
			print ("Congratulation. The player 2 won. The score is " + str(self.second_player.get_total_scores()))

#Fifty game
class FiftyGame:
	
	 #constructor
	def __init__(self, win_scores):
		self.win_scores = win_scores
		self.dice1 = Dice(6)
		self.dice2 = Dice(6)
		self.first_player = Player(1)
		self.second_player = Player(2)
		self.current_turn = self.first_player
	#
	# player plays one turn
	# input: player number
	# return the turn points
	#
	def take_turn(self):
		
		#turn points 
		turn_points = 0


		print ("==================================================")
		print ("Player " + str(self.current_turn.get_number()) + " press enter to begin your turn.")

		#wait for the enter key to be pressed
		input("")

		#roll
		value1 = self.dice1.roll()
		value2 = self.dice2.roll()
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
	# play pig game
	# 2 players take turn to play pig game until
	# win_scores scores archived
	def play(self):

		#run until win scores
		while self.first_player.get_total_scores() < self.win_scores and self.second_player.get_total_scores() < self.win_scores:
			
			#take turn
			turn_scores = self.take_turn()

			self.current_turn.add_score(turn_scores)
			print ("Total point is " + str(self.current_turn.get_total_scores()))
			
			#swap turn
			if self.current_turn == self.first_player:
				self.current_turn = self.second_player
			else:
				self.current_turn = self.first_player #swap turn
			print()	
			
		if self.first_player.get_total_scores() >= self.win_scores:
			print ("Congratulation. The player 1 won. The score is " + str(self.first_player.get_total_scores()))
		else:
			print ("Congratulation. The player 2 won. The score is " + str(self.second_player.get_total_scores()))
		print()
		
#main function displays menu for user to choose a game to play
if __name__ == "__main__":
	
	#define constants
	win_scores_pig = 10 #win scores in pig game
	win_scores_fifty = 10 #win scores in fifty game
	
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
			game = FiftyGame(win_scores_fifty)
			game.play();
		elif str(choice) == "2":
			game = PigGame(win_scores_pig)
			game.play();
		elif str(choice) == "0":
			pass
		else:
			print ("Invalid choice")
		print("")	
	#good bye
	print ("Thank you for using the program")
