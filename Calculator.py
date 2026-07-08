# this is the introduction and input section of code
print("-----Welcome to the caclulator-----")
num1 =int(input("--Enter your first number-- \t"))
num2 =int(input("--Enter your second number-- \t"))
operation = input("Choose between these operations: \n + \n - \n * \n / \n")

# this section will be the logical section in which operation performed based on option chosen
#adding a while loop for exception handling, part of new branch
while operation not in ["+" , "-" , "*" , "/"]:
    print("Invalid operation chosen")
    operation = operation = input("Choose between these operations: \n + \n - \n * \n / \n")

    if operation == "+":
        sum = num1 + num2
        print(f"The answer is {sum}")
    elif operation == "-":
        sum = num1 - num2
        print(f"The answer is {sum}")
    elif operation == "*":
        sum = num1 * num2
        print(f"The answer is {sum}")
    elif operation == "/":
        sum = num1 / num2
        print(f"The answer is {sum}")
    
