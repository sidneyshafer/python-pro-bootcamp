# PyPi - python packages
# Practice modifying object attributes and calling methods

# Import PrettyTable class form prettytable package
from prettytable import PrettyTable
# Create an object from the PrettyClass
table = PrettyTable()

# Add columns to table using the add_column() method
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Change table style attributes
table.align = "l"
table.header_style = "upper"

# Display table
print(table)
