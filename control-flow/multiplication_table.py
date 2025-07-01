# multiplication_table.py

def main():
    try:
        # Prompt the user for a number
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print the multiplication table from 1 to 10
        for i in range(1, 11):
            result = number * i
            print(f"{number} * {i} = {result}")

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
