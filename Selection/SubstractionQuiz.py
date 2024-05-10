import random

# ជំហានទី 1: បង្កើតចំនួនគត់ចំនួនពីរដោយចៃដន្យ number1 និង number2 ។
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
# ជំហានទី 2: ប្រសិនបើ number1 < number2, ធ្វើការប្ដូរតម្លៃគ្នារវាង number1 ជាមួយ number2 ។
if number1 < number2:
    number1, number2 = number2, number1  # Simultaneous assignment
# ជំហានទី 3: ឱ្យសិស្សញ្ចូលតម្លៃដើម្បឆ្លើយសំណួរ "តើ number1 - number = ?" ។
answer = eval(input("តើ " + str(number1) + " - " + str(number2) + " ? "))
# ជំហានទី 4: ពិនិត្យចម្លើយរបស់សិស្ស ហើយបង្ហាញថាតើចម្លើយរបស់សិស្សត្រឹមត្រូវឬក៏អត់។
if number1 - number2 == answer:
    print("ចម្លើយរបស់អ្នកត្រឹមត្រូវ")
else:
    print("ចម្លើយរបស់អ្នកមិនត្រឹមត្រូវទេ\n", number1, '-', number2, "=", number1 - number2, '។')


