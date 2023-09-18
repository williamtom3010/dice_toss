import random

def roll_dice():

    roll = random.randint(1, 6)
    return roll

N = int(input("How many dice do you want to roll?"))
outcome = []
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0

for i in range(N):

    output = roll_dice()
    if output == 1:
        count_1 +=1
    elif output == 2:
        count_2 +=1
    elif output == 3:
        count_3 +=1
    elif output == 4:
        count_4 +=1
    elif output == 5:
        count_5 +=1
    elif output == 6:
        count_6 +=1

    outcome.append(output)


print(outcome)

print("The occurence of face 1",count_1)
print("The occurence of face 2",count_2)
print("The occurence of face 3",count_3)
print("The occurence of face 4",count_4)
print("The occurence of face 5",count_5)
print("The occurence of face 6",count_6)
