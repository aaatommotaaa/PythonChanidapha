pets = ["Cat","Dog","Bird"]
for i in pets:
    print (i)
    if i == "Cat":
        print("Cat")
    break

for x in range (10):
    print(x)
    for y in range(10):
        print(y)

for a in range (3):
    for b in range (0,a+1):
        if (b==1):
            print(b,end="")