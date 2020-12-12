# ERROR IN PYTHON
# syntax error: occurs when you don'f follow python's syntax (forget to add colon or indentation is not proper)
# exceptions: exceptions are raised during the execution of the program interrupting the normal flow of the application

# ----------------------------------------------------------

# EXCEPTIONS

# correctly specify the error that may occurs
# for i in range(5):
#     try:
#         print(i / 0)
#     except ZeroDivisionError as e:
#         print(e, "Division by 0 is not allowed, sorry!")

# wrong specify the error that may occurs, will only return the plain old exception message (default error message)
# for i in range(5):
#     try:
#         print(i / 0)
#     except NameError as e:
#         print(e, "name error, sorry!")

# specify multiple exceptions
# for i in range(5):
#     try:
#         print(i / 0)
#     except ZeroDivisionError as e:
#         print(e, "division by zero is not allowed, sorry!")
#     except NameError as e:
#         print(e, "name error, sorry!")
#     except ValueError as e:
#         print(e, "value error, sorry!")

# catch all possible exceptions that my occurs
# for i in range(5):
#     try:
#         print(i / 0)
#     except:
#         print("error detected, sorry!")
#     else:
#         print("no exception detected")

# finally clause would still be executed regardless exception occurs or not
# for i in range(5):
#     try:
#         print(i / 0)
#     except:
#         print("error detected, sorry!")
#     finally:
#         print("i don't care, i'm getting printed anyway")