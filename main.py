# (5 points): As a developer, I want to make at least three commits with descriptive messages. 

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
form_of_entertainments = ['Hiking', 'Disney World', 'Ballet', 'Cirque du Soleil', 'Broadway Musical'] 


random_destination = destinations[0]
random_resturant = restaurants[0]
random_mode_of_transportation = mode_of_transportations[0]
random_form_of_entertainment = mode_of_transportations[0]

user_input = "Yes", "No" 

for destination in destinations:
    print(f"How about {random_destination(1)} as a place to visit? Is that okay? ")


for restaurant in restaurants:
    print(f"How about {random_resturant} as a place to eat? Is that okay? ")


