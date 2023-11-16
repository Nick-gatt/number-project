def player_guess():
    check = False
    while check == False:
        guess = input("Give a number between 1 and 100\n")
        if guess.isdigit:
            if int(guess) >= 1 and int(guess) <= 100:
                guess = int(guess)
                check = True
    return guess

def give_feedback(secret_number, guess):
    if guess > secret_number:
        print("guess is larger than number")
        return 1
    elif guess < secret_number:
        print("guess is less than number")
        return 1
    elif guess == secret_number:
        print("Correct!!!!")
        return 0
    else:
        print("if you get this result a critical error occured")