import random
import my_module

# Create random whole numbers
# Specify range of numbers (start, end) <-- includes start and end
random_int = random.randint(1, 10)
print(random_int)

print(my_module.pi)

# Create a random floating number
# random() always generates a num between 0 and 1
rand_float = random.random()
print(rand_float)

# Generate random float between 0 and 5
randomFloat = random.random() * 5
print(randomFloat)

# Generate a random love score
loveScore = random.randint(1, 100)
print(f"Your love score is {loveScore}.")
