import math
radius = eval(input("សូមបញ្ចូលកាំរបស់រង្វង់៖"))
if radius >= 0:
    area = radius * radius * math.pi
    print("ក្រឡាផ្ទៃនៃរង្វង់ដែលមានកាំ ", radius, " គឺ ", area)
else:
    print("អ្នកបញ្ចូលតម្លៃអវិជ្ជមាន")
