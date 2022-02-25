#(5 points): As a developer, I want to make at least three commits with descriptive messages.
#(5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.
#(5 points): As a user, I want a destination to be randomly selected for my day trip.
#(5 points): As a user, I want a restaurant to be randomly selected for my day trip.
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
#(10 points): As a user, I want to display my completed trip in the console.
#(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


import random
from tkinter.messagebox import NO, YES

answer = YES
answer = NO

destination = ['Australia', 'Bali', 'Mexico', 'Turkey']
transportation = [ 'Bus', 'plane', 'rocket', 'cruise ship']
restaurants = ['pizza shop', 'Italian restaurant', 'authentic mexican food truck', 'street meat vendor']
entertainment = ['private beach villa', 'nightclub with VIP booth', 'Dive-bar', 'dia de muerto']



def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return 1
    elif reply[0] == 'n':
        return 0
    else:
        return yes_or_no("Please Enter (y/n) ")

user_name = input('what is your name?')



print('Welcome! time to plan your trip',user_name)





print("")
while True:
    # DRAW PLOT HERE;
    print("OK...")
    if(yes_or_no((('would you like to go to ' + (random.choice( destination)))))):
        break
print("Good Choice")




print("")
while True:
    # DRAW PLOT HERE;
    print("OK...")
    if(yes_or_no((('would you like to arrive by ' + (random.choice( transportation)))))):
        break
print("Good Choice")


print('Would you like to eat at a ' + (random.choice( restaurants)))

print("")
while True:
    # DRAW PLOT HERE;
    print("OK...")
    if(yes_or_no((('would you like to eat at a ' + (random.choice( restaurants)))))):
        break
print("Good Choice")



print('Would you like to be entertained via ' + (random.choice( entertainment)))

print("")
while True:
    # DRAW PLOT HERE;
    print("OK...")
    if(yes_or_no((('would you like to be entertained via ' + (random.choice( entertainment)))))):
        break
print("Good Choice")
