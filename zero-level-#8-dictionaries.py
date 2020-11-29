# DEFINITION
# dictionary is an unordered set of key-value pairs, seperated by a comma and enclosed by curly braces
# dictionary is mutable
# dictionary is indexed by key

# declare dictionary
# key key be string or number or tuples
# dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
# print(dict1)
# dict2 = {1: "First Element", 2: "Second Element"}
# print(dict2)

# return specific value & add new value-pair
# dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
# print(dict1["Vendor"])
# dict1["RAM"] = "128"
# print(dict1)

# delete key-value pair from dictionary
# dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
# del dict1["Model"]
# print(dict1)

# check key in dictionary, case sensitive
# dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
# print("IOS" in dict1)
# print("ports" in dict1)

# keys, values, & items method in dictionary
# dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items()) #return list of tuples in dictionary

# access data return by keys, values, & items method in list format
# dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
# listKeys = list(dict1.keys())
# print(listKeys)
# listValues = list(dict1.values())
# print(listValues)
# listItems = list(dict1.items())
# print(listItems)

# convert data type
# num = 24
# f = 5.23
# string = 8
# list1 = [1,2,3]
# numString = str(num) # integer to string
# fString = str(f) # integer to string
# stringFloat = float(string) # string to float
# set1 = set(list1) # list to set
# tuple1 = tuple(list1) # list to tuple
# binary = bin(num) # integer to binary representation
# hexadecimal = hex(num) # integer to hexadecimal representation
# print(hexadecimal)
# print(type(hexadecimal))