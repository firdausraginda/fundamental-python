# regex is represented by a special syntax that helps find and match a pattern inside the string
# . = any characters except a newline character
# + = 1 or more repetitions of the expression before it
# * = 0 or more repetitions of the expression before it
# () = any pair of parentheses matches the regular expression in between them
# ? = match the characters without include the whitespace if there's any
# \d = any decimal digit from 0 to 9
# \s = matches any whitespace character whether it is a space, a tab, or a newline character
# {2,} = python should expect 2 or more occurrences of the pattern preceding the curly braces. Not typing the comma inside curly braces, meaning python expect exactly 2 repetitions of the previous pattern.
# \w = matches any of characters  (lowercase a to z, uppercase a to z, number 0 to 9, underscore)

# ----------------------------------------------------------

# MATCH()
# match the string from the begining of the characters
# re.match(pattern, string, optional flags)

# import re

# mystr = 'You can learn any programming language, whether it is Python2, Python3, Perl, Java, Javascript or PHP.'

# a = re.match('You', mystr)
# print(a.group())

# a = re.match('you', mystr, re.I) # ignoring the case sensitive as the third argument in the method
# print(a.group())

# ----------------------------------------------------------

# SEARCH()
# re.search(pattern, string, optional flags)

# import re

# mystr = '22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222     L'

# a = re.search(r'(.+?) +(\d) +(.+?)\s{2,} (\w)*', mystr)

# print(a.group(0)) # return all characters
# print(a.group(1)) # (.+?)
# print(a.group(2)) # (\d)
# print(a.group(3)) # (.+?)\s{2,}
# print(a.group(4)) # (\w)*