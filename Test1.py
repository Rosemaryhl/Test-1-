#Rosemary Hoffman Test1
#problem 1
import math
def calculation(a,b,c):
    Trig=(2*math.pi*a**3)+3*math.sin(b)+530.27*math.sqrt(c+34)
    print(Trig)

calculation(20,0,30)

#Problem 2
def is_divisible_five(x):
    if x%5==0:
        print("Yes, it is!")
    else:
        print("No, it is not!")
is_divisible_five(15)
is_divisible_five(13)

#problem 3
import math
for x in range(2,10):
    print(math.sqrt(x)+1)
