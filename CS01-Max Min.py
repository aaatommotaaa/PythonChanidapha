num = int(input('Enter Your Loop '))
total =[]
for i in range(num):
    data = int(input('Enter Your Number:'))
    total += [data]
total.sort()
print(total[0])
print(total[-1])