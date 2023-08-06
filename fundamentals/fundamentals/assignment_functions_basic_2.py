# Countdown
def countdown(num):
    my_num = []
    for i in range(num, -1,-1):
        my_num.append(i) 
    return my_num

print(countdown(10))

# Print and Return
def print_and_return(a):
    print(a[0])
    return a[1]

a = [1,2]
print(a)

# First Plus Length
def first_plus_length(num_list):
    return num_list[0] + len(num_list)

list = [1,2,3,4,5,6,7,8,9]
result = first_plus_length(list)
print(result)

# Values Greater than Second
def values_greater_than_second(first_value):
    if len(first_value) < 2:
        return False

    second_value = first_value[1]
    new_list = [value for value in first_value if value > second_value]

    print(f"The number of values greater than the 2nd value is: {len(new_list)}")
    return new_list

result1 = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(result1)
result2 = values_greater_than_second([3])
print(result2)

# This Length, That Value 
def length_value(size,value):
    return [value] * size

output = length_value(10,10)
print(output)
