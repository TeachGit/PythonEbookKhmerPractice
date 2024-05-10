import random

guessNumber = random.randint(1, 100)
print("ទស្សន៍ទាយលេខនៅចន្លោះ 0 - 100")
answer = -1
while guessNumber != answer:
    answer = eval(input("សូមបញ្ចូលលេខដែលអ្នកទាយ៖"))
    print("លេខដែលអ្នកបញ្ចូលមានតម្លៃធំជាងលេខចៃដន្យ") if answer > guessNumber else print("លេខដែលអ្នកបញ្ចូលមានតម្លៃតូចជាងលេខចៃដន្យ")
print("លេខដែលអ្នកទាយត្រឹមត្រូវហើយ")
