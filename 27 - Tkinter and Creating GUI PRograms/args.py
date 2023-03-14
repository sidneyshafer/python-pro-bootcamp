# Many Positional Arguments *
# Unlimited Arguments
# def add(*args):
#    for n in args:
#        print(n)

def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(3, 5, 6))
