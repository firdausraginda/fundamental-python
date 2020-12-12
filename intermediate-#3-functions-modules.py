# RULE
# defined using def keywoard, followed by the name of the function, pair of parentheses, & a colon

# example of a function
# def my_first_function():
#     "This is my first function" # space to give description of the function
#     print("Hello Python")

# can check the description of a function with help() function
# help(my_first_function)

# ----------------------------------------------------------

# PARAMETERS
# parameters: are the ones written inside parentheses when DECLARING the function
# arguments: are the ones written inside parentheses when CALLING the function

# function with parameters
# def my_first_function(x,y):
#     "This is function with a parameter"
#     print("hello " + x)
#     print("hello " + y)

# my_first_function('this is 1st argument', 'this is 2nd argument')

# function with return
# def my_sum(x,y):
#     sum = x + y
#     return sum

# print(my_sum(5,2))

# function with default parameter
# def my_sum(x,y=19):
#     sum = x + y
#     return sum

# print(my_sum(5))

# define function with unknown number of parameters
# def my_func(x, *arguments):
#     print(x)
#     for argument in arguments:
#         print(argument)

# print(my_func('1st argument',4,7,1))