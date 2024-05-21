sum = 0
i = 0.01
# បូក 0.01, 0.02, ..., 0.99, 1 ផ្ដល់តម្លៃទៅឱ្យអថេរ sum  
for count in range(100):
    sum += i
    i += 0.01
print("Sum = ", sum)
