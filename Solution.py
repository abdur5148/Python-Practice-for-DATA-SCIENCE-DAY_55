var1 = int(input("Enter number : "))
num1 = 0
for i in range(1, var1+1):
    num1 += float(float(i)/(i+1))
print(num1)
