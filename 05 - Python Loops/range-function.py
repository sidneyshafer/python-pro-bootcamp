# For loops with range function (no lists)
''' 
for number in range(a,b)
   print (number)

for number in range(1, 10):  # 1 through 10 (but not including 10)
    print(number)

for number in range(1, 11, 2):
    print(number)
'''

total = 0
for number in range(1, 101):
    total += number
print(total)
