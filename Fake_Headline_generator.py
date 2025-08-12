import random
subjects = [
    "Sahrukh Khan",
    "virat Kohli",
    "Salman Khan",
    "A Mumbai Cat",
    "A group of monkey",
    "Auto Driver From Durgapur"
]

actions = [
    
    "cancels",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
    "dancing",
    "play"
]

places = [
    "at red fort",
    "in Ganga ghat",
    "Indian gate",
    "during ipl match",
    "inside parliament",
    "on the stage",
    "plate of samosa",
    "free fire"
]

while True:
     subject = random.choice(subjects)
     action = random.choice(actions)
     place = random.choice(places)

     headline = f"BREAKING NEWS: {subject} {action} {place}"
     print("\n" + headline)


     user_input = input("\n Do You want another headline ?").strip().lower()
     if user_input == "no":
          break
     
print("\nThanks for using the fake news headline generator. ")