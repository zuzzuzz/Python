#1 Basic - Print all integers from 0 to 150. 
"""start, end = 0, 150

for num in range(start, end + 1):
    if num >= 0: 
        print(num, end =" ") """

#2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
#option 1. starts at 1 
""" for i in range(1,1000+1):
        print(i*5, end =" ")"""

#option2. starts at 5 
"""for i in range (5, 1000+1, 5):
    print(i)"""

#3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""for i in range (1, 100+1):
    if(i % 10 == 0):
        print("coding dojo")
    elif(i % 5 == 0 ):
        print("coding")
    else:
        print(i)"""

#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
#option 1: 
"""maxNum = 500000
newNum = sum(range(1,maxNum+1, 2)) # prints sum of all odd numbers in ranage 

for i in range(0,5000000): 
    if i % 2 != 0:
        print(i) #prints all odd numbers 
print(newNum)"""

#option 2: 
"""sum = 0
for i in range(1,50000+1,2):
    sum += i
print(sum)"""

#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
"""for i in range(2018, 0, -4):
    print(i)"""

#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

"""
lowNum = 0 
highNum = 20
mul = 4 

for i in range(lowNum,highNum+1): 
    if(i % mul == 0):
        print(i)
"""

