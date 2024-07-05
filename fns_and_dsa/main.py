#main.py
from arithmetic_operations import perform_operation
operation = input("what kind of operation do you want to process?(add/subtract/multiply/divide) ").strip().lower()
num1 = float(input("enter num1 "))
num2 = float(input("enter num2 "))
result = perform_operation(num1, num2, operation)
print(f"result : {result}")