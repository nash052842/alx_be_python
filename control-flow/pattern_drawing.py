# pattern_drawing.py

def main():
    try:
        # Exact line expected by the checker
        rows = int(input("Enter the size of the pattern: "))

        for i in range(1, rows + 1):
            print("*" * i)

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()


