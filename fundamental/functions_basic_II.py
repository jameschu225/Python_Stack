# countdown
import random
x = []
def count_down(num):
    print(num)
    for i in range(num,0,-1):
        x.append(i)
    print(x)

count_down(random.randint(0,9))

# Print and Return
import random
def print_return (list):
    print (f"print {list[0]}")
    return list[1]

print_return ([random.randint(0,100), random.randint(0,100)])

# First Plus Length
import random
random_list =[]
list_len = random.randint(1,9)
for i in range(list_len):
    random_list.append(random.randint(0,9))
print (random_list)

def first_plus_length (list):
    plus = list[0] + list[len(list)-1]
    return plus
first_plus_length (random_list)

# Values Greater than Second
import random
random_list =[]
list_len = random.randint(1,10)
for i in range(list_len):
    random_list.append(random.randint(0,9))
print (random_list)

def value_grater_than_second (input_list):
    count = 0
    greater_2_list = []
    if len(input_list) >= 2:
        for i in input_list:
            if i > 2:
                greater_2_list.append(i)
                count += 1
        print (f" count {count}")
        return greater_2_list
    else:
        return "False"
value_grater_than_second (random_list)

# This Length, That Value
import random
def length_value (num1, num2):
    print(num1,num2)
    length_value_lsit = []
    i = 1
    while i <= num1:
        length_value_lsit.append(num2)
        i += 1
    return length_value_lsit

length_value (random.randint(1,10), random.randint(0,10))