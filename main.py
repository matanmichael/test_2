import tools.helper
import tools.strTools
import os
import pickle

def clear_console():
    os.system('cls')

def menu_script():
    print("Menu\nchoose one option")
    print("1.check the biggest number")
    print("2.show fibonacci array")
    print("3.show the longer array")
    print("4.change % and $")
    print("5.exit")
numbers = tools.helper.Numbers()
string_comparator = tools.strTools.StringComparator()        

def menu():
    while(True):
        
        menu_script()
        user_choice = input()
        clear_console()
        if user_choice == '1':
            numbers.print_largest_number()
        if user_choice == '2':
            num_chose= int(input("how many numbers you want to check: "))
            fib_result=numbers.fibonacci(num_chose)
            print("Fibonacci sequence:", fib_result)
        if user_choice == '3':
            input_str1 = input("Enter the first string: ")
            input_str2 = input("Enter the second string: ")
            result = string_comparator.get_longer_string(input_str1, input_str2)
            print("The longer string is:", result)
        if user_choice == '4':
            input_str = input("Enter a string with $ or % symbols: ")
            modified_str = string_comparator.replace_symbols(input_str)
            print("Modified string:", modified_str)
        if user_choice == '5':
            break

def main():
    menu()


if __name__ == '__main__':
    main()