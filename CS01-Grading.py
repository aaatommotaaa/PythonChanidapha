a = int(input("Accumulated scores : "))
b = int(input("Midterm scores : "))
c = int(input("Final scores : "))
x = a+b+c

if (x>=80) :
    print("A")
elif (x>=75) :
    print("B+")
elif (x>=70) :
    print("B")
elif (x>=65) :
    print("C+")
elif (x>=60) :
    print("C")
elif (x>55) :
    print("D+")
elif (x>=50) :
    print("D")
else : 
    print("F")

