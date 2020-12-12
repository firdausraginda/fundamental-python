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
x = 1

while x <= 10:
    print(x)
    x = x + 1
else:
    print("x is now > 10")