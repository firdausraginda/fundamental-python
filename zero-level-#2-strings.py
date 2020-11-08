# BUILD IN METHODS
# use triple quotes for text with seperate line
# my_string = '''this
# is
# my
# first
# string'''
# print(my_string)

# \n can also create new line
# my_string = 'this\nis\nmy\nfirst\nstring'
# print(my_string)

# read string per character
# string1 = 'Cisco Router'
# print(string1[0])
# print(string1[2])
# print(string1[-1])
# print(string1[-2])

# find the first occurance of a char in a string
# a = 'Cisco Switch'
# print(a.index("i"))

# count hom many char appears in a string
# a = 'Cisco Switch'
# print(a.count("i"))

# find sequence of char in a string and retun the first index
# a = 'Cisco Switch'
# print(a.find("sco"))

# if a.find() didn't find a match, then will return -1
# a = 'Cisco Switch'
# print(a.find("scox"))

# proof that strings is immutable
# a = 'Cisco Switch'
# print(a.lower())
# print(a.upper())
# print(a)

# starswith & endswith built-in method
# a = 'Cisco Switch'
# print(a.startswith("C"))
# print(a.endswith("h"))

# strip built-in method to remove whitespaces
# b = "         Cisco Switch         "
# print(b)
# print(b.strip())

# replace built-in method to remove whitespaces
# b = "         Cisco Switch         "
# print(b)
# print(b.replace(" ", ""))

# split built-in method to split strings
# d = "Cisco,Juniper,HP,Avaya"
# print(d.split(","))

# join built-in method to join strings
# a = 'Cisco Switch'
# print("_".join(a))

# ----------------------------------------------------------

# OPERATOR
# concat strings
# x = "Cisco"
# y = "Switch"
# print(x+y)

# in & not in operator
# x = "Cisco"
# print("o" in x)
# print("b" not in x)

# ----------------------------------------------------------

# STRING FORMATTING
# string formatting using % operator
# %s for string, %d for double, %f for float
# a = "Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
# print(a)

# % operator for float and specify its comma
# a = "Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM", 2, 12.4)
# print(a)

# string formatting using .format
# a = "Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4)
# print(a)

# string formatting using .format and defined index
# a = "Cisco model: {2}, {0} WAN slots, IOS {1}".format("2600XM", 2, 12.4)
# print(a)

# string formatting using F-string
# model = '2600XM'
# slots = 4
# ios = 12.3
# a = f"Cisco model: {model.lower()}, {slots*2} WAN slots, IOS {ios}"
# print(a)

# ----------------------------------------------------------

# SLICES
# a = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

# print(a[5:15]) # print out char from index 5 to index 14
# print(a[5:]) # print out char from index 5 to the last index
# print(a[:10]) # print out char from the beginning to index 9
# print(a[-9:-1]) # print out char from index -9 to index -2
# print(a[-5:]) # print out char from index -5 to the last index
# print(a[:-5]) # print out char from the beginning to index -6
# print(a[::2]) # skip every 2nd char in a string, from the beginning to the last index
# print(a[::-1]) # print out char in reverse order

# ----------------------------------------------------------

