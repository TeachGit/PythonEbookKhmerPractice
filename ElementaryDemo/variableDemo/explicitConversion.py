stringNumber = '12'  # ផ្ដើមតម្លៃតួអក្សរ ឱ្យអថេរ stringNumber
integerNumber = 23  # ផ្ដើមតម្លៃចំនួនគត់ ឱ្យអថេរ integerNumber

# ធ្វើការបំប្លែងតម្លៃរបស់អថេរ stringNumber ទៅជាចំនួនគត់តាមការបំប្លែងដោយផ្ទាល់
stringNumber = int(stringNumber)

# ធ្វើប្រមាណវិធីលើតម្លៃទាំងពី
sumNumber = integerNumber + stringNumber

# បង្ហាញតម្លៃថ្មីក្រោយការគណនា និងប្រភេទទិន្នន័យរបស់វា
print("លទ្ធផលគឺ :", sumNumber)
print("ប្រភេទទិន្នន័យ sumNumber គឺ", type(sumNumber))
