secret_num = 7
tries = 0
max_trial = 3
while tries < max_trial:
    guess = int(input("Guess any number between 0 and 10: "))
    tries += 1
    if guess != secret_num:
        print("Wrong!  Try Again")
    if guess == secret_num: 
        print("You got it!")
        break
if tries == max_trial and guess != secret_num:
    print("Out of entry!, Secret is", secret_num)