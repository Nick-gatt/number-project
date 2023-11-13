def logic(number):
    check = False
    attempt = 0
    won = False
    while attempt != 3 and won == False:
        while check == False:
            guess = input("Give a number between 1 and 100\n")
            if guess.isdigit and len(guess) < 4:
                guess = int(guess)
                check = True
        if guess > number:
            print("guess is larger than number")
            attempt += 1
        elif guess < number:
            print("guess is less than number")
            attempt += 1
        elif guess == number:
            print("Correct!!!!")
            won = True
        else:
            print("if you get this result a critical error occured")
        check = False
