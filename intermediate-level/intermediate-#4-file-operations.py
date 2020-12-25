# OPEN FILE MODE
# r: reading (default mode)
# w: writing
# a: appending
# b: binary
# x: exclusive creation

# ----------------------------------------------------------

# myfile = open("./routers.txt", "r")
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

# print data with 'a' char in the begining

# myfile = open("./routers.txt", "r")
# myfile.seek(0)

# for line in myfile.readlines():
#     if line.startswith('a'):
#         print(line)

# ----------------------------------------------------------

# HOW TO AVOID UNIQUECODE ERROR IN SPECIFYING PATH TO A FILE

# python has a set of special characters also called escape sequences: '\n', '\t', '\U'

# the solution is to use double backslash: f = open("C:\\Users\\todo\\Desktop\\new\\test.txt", "r")
# or can use r in front of the path: f = open(r"D:\Users\todo\file1.py", "w")

# ----------------------------------------------------------

# WRITING TO FILE

# newfile = open(r"./newfile.txt", "w") # write a file if not exist, replace if exist

# newfile.write('''I like Python! 
# Do you?
# ''') # write something inside the file

# newfile.close() # close write mode

# newfile = open(r"./newfile.txt", "r") # read file
# print(newfile.read())

# ----------------------------------------------------------

# APPENDING TO FILE

# newfile = open(r"./newfile.txt", "w") # write a file if not exist, replace if exist
# newfile.writelines(["Cisco", "Juniper", "HP"]) # write something in list

# newfile = open(r"./newfile.txt", "a") # append file
# newfile.write("this string was appended")
# newfile.close()

# ----------------------------------------------------------

# CLOSE AUTOMATICALLY USING WITH .. AS ..

# with open(r"./newfile.txt", "w") as f:
#     f.write("Hello Python!!!")

# res = open(r"./newfile.txt", "r")
# print(res.read()) # read file
# print(f.closed) # check whether it is closed or not

# ----------------------------------------------------------

# DELETING FILE CONTENTS

# read the length of the file content
# f = open("./text.txt")
# print(f.read())
# f.seek(0)
# print(len(f.read())) # print length of file content
# f.close()

# delete partial of the file content
# f = open("./text.txt", "r+") # open the file for reading & writing simultanously
# f.truncate(10) # delete all except the first 10 characters
# f.close()

# delete all the file content
# f = open("./text.txt", "r+") # open the file for reading & writing simultanously
# f.truncate() # delete all file content
# f.close()