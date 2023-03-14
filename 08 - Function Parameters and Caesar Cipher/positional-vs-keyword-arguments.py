
# Positional Arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Sidney", "Minnesota")

# Keyword Arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(location="Minnesota", name="Sidney")