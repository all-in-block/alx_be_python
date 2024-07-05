def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    
    shopping_list = []
    
    while True:
        display_menu()
        choice = int(input("What is your choice (1/2/3/4)? "))
        if choice == 1:
            new_item = input("enter the item name ")
            shopping_list.append(new_item)
        elif choice == 2:
            toremove = input("enter the item name ")
            if toremove in shopping_list:
                shopping_list.remove(toremove)
            else :
                 print("item not found ")
        elif choice == 3:
            for i in range(len(shopping_list)):
                print(shopping_list[i])
        elif choice == 4:
            print("goodby")
            break
        else:
            print("enter a valid number ")       
main()    