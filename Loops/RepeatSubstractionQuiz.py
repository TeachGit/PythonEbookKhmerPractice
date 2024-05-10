import random

# ជំហានទី 1: បង្កើតចំនួនគត់ចំនួនពីរដោយចៃដន្យ number1 និង number2 ។
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
# ជំហានទី 2: ប្រសិនបើ number1 < number2, ធ្វើការប្ដូរតម្លៃគ្នារវាង number1 ជាមួយ number2 ។
if number1 < number2:
    number1, number2 = number2, number1  # Simultaneous assignment
# ជំហានទី 3: ឱ្យសិស្សញ្ចូលតម្លៃដើម្បឆ្លើយសំណួរ "តើ number1 - number = ?" ។
answer = eval(input("តើ " + str(number1) + " - " + str(number2) + " ? "))
# ជំហានទី 4: ផ្ទៀងផ្ទាត់ចម្លើយរបស់សិស្ស បើមិនត្រឹមត្រូវត្រូវបញ្ចូលឡើងវិញម្ដងទៀត
while number1 - number2 != answer:
    answer = eval(input("តើ " + str(number1) + " - " + str(number2) + " ? "))
print("ចម្លើយរបស់អ្នកត្រឹមត្រូវ")


