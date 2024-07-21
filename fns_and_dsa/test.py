def devide(num1,num2):
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return num1/num2


def main():

            num1 = int(input("enter num1 "))
            num2 = int(input("enter num2 "))
           
            result = devide(num1,num2)
            print(f"the devision of {num1} and {num2} is {result}")
        

main()