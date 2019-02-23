import random

# variables to keep track of # of wins
user_wins = 0
computer_wins = 0

while user_wins < 3 and computer_wins < 3:

	# get user's choice
	user_choice = raw_input("Rock, paper or scissors?") 

	# get computer's random choice
	computer_choice = random.randint(1,3)

	# 1 = rock, 2 = paper, 3 = scissors 
	computer_word = ""
	if computer_choice == 1:
		computer_word = "rock"
	elif computer_choice == 2:
		computer_word = "paper"
	elif computer_choice == 3:
		computer_word = "scissors"

	# determine winner!
	if user_choice == "rock" and computer_word == "paper":
		print("computer wins!")
		computer_wins = computer_wins + 1
	elif user_choice == "rock" and computer_choice == "rock":
		print("tie!")
	elif user_choice == "rock" and computer_choice == "scissors":
		print("user wins!")
		user_wins = user_wins + 1
	elif user_choice == "paper" and computer_choice == "rock":
		print("user wins!")
		user_wins = user_wins + 1 
	elif user_choice == "paper" and computer_choice == "paper":
		print("tie")
	elif user_choice == "paper" and computer_choice == "scissors":
		print("computer wins!")
		computer_wins = computer_wins + 1
	elif user_choice == "scissors" and computer_choice == "rock":
		print("computer wins!")
		computer_wins = computer_wins + 1
	elif user_choice == "scissors" and computer_choice == "paper":
		print("user wins!")
		user_wins = User_wins + 1
	elif user_choice == "scissors" and computer_choice == "scissors":
		print("tie!")
	else:
		print("invalid input")
		
			