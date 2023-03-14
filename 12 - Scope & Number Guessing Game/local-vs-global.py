# Scope
# Namespace

# Modifying Global Scope
enemies = 1

def increase_enemies():
    # define global variable in order to access it
    # not recomended!!
    # global enemies
    print(f"enemies inside function: {enemies}")
    return enemies + 2

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
# Within functions
def drink_potion():
    potion_strength = 2 # variable can only be accesible within the function
    print(potion_strength)

drink_potion()
# print(potion_strength) --> output NameError, not defined

# Global Scope
player_health = 10 # variable is available anywhere within file; defined at top level

def boost_health():
    potion_strength = 2
    print(player_health)

boost_health()

# No Block Scope
game_level = 3
def create_enemy():
    # If you create a variable within a function, 
    # it is only available within that function
    enemies_list = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        # If you create a variable within an if or for loop,
        # than you can access it outside the loop
        new_enemy = enemies_list[0]
    
    print(new_enemy) # valid

# print(new_enemy) -- > not valid

# Global Constants
# Define constant -- > all uppercase
PI = 3.14159
HAPPY = True

def calc():
    pi

def greet():
    return HAPPY