# Object Oriented Programming (OOP)
# class: data type containing its own variables attributes and functions which in OOP called methods (instead of function)
# class is like a blueprint for creating objects
# object: is an instance of a defined class & the attribute is defined the state of that object
# class inheritance: new class may inherit all the names & functionalities from an existing class
# the class name use CamelCase

# 'init' uses double underscores, this is the way python identifies a special method
# self as parameter in 'init' function is a reference to the current instance of the class

# define class (MyRouter)
# class MyRouter(object):
#     "This is a class that describes the characteristics of a router."
#     def __init__(self, routername, model, serialno, ios): # init here is to initialize some variables & the method is called whenever we create a new instance of a class in which it resides.
#         self.routername = routername
#         self.model = model
#         self.serialno = serialno
#         self.ios = ios
    
#     def print_router(self, manuf_date):
#         print('The router name is: ', self.routername)
#         print('The router model is: ', self.model)
#         print('The serial number of: ', self.serialno)
#         print('The IOS version is: ', self.ios)
#         print('The model and date combined: ', self.model + ' ' + manuf_date)

# create new object (router1 & router2)
# router1 = MyRouter('R1', '2600', '123456', '12.4')
# router2 = MyRouter('R2', '7200', '101010', '12.2')

# set new value for an attribute
# router2.ios = '10.0'
# setattr(router2, "ios", 9.0)

# print an attribute
# print(router1.ios)
# print(getattr(router2, "ios"))

# delete an attribute
# delattr(router2, "ios")

# check whether object has attribute
# print(hasattr(router2, "ios"))

# call methods
# router1.print_router('01-01-2020')
# router2.print_router('03-03-2023')

# check whether object is an instance of a class
# print(isinstance(router2, MyRouter))