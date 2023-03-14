# List = Data Structure
fruits = ['Cherry', 'Apple', 'Orange']

states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
          "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

state = states[3]
state2 = states[-5]

print(states[1])
print(state)
print(state2)

# Change data
states[1] = "Pencilvania"
print(states)

# Add item to end of list
states.append("New State")
print(states)

# Add multiple items to end of list
states.extend(["Sidney Land", "Allie Land"])
print(states)
