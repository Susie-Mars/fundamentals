# BASIC
for i in range(151):
    print(i)

# MULTIPLES OF FIVE
for i in range(5,1001,5):
    print(i)

# COUNTING, THE DOJO WAY
for i in range(1,100+1):
    if (i%10==0):
        print("Coding Dojo")
    elif (i%5==0):
        print("Coding")
    else:
        print(i)


# WOAH, THAT SUCKERS HUGE
sum = 0
for i in range(0,50000+1):
    if (i%2!=0):
        sum+=i
print(sum)

# COUNTDOWN BY FOURS
for i in range(2018,0,-4):
    print(i)

# FLEXIBLE COUNTER
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if (i%3=0):
        print(i)