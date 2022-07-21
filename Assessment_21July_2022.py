# Aarush wants to create his application in python. He just knows the basics and wants to create something useful. Finally, he decided to create a calculator. He added some extra functionality which was useful for him. Taking inspiration from Aarush, Create your functioning calculator.
# Note :
# Add the basic functions in the calculator like addition, subtraction, multiplication, and division.
# Put the entire program inside a loop so that users don’t need to run the program again and again to calculate anything.
# Handle all the exceptions.

# Add basic calc functions. Put inside a loop. Fix user errors.


while 2 > 1:
    print("Enter the corresponding number of the operation you would wish to perform : ")
    userinput = int(input("1 for Addition, 2 for Subtraction, 3 for multiplication, 4 for division : "))

    if userinput > 4:
        print("Invalid input")
        break

    numinput = int(input("Enter the 1st number = "))
    num2input = int(input("Enter the 2nd number = "))

    if userinput == 1:
        result_add = numinput + num2input
        print("You have selected 1) Addition. The result of", numinput, "and", num2input, "is equal to", result_add)

    if userinput == 2:
        result_subtract = numinput - num2input
        print("You have selected 2) Subtraction. The result of", numinput, "and", num2input, "is equal to",
              result_subtract)

    if userinput == 3:
        result_multiply = numinput * num2input
        print("You have selected 3) Multiply. The result of", numinput, "and", num2input, "is equal to",
              result_multiply)

    if userinput == 4:
        result_divide = numinput / num2input
        print("You have selected 4) Divide. The result of", numinput, "and", num2input, "is equal to", result_divide)

    print("End of program.")

    run_consent = input("Would you like to run the program again? Y for Yes, N for No = ")

    if run_consent == 'Y':
        pass
    else:
        print("Program has stopped")
        exit()

