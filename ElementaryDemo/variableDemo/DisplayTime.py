seconds = eval(input("បញ្ចូលចំនួនវិនាទីសរុប៖ ")) #អនុញ្ញាឱ្យអ្នកប្រើបញ្ចូលចំនួនវិនាទី
minute = seconds // 60  # ធ្វើប្រមាណវិធីចែកចំនួនគត់ដើម្បីរកចំនួននាទី
remainSeconds = seconds % 60 # ធ្វើប្រមាណវិធីចែករកសំណល់ដើម្បីរកចំនួនវិនាទីនៅសល់
print(seconds, "វិនាទី ស្មើរនឹង", minute, "នាទី ", remainSeconds, "វិនាទី")

