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

# ----------------------------------------------------------

# ARGUMENTS
# arguments: are the ones written inside parentheses when CALLING the function

# positional arguments: number of argument in the function call should be the same as the number in the function definition
# example
# def my_func(a,b,c):
#     return a+b+c
# print(my_func(1,2,3))

# keyword arguments: allow us to ignore order when we enter the parameter in function definition, or even to skip some of them when calling the function.
# example1
# def my_func(a,b,c):
#     return a+b+c
# print(my_func(c=3,a=2,b=1))

# example2
# def my_func(a,b,c):
#     return a+b+c
# print(my_func(1,2,c=3))

# ----------------------------------------------------------

# NAMESPACES
# namespace is a space holding some name (variables, functions, classes)
# built-in namespace: contains python's built-in function (max, len, sort).
# global namespace: are variables that we defined globally
# local namespace: are variables that we defined locally (inside loops, or function)

# the different between global & local namespace
# my_var = 20 # global namespace
# def my_var_func():
#     my_var = 10 # local namespace    
#     print(my_var)

# my_var_func()
# print(my_var)

# need to define namespace (for both local & global) before print it out
# my_var = 20 # global namespace
# def my_var_func():
#     print(my_var)
#     my_var = 10 # local namespace    

# my_var_func()
# print(my_var)

# access global namespace in local
# my_var = 20 # global namespace
# def my_var_func():
#     global my_var # access global namespace    
#     print(my_var)
#     my_var = 10 # define local namespace
#     print(my_var)

# my_var_func()

# ----------------------------------------------------------

# IMPORTING MODULES

# import math
# print(dir(math)) # to breakdown the modules
# print(math.pi) # call var from the module

# import my_module
# print(my_module.my_var) # call var from the module
# my_module.my_function() # call function from the module

# using from import
# from my_module import my_function
# my_function()