# RULE
# python uses indentation to define code blocks (if, for, while), function & clases
# uses indentation means that white spaces (4 spaces or a tab key) are used as delimiters for code blocks
# after every if, for, while statement, or function or class definition, must use a colon

# ----------------------------------------------------------

# IF ELSE STATEMENT

# x = 5

# if x == 5 and type(x) is int:
#     print("x equals 5 & is int")
#     print(x)
# elif x == 10 and type(x) is int:
#     print("x equals 5 & is int")

# ----------------------------------------------------------

# FOR LOOPS
# for loops iterate through indexes

# example for loop
# vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

# for each_vendor in vendors:
#     print(each_vendor)
# else:
#     print("The end of list has been reached")

# loop with range
# r = range(10)

# for i in r:
#     print(i * 2)

# loop with range and length of the list
# vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

# for el_index in range(len(vendors)):
#     print(vendors[el_index])

# loop with enumerate
# vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

# for idx, el in enumerate(vendors):
#     print(idx, el)

# ----------------------------------------------------------

# WHILE LOOPS
# while loops will continue looping until the value become false

# example while loop
# x = 1

# while x <= 10:
#     print(x)
#     x = x + 1
# else:
#     print("x is now > 10")

# ----------------------------------------------------------

# NESTED IF STATEMENT & FOR LOOPS
# inner if statement will be executed if the outer statement is true

# example of nested if statement
# x = "Cisco"

# if "i" in x:
#     if len(x) > 3:
#         print(x, len(x))

# example of nested for loops
# list1 = [4,5,6]
# list2 = [10,20,30]

# for i in list1:
#     for j in list2:
#         print(i*j)
#     print('---',i,'---')

# example of nested if statement inside for loops
# for number in range(10):
#     if 5 <= number <= 9:
#         print(number)

# ----------------------------------------------------------

# BREAK STATEMENT

# break will ignore the print function & completely quit the for loops
# for number in range(10):
#     if number == 7:
#         break
#     print(number)

# break only terminates the execution of the innermost loop, not all the loops
# list1 = [4,5,6]
# list2 = [10,20,30]

# for i in list1:
#     for j in list2:
#         if j == 20:
#             break
#         print(i*j)
#     print("outside the nested loop")

# ----------------------------------------------------------

# CONTINUE STATEMENT

# continue statement will not stop the whole iteration of the innermost for loop, instead, it only stops the current iteration
# list1 = [4,5,6]
# list2 = [10,20,30]

# for i in list1:
#     for j in list2:
#         if j == 20:
#             continue
#         print(i*j)
#     print("outside the nested loop")

# ----------------------------------------------------------

# PASS STATEMENT

# pass statement is equal of do nothing
# pass statement is just a placeholder for whenever you want to leave the addition of a piece of code for later

# for i in range(10):
#     pass