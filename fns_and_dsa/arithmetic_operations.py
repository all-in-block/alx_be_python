#arithmetic_operations.py
def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return {num1 + num2}
        case "subtract":
            return {num1 - num2}
        case "multiply":
            return {num1 * num2}
        case "divide":
            if num2 == 0:
                print("num2 can not be 0")
            elif num2 != 0:
                return {num1 / num2}
        case _:
            print("not a valid choice")




