import random
num = random.randint(1,100)

tries = 0

while True:
    guess = int(input("Guess the no.\n"))
    tries+=1

    if num == guess:
        print(f"Congratulation! Perfect guess in {tries} tries\n")
        break
    elif guess < num:
        print("Try again! Go upper\n")
    elif guess > num:
            print("Try again! Go lower\n")