num1 = 42 #numbers
num2 = 2.3  #floats
boolean = True #boolean
string = 'Hello World' #strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuples
print(type(fruit)) #initialize print class type fruit and strings
print(pizza_toppings[1])#initialize 
pizza_toppings.append('Mushrooms')#add value 
print(person['name']) #access value 
person['name'] = 'George' #add key value pair
person['eye_color'] = 'blue'# add a value pair
print(fruit[2]) #print index 2 of fruit 

if num1 > 45: #conditional statement 
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #data type that has alength attribute used to get length string 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop function 0,1,2,3,4
    print(x)
for x in range(2,5):#for loop 2,3,4
    print(x)
for x in range(2,10,3):#for loop--multiples of 3:  2,5,8
    print(x)
x = 0
while(x < 5): #while loop 
    print(x)
    x += 1

pizza_toppings.pop() #removes last 
pizza_toppings.pop(1) #removes index at 1

print(person) 
person.pop('eye_color')#removes values 
print(person) #initilize new value 

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello') #out hello 10x 

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)