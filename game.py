import random

def main():
    play_game()

def play_game():
    want_game = input("Would you like to play the number guessing game\n").lower()
    if want_game == "yes":
        random_number = generate_random_number()
        attempt = 0
        while attempt != 3:
            guess = player_guess()           
            feedback = give_feedback(random_number, guess)
            if feedback == 1:
                attempt += 1
            elif feedback == 0:
                break
            else:
                print('something went wrong')
        print(f"The number was {random_number}. \nYou made {attempt + 1} attempts")
    want_game = input('Would you like to play again\n').lower()
    if want_game == "yes":
        play_game()



def generate_random_number():
    return random.randint(1, 100)



def player_guess():
    check = False
    while check == False:
        guess = input("Give a number between 1 and 100\n")
        if guess.isdigit():
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

    

if __name__ == "__main__":
    main()
    
