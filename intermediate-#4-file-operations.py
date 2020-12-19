# OPEN FILE MODE
# r: reading (default mode)
# w: writing
# a: appending
# b: binary
# x: exclusive creation

# ----------------------------------------------------------

myfile = open("./routers.txt", "r")
# print(myfile.mode) # print out the mode

# print(myfile.seek(0)) # setting the cursor to index 0
# print(myfile.tell()) # print out current cursor
# print(myfile.read(5)) # print first 5 char

# myfile.seek(0)
# print(myfile.readline()) # print per line
# print(myfile.readline()) # print per line
# print(myfile.readline()) # print per line

# myfile.seek(0)
# print(myfile.readlines()) # return a list contains data in all line

# ----------------------------------------------------------

# print only chart with 'a' char in the begining

# myfile = open("./routers.txt", "r")
# myfile.seek(0)

# for line in myfile.readlines():
#     if line.startswith('a'):
#         print(line)

# ----------------------------------------------------------

# HOW TO AVOID ERROR IN SPECIFYING PATH TO A FILE

# python has a set of special characters also called escape sequences: '\n', '\t', '\U'

# the solution is to use double backslash: f = open('C:\\Users\\todo\\Desktop\\new\\test.txt', 'r')
# or can use r in front of the path: f = open(r'D:\Users\todo\file1.py', 'w')

# ----------------------------------------------------------

