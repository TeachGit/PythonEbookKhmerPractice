sum = 0
number = 0
print("sum = 0", end="")
while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue
    sum += number
    print(" + ", number, end="")

print(" = ", sum)
print("អថេរ number មានតម្លៃ", number)
