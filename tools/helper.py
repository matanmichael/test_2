# Define a class called "Numbers"
class Numbers:
    # Constructor (__init__) method for initializing the class
    def __init__(self):
        # Create an empty list to store numbers
        self.numbers = []
        
    # Method to get input from the user
    def get_input(self):
        # Loop to repeatedly prompt the user for input
        while True:
            try:
                # Prompt the user to enter a number and convert the input to a float
                num = int(input("Enter a number (or 'q' to finish): "))
                # Append the entered number to the list of numbers
                self.numbers.append(num)
            except ValueError:
                # Handle invalid input (non-numeric input)
                print("Invalid input. Please enter a valid number or 'q' to finish.")
                continue

            # Prompt the user whether they want to finish entering numbers
            finish_input = input("Do you want to finish? (y/n): ").strip().lower()
            if finish_input == 'y':
                # Break out of the loop if the user wants to finish
                break

    # Method to find the largest number among the entered numbers
    def find_largest_number(self):
        # Check if the list of numbers is empty
        if not self.numbers:
            return None

        # Initialize the largest number with the first element in the list
        largest = self.numbers[0]
        # Loop through the list of numbers to find the largest
        for num in self.numbers:
            if num > largest:
                largest = num

        # Return the largest number
        return largest

    # Method to print the largest number
    def print_largest_number(self):
        self.get_input()
        # Call the find_largest_number method to get the largest number
        largest = self.find_largest_number()
        # Check if no numbers were entered
        if largest is None:
            print("No numbers were entered.")
        else:
            # Print the largest number
            print("The largest number is:", largest)

    # Static method to generate the Fibonacci sequence up to 'n' terms
    @staticmethod
    def fibonacci(n):
        fib_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

        while len(fib_sequence) < n:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)

        return fib_sequence

