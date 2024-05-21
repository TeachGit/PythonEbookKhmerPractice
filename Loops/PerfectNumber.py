NUMBER_IN_RANGE = 10000
for isPerfectNumber in range(NUMBER_IN_RANGE):
    sum = 0
    for i in range(1,isPerfectNumber):
        if isPerfectNumber % i == 0:
            sum += i
    if isPerfectNumber == sum and isPerfectNumber != 0:
        print(format(isPerfectNumber,"4d"),end=" ")
