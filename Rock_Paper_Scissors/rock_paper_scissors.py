import random

choices = ['rock' , 'paper' , 'scissors']

player_score = 0
cpu_score = 0

while True:

    cpu_input = random.choice(choices)

    user_input = input('Choose one of Rock, Paper or Scissors: ')

    if user_input.lower() not in choices:
        print("Enter a valid choice from Rock, Paper, Scissors")

    if user_input == 'end':
        break

    if user_input.lower() == cpu_input: print ("It is a TIE")

    elif user_input.lower() == 'rock':
        if cpu_input == 'scissors': 
            print("Scissors , You win this round")
            player_score+=1
        else:
            print("Paper , the CPU wins")
            cpu_score += 1

    elif user_input.lower() == 'paper':
        if cpu_input == 'rock':
            print("Rock, you win this round")
            player_score +=1
        else:
            print("Scissors, the CPU wins")
            cpu_score += 1
    
    elif user_input.lower() == "scissors":
        if cpu_input =="paper":
            print("Paper, you win this round")
            player_score+=1
        else:
            print("Rock, the CPU wins")
            cpu_score+=1

print(f"Your score is {player_score}, and the computer's score is {cpu_score}")



    