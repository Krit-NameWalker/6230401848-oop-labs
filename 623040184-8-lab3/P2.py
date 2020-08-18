turns = 3

for turns in range(turns-1, -1, -1):
    guess = input("Enter a word: ")
    if guess == "AWK":
        print("Congrats that you can guss the secret_word correctly")
        break
    else:
        print("Incorrect! You have", turns, "guesses left")
        print("Thank for trying, but the secret word is actually AWK")
