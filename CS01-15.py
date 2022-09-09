a = []
while (a != -1):
    b = int(input("Input your scores : "))
    if b == -1 :
        break
    a += [b]

for b in a:
    print(b)