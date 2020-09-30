# Simple Calculator
Simple calculator using python 3.8.5

num1 = int(input("Enter the first number"))

op = (input("Enter the operator"))

num2 = int(input("Enter the second number"))

if op == "+":
            print(num1 + num2)
          
elif op == "-":
             print(num1 - num2)
           
elif op == "*":
            print(num1 * num2)
           
elif op == "/":
              print(num1 / num2)
           
else:
    print("Invalid Operator")
