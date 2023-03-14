# PYTHON BUILT-IN FUNCTIONS
''' 
## print(), int(), len()
string = "Hello"
print(string)
char = len(string)
print(char)
'''

# CREATING FUNCTIONS

def my_function():
    print("Hello")
    print("Goodbye")

# CALL FUNCTION
my_function()

''' REBORG'S WORLD PUZZLE
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(num):
    hurdle = 0
    while hurdle != num:
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        hurdle += 1
    
jump(6)
'''
# While loop can also be written as:
'''
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
'''