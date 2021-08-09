#!/usr/bin/env python3

def add(x, y):
    answer = x + y
    print(answer)

def subtract(x, y):
    
    answer = x - y
    print(answer)

def divide(x, y):
    answer = x / y
    print(answer)

def multiply(x, y):
    answer = x * y
    print(answer)

def main():
    while True:
        try:
            x = float(input("Enter in a number: "))
            y= float(input("Enter ANOTHER  number: "))
            break
        except:
            print("Invalid input, try again.")

    operation = ""
    while(operation != "add" and operation != "subtract" and operation != "divide" and operation != "multiply"):
        operation = input("What operation would like to perform? OPTIONS: 'add', 'subtract','divide','multiply': ").lower()

    if(operation == "add"):
        add(x, y)
    elif(operation == "subtract"):
        subtract(x, y)
    elif(operation == "divide"):
        if y != 0:
            divide(x, y)
        else:
            print("You can't divide by zero!")
    elif(operation == "multiply"):
        multiply(x, y)
    else:
        print("use a valid OPTION")

if __name__ == "__main__":
    main()

