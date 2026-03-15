Number = int(input("Enter your first number: "))
Number2 = int(input("Enter your second number: "))

User_Choose = input("Choose your operations (add, subtract, multiply, divide): ")
if User_Choose == "add":
    print(f"The sum of {Number} and {Number2} is: {Number + Number2}")
elif User_Choose == "subtract":
    print(f"The difference of {Number} and {Number2} is: {Number - Number2}")
elif User_Choose == "multiply":
    print(f"The product of {Number} and {Number2} is: {Number * Number2}")
elif User_Choose == "divide":
    print(f"The quotient of {Number} and {Number2} is: {Number / Number2}")