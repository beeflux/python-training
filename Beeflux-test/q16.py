"""
Q16.
The birthday paradox says that the probability that two people in a room will have the same birthday 
is more than half, provided n, the number of people in the room, is more than 23. 
This property is not really a paradox, 
but many people find it surprising. Design a Python program that can 
test this paradox by a series of experiments on randomly generated birthdays, which test 
this paradox for n = 5,10,15,20,...,100
"""

from random import randint


def random_birthday_generator(n):
    #this function generates the birthday randomly in between the days [0,32]
    birthdays = []
    birthmonth = []
    for i in range(n):
        birth = randint(0,32)
        month = randint(0,13)
        birthdays.append(birth)
        birthmonth.append(month)
    return birthdays



def has_same_birthdays(birthdays):
    yes = len(birthdays) != len(set(birthdays)) 
    print(f"Checking for Same Birthdays in a room with students {len(birthdays)}")
    if yes:
        print("Has Same birthdays")
    else:
        print("Has not Same birthdays")

for i in range(1,101,5):
    birthdays = random_birthday_generator(i)
    has_same_birthdays(birthdays)