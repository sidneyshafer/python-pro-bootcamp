# Creating a class
# Classes should be in PascalCase (ex: HelloWorldMethod)
#    - camelCase --> not used much in python
#    - snake_case
# Attribute: variable associated with an object, the thing an object has
# Method: the thing the object does
# Constructor: specifies what should happen when the object is being constructed
#    - also known as "initializing" an object
#    - def__init__(self) function --> used to initialise attributes
#      - __init__ called everytime class is initialized
# pass - continue on

class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Initialize an object from a class
user_1 = User("001", "Sidney")
user_2 = User("002", "Allie")
user_2.followers = 10

user_1.follow(user_2)
user_2.follow(user_1)

print(f"{user_1.username} --> Followers: {user_1.followers} Following: {user_1.following}")
print(f"{user_2.username} --> Followers: {user_2.followers} Following: {user_2.following}")

