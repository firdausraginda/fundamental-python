# DEFINITION
# set is an un-ordered collection of UNIQUE elements (list that have no duplicate element)

# ----------------------------------------------------------

# CREATE A SET

# create list and then convert to set
# list1 = [1,2,3,4,5,2,3]
# set1 = set(list1)
# print(set1)

# create set
# set1 = set([11,12,13,14,15,15,15,11])
# print(set1)

# create set with curly braces
# set1 = {11,12,13,14,15,15,15,11}
# print(set1)

# checking element is or is not a member of a set
# set1 = {11,12,13,14,15,15,15,11}
# print(11 in set1)
# print(99 not in set1)

# ----------------------------------------------------------

# ADD ELEMENT TO SET

# add
# set1 = {11,12,13,14,15,15,15,11}
# set1.add(28)
# print(set1)

# remove
# set1 = {11,12,13,14,15,15,15,11}
# set1.remove(12)
# print(set1)

# ----------------------------------------------------------

# OTHER BUILT-IN METHODS FOR SET

# intersection
# set1 = {1,2,3,4}
# set2 = {3,5,8}
# print(set1.intersection(set2))
# print(set2.intersection(set1))

# difference
# set1 = {1,2,3,4}
# set2 = {3,5,8}
# print(set1.difference(set2))
# print(set2.difference(set1))

# union
# set1 = {1,2,3,4}
# set2 = {3,5,8}
# set3 = set1.union(set2)
# print(set3)

# pop
# set1 = {1,2,3,4}
# set2 = set1.pop()
# print(set2)

# clear
# set1 = {1,2,3,4}
# set1.clear()
# print(set1)

# ----------------------------------------------------------

# FROZENSETS

# frozenset is immutable version of set
# list1 = [1,2,3,4]
# list2 = [3,4,7]
# fs1 = frozenset(list1)
# fs2 = frozenset(list2)
# print(fs1)
# print(fs2)

# but intersection, difference, & union method still works bc not modify the set
# print(fs1.intersection(fs2))
# print(fs2.difference(fs1))
# print(fs2.union(fs1))