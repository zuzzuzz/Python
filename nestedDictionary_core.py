
# 1 Update Values in Dictionary and Lists 

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15 #changes 10 to 15 at x index [1][0]
#print(x)

students[0]['last_name'] = 'Bryant' #changes name from Jordan to Bryant
#print(students)

sports_directory['soccer'][0] = 'Andres' #changed Messi to Andres  
#print(sports_directory)

z[0]['y'] = 30
#print(z)


# 2. Iterate Through List of Dictionaries 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(list): 
	for i in range(0, len(list)): 
		output = ""
		for key,val in list[i].items(): 
			output += f" {key} - {val}" 
		#print(output)

#iterateDictionary(students)

# 3. Get Values From a List of Dictionaries

def iterateDictionary2(key_name,list): 
	for i in range(0, len(list)): 
		for key,val in list[i].items():
			if key == key_name:
				print(val)
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#4 Iterate through a dictionary with list values

dojo = {
	'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
	'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict): 
	for key,val in dict.items(): 
		print("----")
		print(f"{len(val)} {key.upper()}")
		for i in range(0, len(val)): 
			print(val[i])

print_info(dojo)



