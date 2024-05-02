def add_one(x):  # parameter x
    y = x + 1  # the logic
    return y


# def functionName(parameters)
#   statements
#   return (expression)

# benefits og using functions:
# 1. Reusable code
# 2. error-checking and validating your code easier
# 3. divide code into manageable chunks
# 4. more rapid application development
# 5. easier to maintain application

###################################
# SCOPE
# A function can call variables that are outside the function, but the rest of the code cannot call variables that are defined inside the function.


def adding(a, b):
    total = a + b
    return description + str(total)


x = 2
y = 3
description = "Total:"

sum = adding(x, y)

print(sum)


#################################################
def adding(a, b):
    total = a + b
    description1 = "Total:"
    return str(total)


x = 2
y = 3
sum = adding(x, y)
# print(description1+sum)
# NameError: name 'description1' is not defined
#################################

# Default values


def multiply(num1, num2=5):  # set a default value of 5 for num2
    total = num1 * num2
    print(f"{num1}*{num2}={total}")


time_5 = multiply(6)
time_5_8 = multiply(5, 8)  # override default value
multiply_test = multiply(num2=5, num1=4)
# enables to provide values ina different order to how they are assigned in the function


# multiply_test=multiply(num2=5,4)
# have to specify either all or none)


# ************ Example 7 ************
def put_number_in_list(num):
    newList = []
    newList.append(num)
    return newList


# ************ Example 8 ************
def put_number_in_list_if_big(num):
    newList = []
    if num > 100:
        newList.append(num)
    return newList  # Be careful! This could return an empty list.


# =========== Functions Without Return Statements ===========
# Functions do not need to have a return statement

# ************ Example 12 ************
print("\nExample 12:")
# We can call the function multiple times in a loop:

num = 10
# This loop runs 10 times, and each time, 1 is added to the value of 10.
# So after the first iteration it will be 11, the second iteration computes
# 11 + 1 = 12, etc... until 20.
for i in range(10):
    num = add_one(num)
print(num)
