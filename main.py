
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!



greeting = "Welcome to the Day Trip Generator! Would you like some help deciding on plans for a vacation? Please, allow me to help you. "

print(greeting)
print("")

destinations = ['Estes Park, CO', 'Orlando, FL', 'San Antonio, TX', 'Portland, ME', 'San Francisco, CA', 'New York City']
restaurants = ['Grubsteak Restaurant', 'Santiagos Bodega Tapas Bar', '18 Oaks Steakhouse', 'Fore Street Restaurant', 'Sotto Mare Seafood', 'Jekyll and Hyde Club']
mode_of_transportations = ['Rental car', 'Horseback', 'Airplane', 'Train', 'Helicopter']
form_of_entertainments = ['See a Cirque du Soleil show', 'Go to a play', 'Go to a ballet', 'Go to Disney World', 'Go to a musical'] 

import random
d = 0
r = 0
t = 0 
e = 0

#Begin destinations
print("What about the lovely city of", destinations[d], "as a destination? Is that okay? Yes or No")

valid_response = False
while valid_response == False: 
    user_input = input("")
    if user_input == "Yes":
        print("Great choice!")
        valid_response = True 
    elif user_input == "No":
        d = d + 1
        print("Oh, my apologies. Let's chose something else. How about", destinations[d],"?")
        valid_response = False
    else:
        print("I'm sorry. Please say Yes or No.")
        valid_response = False 
final_dest = destinations[d]

print(final_dest, "is a wonderful city to explore!")
print("")
#Next is restaurant
print("Next, let's chose a delicous restaurant. How about", restaurants[0],"?")

valid_response = False
while valid_response == False: 
    user_input = input("")
    if user_input == "Yes":
        print("Yum! That sounds amazing!")
        valid_response = True 
    elif user_input == "No":
        r = r + 1
        print("Oh, my apologies. Let's try another one. How about", restaurants[r],"?")
        valid_response = False 
    else:
        print("I'm sorry. Please say Yes or No.")
        valid_response = False 
final_rest = restaurants[r]
print(final_rest, "is a fantastic decision!")
print("")

#Modes of transportation
print("Next, we'll decide on a method of transportation. How about", mode_of_transportations[0],"? Isn't that exciting? Yes or No")

valid_response = False
while valid_response == False: 
    user_input = input("")
    if user_input == "Yes":
        print("Great choice!")
        valid_response = True 
    elif user_input == "No":
        t = t + 1
        print("Oh, my apologies. Let me try again. How about", mode_of_transportations[t],"?")
        valid_response = False
    else:
        print("I'm sorry. Please say Yes or No.")
        valid_response = False 
final_mode_of_trans = mode_of_transportations[t]

print(final_mode_of_trans, "sounds exciting!")
print("")

#Entertainment 
print("Finally, during your trip what would you like to do? How about", form_of_entertainments[0],"? Doesn't that sound lovely? Yes or No")

valid_response = False
while valid_response == False: 
    user_input = input("")
    if user_input == "Yes":
        print("I'm so excited for you!")
        valid_response = True 
    elif user_input == "No":
        e = e + 1
        print("Oh, my apologies. Let me try again. How about", form_of_entertainments[e],"?")
        valid_response = False
    else:
        print("I'm sorry. Please say Yes or No.")
        valid_response = False 
final_entertainment = form_of_entertainments[e]

print(final_entertainment, "sounds exciting!")
print("")

#Let's wrap this up
print("All right! Let's confirm everything:")
def run():
    print(final_dest)
    print(final_rest)
    print(final_mode_of_trans)
    print(final_entertainment) 

run()
print("Does that all look good? Yes or No")
print("")
valid_response = False
while valid_response == False: 
    user_input = input("")
    if user_input == "Yes":
        print("I'm so excited for you! You'll be visiting the exciting city of", final_dest, "by way of", final_mode_of_trans, "where you'll dine at the award winning", final_rest, ", and finish the evening by", final_entertainment,".")
    elif user_input == "No":
        print("I'm sorry. Let's try this again. Please start over.")
    break
    
print("")



