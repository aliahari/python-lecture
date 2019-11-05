x = 37
maxGuess = 6
for i in range(maxGuess):
    guess = int(input("Enter a number:"))
    if x == guess:
        print("Congrats! You won")
        break
    elif i<5:
        remainingGuess = maxGuess - (i+1)
        print(f"You have  {remainingGuess} remaining guesses")
    elif i == 5:
        print("You lost")
