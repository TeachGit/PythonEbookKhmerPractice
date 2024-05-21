n = eval(input("បញ្ចូលចំនួនគត់ >= 2: "))
factor = 2
while factor <= n:
    if n % factor == 0:
        break
    factor += 1
print("ផលគុណកត្តាដែលតូចបំផុតក្រៅពី 1 នៃ", n, "គឺ", factor)


