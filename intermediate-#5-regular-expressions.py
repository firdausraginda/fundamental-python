# regex is represented by a special syntax that helps find and match a pattern inside the string
# reference: https://www.tutorialspoint.com/python3/python_reg_expressions.htm
# . = any characters except a newline character
# + = 1 or more repetitions of the expression before it
# * = 0 or more repetitions of the expression before it
# () = any pair of parentheses matches the regular expression in between them
# ? = match the characters without include the whitespace if there's any
# \d = match any decimal digit from 0 to 9
# \D = match any NON decimal digit from 0 to 9
# \s = matches any whitespace character whether it is a space, a tab, or a newline character
# \S = matches any NON whitespace character whether
# {2,} = python should expect 2 or more occurrences of the pattern preceding the curly braces. Not typing the comma inside curly braces, meaning python expect exactly 2 repetitions of the previous pattern.
# {1,3} = python expect occurrs either 1, 2, or 3 times
# \w = matches any of characters  (lowercase a to z, uppercase a to z, number 0 to 9, underscore)
# \W = matches any NON word characters
# ^ = matches the start of the string
# $ = matches the end of the string
# \. = character escaping, meaning we want to match actual dot in a string. This also works for question mark, plus sign, parentheses, & any other characters that also have a special meaning in regular expressions.

# ----------------------------------------------------------

# MATCH()
# match checks for a match only at the beginning of the string
# re.match(pattern, string, optional flags)

# import re
# mystr = 'You can learn any programming language, whether it is Python2, Python3, Perl, Java, Javascript or PHP.'
# a = re.match('You', mystr)
# print(a.group())
# a = re.match('you', mystr, re.I) # ignoring the case sensitive as the third argument in the method
# print(a.group())

# ----------------------------------------------------------

# SEARCH()
# search checks for a match anywhere in the string
# re.search(pattern, string, optional flags)

# import re
# mystr = '22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222     L'
# a = re.search(r'(.+?) +(\d) +(.+?)\s{2,} (\w)*', mystr)
# print(a.group(0)) # return all characters
# print(a.group(1)) # (.+?)
# print(a.group(2)) # (\d)
# print(a.group(3)) # (.+?)\s{2,}
# print(a.group(4)) # (\w)*

# match start & end of the string
# import re
# mystr2 = 'I enjoy doing Python 3'
# start = re.search(r'^[A-Z]\s\D{5}', mystr2)
# end = re.search(r'[A-Z][a-z]{5}\s\d$', mystr2)
# print(start.group())
# print(end.group())

# ----------------------------------------------------------

# FINDALL()
# return a list of the pattern that were matched

# import re
# mystr = '22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222   31.54.24.98   L'
# a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", mystr)
# print(a)
# a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", mystr) # print by grouping
# print(a)

# match certain characters
# import re
# mystr2 = 'I enjoy doing Python 3'
# a = re.findall(r'[opq]', mystr2)
# print(a)
# b = re.findall(r'[PYH]', mystr2)
# print(b)
# c = re.findall(r'[913]', mystr2)
# print(c)
# d = re.findall(r'[^o]', mystr2) # match all characters except o
# print(d)

# ----------------------------------------------------------

# SUB()
# replace all occurrences of the specified pattern in the target string with another string that you provide as an argument

# import re
# mystr = '22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222     L'
# a = re.sub(r"\d", "7", mystr)
# print(a)

# ----------------------------------------------------------

# OR()

# import re
# a = 'I enjoy learning programming languages such as Java 3'
# result = re.search(r'\s(\w{20})\s|([A-Z][a-z]{3})\s\d', a)
# print(result.group(1)) # group 1 is empty because the rule is not match with any of char pattern in string
# print(result.group(2))

# ----------------------------------------------------------

# SPLIT() & SUBN()
# split: to split the string by the occurrences of certain pattern
# subn: similar to sub() but also return the number of replacement being made

# import re
# a = 'I enjoy learning programming languages such as Java 3'
# res = re.split(r' ', a) # split by whitespaces
# print(res)
# res2 = re.split(r'\s\w{2}\s',a) # split by char 'as'
# print(res2)
# res3 = re.subn(r'\s','-',a) # subn whitespaces to _
# print(res3)