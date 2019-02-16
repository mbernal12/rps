import random

player = raw_input("rock, paper, or scissors?")

computer = random.randint(1,3)


for (int i = 1; i < 3; i++):
	print(i)



if (player == "rock" and computer == 3):
	print("player wins")
elif (player == "rock" and computer == 2):
	print("computer wins")
elif (player == "rock" and computer == 1):
	print("tie")
elif (player == "paper" and computer == 3):
	print("computer wins")
elif (player == "paper" and computer == 2):
	print("tie")
elif (player == "paper" and computer == 1):
	print("player wins")
elif (player == "scissors" and computer == 3):
	print("tie")
elif (player == "scissors" and computer == 2): 
	print("player wins")
elif (player == "scissors" and computeer == 1):
	print("computer wins")
else:
	print("invalid input")