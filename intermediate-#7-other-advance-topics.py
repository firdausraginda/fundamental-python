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