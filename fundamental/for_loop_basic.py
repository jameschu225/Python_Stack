# basic
for i in range(151):
    print(i)

# Multiples of Five
for i in range(5,1001):
    if i % 5 == 0:
        print(i)        

# Counting, the Dojo Way
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa. That Sucker's Huge
x =0
for i in range(500001):
    if i % 2 ==0:
        x += i
print(x)

# Countdown by Fours
for i in range(2018,0,-4):
    print(i)

# Flexible Counter
import random
lowNum = random.randint(0,50)
highNum = random.randint(50,100)
mult = random.randint(0,9)
print(lowNum,highNum,mult)
for i in range(lowNum, highNum):
    if i % mult ==0:
        print(i)