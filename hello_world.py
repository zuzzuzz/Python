# 1. TASK: print "Hello World"
greetings = "Hello World"
print(greetings)

# 2. print "Hello Noelle!" with the name in a variable
name = "Duy"
print("Hello", name,"!")	# with a comma
print("Hello " + name + "!")	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 8
print("Hello", name, "!")	# with a comma
print("hello" + str(8) +"!")	# with a +-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "pad see eww"
fave_food2 = "pho"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) 
print(f"I love to eat {fave_food1} and {fave_food2}.")

