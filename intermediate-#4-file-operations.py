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