# DEFINITION
# tuple is immutable list
# tuple usefull when want to store data in a from of a sequence but duplication is allowed

# create tuple
# my_tuple = (1,2,3,4,5)
# print(type(my_tuple))
# print(my_tuple[2])

# tuple is immutable
# my_tuple = (1,2,3,4,5)
# my_tuple[1] = 9
# del my_tuple[1]

# taple packing & unpacking
# tuple1 = ("Cisco", "2600", "17.4")
# (vendor, model, ios) = tuple1
# print(tuple1)
# print(vendor)
# print(ios)

# another way to pack & unpack tuple
# (vendor, model, ios) = ("Cisco", "2600", "17.4")
# print(vendor)
# print(ios)

# ----------------------------------------------------------

# TUPLE VS LIST
# tuple is immutable
# list is mutable

# my_tuple = ()
# my_list = []

# ----------------------------------------------------------

# BUILT IN METHOD
# tuple2 = (1,2,3,4)
# print(len(tuple2))
# print(min(tuple2))
# print(max(tuple2))

# concate & multiply
# print(tuple2 + (5,6,7))
# print(tuple2 * 2)

# slicing
# tuple2 = (1,2,3,4)
# print(tuple2[:3])
# print(tuple2[3:])

# in & not in
# tuple2 = (1,2,3,4)
# print(3 in tuple2)
# print(3 not in tuple2)

# del
# tuple2 = (1,2,3,4)
# del tuple2
# print(tuple2)