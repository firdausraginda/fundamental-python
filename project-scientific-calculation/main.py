import math

while True:
    print('''Choose the math operation:
            0 - Addition 
            1 - Substraction
            2 - Multiplication
            3 - Division
            4 - Modulo
            5 - Raising to a power
            6 - Square root
            7 - Logarithm''')
    
    oper = input("\nYour option from the menu: ")
    
    # Addition
    if oper == '0':
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is : " + str(val1 + val2) + '\n')
        
        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    # Substraction
    if oper == '1':
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is : " + str(val1 - val2) + '\n')
        
        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break
    
    # Multiplication
    if oper == '2':
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is : " + str(val1 * val2) + '\n')
        
        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break
    
    # Division
    if oper == '3':
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is : " + str(val1 / val2) + '\n')
        
        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break
    
    # Modulo
    if oper == '4':
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print('\nThe result is: ' + str(val1 % val2) + '\n')

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    # Raising to a power
    if oper == '5':
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print('\nThe result is: ' + str(math.pow(val1, val2)) + '\n')

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    # Square root
    if oper == '6':
        val1 = float(input("\nInput value for extracting the square root: "))

        print('\nThe result is: ' + str(math.sqrt(val1)) + '\n')

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break
    
    # Logarithm
    if oper == '7':
        val1 = float(input("\nInput value for calculating the logarithm to base 2: "))

        print('\nThe result is: ' + str(math.log(val1, 2)) + '\n')

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break
    
    # Handling invalid options
    else:
        print("\nInvalid option!")
        continue