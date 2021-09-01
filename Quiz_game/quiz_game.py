def check_guess(guess,ans):

    global score
    score = 0
    still_guessing = True

    attempts = 1

    while still_guessing and attempts<=3:
        if guess.lower() == ans.lower():
            print("Correct")

            score=score+1

            still_guessing = False

        elif attempts <= 2:
            guess = input ("Incorrect answer, try again ")
            attempts+=1
        
        if attempts == 3:
            print("You have exhausted all yout attempts, the correct answer is ", ans)
            attempts +=1

    
print("Welcome to the guess the animal game!")

guess1 = input("Which country in North America has the largest land area? ")
check_guess(guess1,'Canada')

guess2 = input("Name Sony's latest gaming console ")
check_guess(guess2,"Playstation5")

guess3 = input("Which city in the US is famous for coffee and Starbucks? ")
check_guess(guess3,"Seattle")
