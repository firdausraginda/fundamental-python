# LISTS DEFINITION
# list is a sequence consisting of elements seperated by comma, the sequence of element is enclosed by square brackets.
# list can have any data types as elements of a list. List may have any number of elements.
# lists are indexed, meaning each element has a certain position inside the list, starting at index 0.

# list is mutable
# list1 = ["Cisco", "Jupiter", "Avaya", 10, 10.5, -11]
# print(list1)
# list1[1] = "HP"
# print(list1)

# min & max operator for list
# list2 = [1,2,-22,5]
# print(min(list2))

# list2 = ["apple","bags","cyclops"]
# print(max(list2))

# list2 = ["Cisco", "Jupiter", "Avaya", 10, 10.5, -11]
# print(max(list2))

# ----------------------------------------------------------

# ADD & REMOVE ELEMENT FROM LIST

# append list
# list3 = ["Cisco", "Jupiter", "Avaya", 10, 10.5, -11]
# list3.append(100)
# print(list3)

# insert
# list3 = ["Cisco", "Jupiter", "Avaya", 10, 10.5, -11]
# list3.insert(2, "Nortel")
# print(list3)

# extend
# list1 = ["Cisco", "Jupiter", "Avaya"]
# list2 = [10, 10.5, -11]
# list1.extend(list2)
# print(list1)

# concate lists
# list1 = ["Cisco", "Jupiter", "Avaya"]
# list2 = [10, 10.5, -11]
# print(list1+list2)

# del
# list3 = ["Cisco", "Jupiter", "Avaya", 10, 10.5, -11]
# del list3[1]
# print(list3)

# pop
# list3 = ["Cisco", "Jupiter", "Avaya", 10, 10.5, -11]
# list3.pop(1)
# print(list3)

# remove
# list3 = ["Cisco", "Jupiter", "Avaya", 10, 10.5, -11]
# list3.remove("Avaya")
# print(list3)

# ----------------------------------------------------------

# FIND ELEMENT'S INDEX & COUNT THE ELEMENT

# index
# list3 = ["Cisco", "Jupiter", "Avaya", 10, 10.5, -11]
# print(list3.index(10.5))

# count
# list3 = ["Cisco", "Jupiter", "Avaya", 10, 10.5, -11, "Cisco"]
# print(list3.count("Cisco"))

# ----------------------------------------------------------

# SORTING LIST

# sorted()
# list1 = [3,5,2,1,7,4,11,67,24,32]
# print(sorted(list1))

# sorted() reverse
# list1 = [3,5,2,1,7,4,11,67,24,32]
# print(sorted(list1, reverse=True))

# ----------------------------------------------------------

# SLICES
# list1 = [1,2,3,"a","b","c"]
# print(list1[0:3])
# print(list1[3:6])
# print(list1[-6:-3])
# print(list1[-3:])