
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


destinations = ['Estes Park, CO', 'Orlando, FL', 'San Antonio, TX', 'Portland, ME', 'San Francisco, CA', 'New York City']
restaurants = ['Grubsteak Restaurant', 'Santiagos Bodega Tapas Bar', '18 Oaks Steakhouse', 'Fore Street Restaurant', 'Sotto Mare Seafood', 'Jekyll and Hyde Club']
mode_of_transportations = ['Rental car', 'Airplane', 'Train', 'Horseback']
form_of_entertainments = ['Go on a hike', 'Go to Disney World', 'Go to a ballet', 'See a Cirque du Soleil show', 'See a Broadway Musical'] 

import random
i = 0

print("What about the lovely city of", destinations[0], "as a destination? Is that okay? Yes or No")

valid_response = False
while valid_response == False: 
    user_input = input("")
    if user_input == "Yes":
        print("Great choice!")
        valid_response = True 
    elif user_input == "No":
        print("Oh, my apologies. How about", destinations[i],"?")
        i = i + 1
        valid_response = False
    else:
        print("I'm sorry. Please say Yes or No.")
        valid_response = False 
final_dest = destinations[i - 1]

print(final_dest, "is a great choice!")

#Next is restaurant

print("Next, let's chose a restaurant. How about", restaurants[0],"?")

valid_response = False
while valid_response == False: 
    user_input = input("")
    if user_input == "Yes":
        print("Excellent!")
        valid_response = True 
    elif user_input == "No":
        print("Oh, my apologies. How about", restaurants[i],"?")
        i = i + 1
        valid_response = False 
    else:
        print("I'm sorry. Please say Yes or No.")
        valid_response = False 
final_rest = restaurants[i - 1]
print(final_rest, "is a fantastic decision!")



#print("Great choice! Now how about ", final_restaurant, "as a restaurant?") 
#print("Excellent! Would you like to travel by", final_transportation),"?")
#print("Fantastic! During your trip what would you like to do? How about", final_entertainment),"?")



# def run():
#     print(final_destination)
#     print(final_restaurant)
#     print(final_transportation)
#     print(final_entertainment) 

# run()
