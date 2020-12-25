# LIST / SET / DICTIONARY COMPREHENSIONS
# comprehensions allows us to build sequences from other sequences in an easy quick and elegant way

# LIST COMPREHENSIONS

# normal way
# list1 = []
# for i in range(10):
#     result = i ** 2
#     list1.append(result)
# print(list1)

# comprehension way
# list2 = [j ** 2 for j in range(10)]
# print(list2)

# comprehension way + else if statement
# list3 = [k ** 2 for k in range(10) if k > 5]
# print(list3)

# SET COMPREHENSIONS

# set1 = {x ** 2 for x in range(10)}
# print(type(set1))
# print(set1)

# DICTIONARY COMPREHENSIONS

# dict1 = {x: x * 2 for x in range(10)}
# print(dict1)

# ----------------------------------------------------------

# LAMBDA FUNCTION
# lambda function enabling us to quickly insert some functionality into our code especially in places that would not allow the definition of a regular function
# lambda arg1, arg2, ... , arg n: an expression using the arguments

# EXAMPLE OF SIMPILE LAMBDA FUNCTION
# a = lambda x, y: x * y
# print(type(a)) # lambda type is function
# print(a(5,10))

# REGULAR FUNCTION
# def myfunc(mylist):
#     list_xy = []
#     for x in range(10):
#         for y in range(5):
#             result = x * y
#             list_xy.append(result)
#     return list_xy + mylist
# print(myfunc([100,101,102]))

# LAMBDA FUNCTION
# b = lambda mylist: [x * y for x in range(10) for y in range(5)] + mylist
# print(b([100,101,102]))

# ----------------------------------------------------------

# MAP() & FILTER()
# map() will take a function and a sequence as argument and applies the function to all the elements of the sequence or returning an iterable object as the result the function taken
# filter() will also take a function and a sequence as argument and its role to extract all elements in the sequence for which the function returns true

# REGULAR FUNCTION USES MAP()
# def product10(a):
#     return a * 10
# r1 = range(10)
# print(list(map(product10, r1)))

# LAMBDA FUNCTION USES MAP()
# result1 = list(map((lambda a: a * 10), range(10)))
# print(result1)

# LAMBDA FUNCTION USES FILTER()
# result2 = list(filter((lambda a: a > 5), range(10)))
# print(result2)

# ----------------------------------------------------------

# ITERATORS & GENERATORS
# generator is a special routine that can be used to control the iteration behaviour of a loop

# EXAMPLE OF ITERATORS
# my_list = [1,2,3,4,5,6,7]
# my_iter = iter(my_list)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# EXAMPLE OF GENERATORS
# def my_gen(x, y):
#     for i in range(x):
#         print("i is %d" % i)
#         print("y is %d" % y)
#         yield i * y

# create a generator object
# my_object = my_gen(10, 5)

# print(next(my_object))
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))

# ----------------------------------------------------------

# ITERTOOLS: CHAIN(), COUNT(), CYCLE(), FILTERFALSE(), ISLICE()
# chain(): combine multiple lists into 1 sequence
# count(): returns an iterator that generates consecutive integers until you stop it
# cycle(): returns an iterator that simply repeats the value given as an argument infinitely
# filterfalse(): returns the elements for which the function you provide as an argument returns false
# islice(): works the same as string slices

# from itertools import *

# CHAIN FUNCTION
# list1 = [1,2,3,'a','b','c']
# list2 = [101,102,103,'X','Y']

# print(list(chain(list1, list2))) # convert chain list1 & list2 into list

# for i in chain(list1, list2): # for loop with list1 & list2 as the iterator
#     print(i)

# COUNT FUNCTION
# for i in count(10, 2.5):
#     if i <= 50:
#         print(i)
#     else:
#         break

# CYCLE FUNCTION
# a = range(11, 16)
# for i in cycle(a):
#     print(i)

# FILTERFALSE FUNCTION
# a = list(filterfalse(lambda x: x < 5, [1,2,3,4,5,6,7]))
# print(a)

# ISLICE FUNCTION
# b = islice(range(10), 2, 9, 2)
# print(list(b))

# ----------------------------------------------------------

# DECORATORS
# decorator is a function that takes another function as parameter and extend its functionality and behaviour without modifying it

# def my_decorator(target_function):
#     def function_wrapper():
#         return "Python is such a " + target_function() + " language!"
#     return function_wrapper

# @my_decorator
# def target():
#     return "cool"
# print(target())

# this is equal to:
# target = my_decorator(target)
# print(target())

# ----------------------------------------------------------

# THREADING BASICS
# threading can be used to run several function calls or other tasks concurrently especially if those tasks involve some waiting times
# this is the case for networking applications and web related tasks among others

# import threading
# import time

# def myfunction():
#     print("Start a thread")
#     time.sleep(3)
#     print("End a thread")

# threads = []

# for i in range(5):
#     th = threading.Thread(target = myfunction)
#     th.start()
#     threads.append(th)

# for th in threads:
#     th.join()