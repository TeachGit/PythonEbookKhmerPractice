number = eval(input("បញ្ចូលលេខដែលជាចំនួនគត់:"))
if number % 2 == 0 and number % 3 == 0:
    print(number, " ជាលេខចែកដាច់នឹង 2 and 3")
if number % 2 == 0 or number % 3 == 0:
    print(number, " ជាលេខចែកដាច់នឹង 2 or 3")
if (number % 2 == 0 or number % 3 == 0) and not(number % 2 == 0 and number % 3 == 0):
    print(number, " ជាលេខចែកដាច់នឹង 2 or 3 តែមិនមែន 2 and 3")
