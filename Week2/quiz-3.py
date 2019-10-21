name = input("What is your name?\n")
print(f"Hello {name.upper()}")
guess = int(input("How many letters are in your name?\n"))
numLetter = len(name)
print(numLetter==guess)

