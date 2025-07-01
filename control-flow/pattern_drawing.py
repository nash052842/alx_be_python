# pattern_drawing.py

def main():
    try:
        rows = int(input("Enter the number of rows: "))

        # Drawing the pattern
        for i in range(1, rows + 1):
            print("*" * i)

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
