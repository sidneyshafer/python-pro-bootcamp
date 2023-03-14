# age: int
# name: str
# height: float
# is_human: bool
#
# age = 18
# name = "Sidney"

# type hints
def police_check(age: int) -> bool:
    can_drive: bool
    if age >= 16:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check(16))
