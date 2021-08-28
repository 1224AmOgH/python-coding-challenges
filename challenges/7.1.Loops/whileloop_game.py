secret_no=7
guess_limit =3
guess_no=0
while guess_no<= guess_limit:
    guess = int(input("Guess: "))
    guess_no += 1
    if guess == secret_no:
        print("You Won!!!")
        break

else:
    print("Hard Luck try again")