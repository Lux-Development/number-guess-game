import random
import os 

os.system("title joelb.services")

lowest_num = int(input("Enter lowest number: "))
highest_num = int(input("Enter highest number: "))

num_final = random.randint(lowest_num, highest_num)

while True:
    guess = int(input("Enter your guess: "))

    if guess == num_final:
        print("Correct")
        break
    elif guess > num_final:
        print("Incorrect! (Hint: It's lower)")
    else:
        print("Incorrect! (Hint: It's higher)")

os.system("pause")