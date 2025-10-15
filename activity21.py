import random

print("guess the number")
print("-----------------------")

random_val = random.randint(1,10)

tries = 0
go = True

name = input(" enter your name ...")

while go == True:
    num = eval(input(" enter the number (1-10) --> "))
    tries += 1
    if num == random_val:
        print("correct !!1")
        break
    else:
        print("incorecct !!")
        continue

print(f"hi {name} you num is correct , your number of try is {tries}")
