secret_num = 9

guess_count = 0 #the conditionn which we give to while loop saying till its true
guess_limit = 3
while (guess_count < guess_limit):
    Guess_num = int(input("Guess the number: "))
    if Guess_num != secret_num :
        print("Wrong Guess")
        guess_count += 1
        print(f"You have only {guess_limit-guess_count} chance left")

        continue
    elif Guess_num == secret_num :
        guess_count += 1
        print("You guessed it right")
        #print(f"You guessed in [{i}] chance")
        break
    else:
        print("Game over!")


