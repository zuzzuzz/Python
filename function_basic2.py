
#1 countdown
# option 1
# for i in range(5,0,-1): 
#     print(i)

#option 2 with reversed() function 
# for i in reversed(range(0,5+1)): 
#     print(i)

#option 3 Best Solution for return function. 
def countdown(num):
    output = []
    for i in range(num,-1,-1): 
        output.append(i)
    return(output)

# print(countdown(6))

def print_and_return(list): 
    print(list[0])
    return(list[1])

# print(print_and_return([1,2]))


def first_plus_length(list): 
    return list[0] + len(list)

# print(first_plus_length([1,6,4,2,8]))

def Values_Greater_than_Second(list): 
    if len(list) < 2: 
        return False
    output = []
    for i in range (0, len(list)): 
        if list[i] > list[1]: 
            output.append(list[i])
    print(len(output))
    return output

# print(Values_Greater_than_Second([1,2,3,4,5]))
# print(Values_Greater_than_Second([3]))

def length_and_Value(size, value): 
    output = []
    for i in range(0, size): 
        output.append(value)
    return output
    
print(length_and_Value(3,6))
print(length_and_Value(5,3))