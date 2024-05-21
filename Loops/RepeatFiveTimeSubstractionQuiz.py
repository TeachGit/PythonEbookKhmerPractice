import random
import time

count = 0
countCorrectAnswer = 0
NUMBER_OF_QUESTIONS = 5
startTime = time.time()  # ពេលវេលាចាប់ផ្ដើម
while count < NUMBER_OF_QUESTIONS:
    # ជំហានទី 1: បង្កើតចំនួនគត់ចំនួនពីរដោយចៃដន្យ number1 និង number2 ។
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    # ជំហានទី 2: ប្រសិនបើ number1 < number2, ធ្វើការប្ដូរតម្លៃគ្នារវាង number1 ជាមួយ number2 ។
    if number1 < number2:
        number1, number2 = number2, number1  # Simultaneous assignment
    # ជំហានទី 3: ឱ្យសិស្សញ្ចូលតម្លៃដើម្បឆ្លើយសំណួរ "តើ number1 - number = ?" ។
    answer = eval(input("តើ " + str(number1) + " - " + str(number2) + " ? "))
    if number1 - number2 == answer:
        print("ចម្លើយរបស់អ្នកត្រឹមត្រូវ")
        countCorrectAnswer += 1
    else:
        print("ចម្លើយរបស់អ្នកមិនត្រឹមត្រូវទេ\n", number1, '-', number2, "=", number1 - number2)
    count += 1
endTime = time.time()  # ពេលវេលាចាប់ផ្ដើម
testTime = int(endTime - startTime)  # គណនារកពេលវេលាដែលបានឆ្លើយ
print("លទ្ធផលអ្នកឆ្លើយត្រូវចំនួន", countCorrectAnswer, "នៃ", NUMBER_OF_QUESTIONS, "សំណួរ\nរយៈពេលដែលអ្នកធ្វើសំណួរគឺ",
      testTime, "វិនាទី")


