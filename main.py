
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!



greeting = "Welcome to the Day Trip Generator! Would you like some help deciding on plans for a vacation? Please, allow me to help you choose. "

print(greeting)


destinations = ['Estes Park, CO', 'Orlando, FL', 'San Antonio, TX', 'Portland, ME', 'San Francisco, CA', 'New York City']
restaurants = ['Grubsteak Restaurant', 'Santiagos Bodega Tapas Bar', '18 Oaks Steakhouse', 'Fore Street Restaurant', 'Sotto Mare Seafood', 'Jekyll and Hyde Club']
mode_of_transportations = ['rental car', 'airplane', 'train', 'horseback']
form_of_entertainments = ['Go on a hike', 'Go to Disney World', 'Go to a ballet', 'See a Cirque du Soleil show', 'See a Broadway Musical'] 


import random
user_input = "Y", "N"


print("What about the lovely city of", random.choice(destinations), "as a destination?")



#print("Great choice! Now how about ", random.choice(restaurants), "as a restaurant?") 
#print("Excellent! Would you like to travel by", random.choice(mode_of_transportations),"?")
#print("Fantastic! During your trip what would you like to do? How about", random.choice(form_of_entertainments),"?")


