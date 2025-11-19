print("Exception Handling Menu")

while True:
    print("\nChoose an exception to demonstrate:")
    print("1. Division by Zero")
    print("2. ValueError - Invalid integer conversion")
    print("3. IndexError - List index out of range")
    print("4. KeyError - Dictionary key not found")
    print("5. FileNotFoundError - File not found")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 / num2
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Invalid number entered.")

    elif choice == '2':
        try:
            s = input("Enter a number to convert to int: ")
            num = int(s)
            print(f"Converted: {num}")
        except ValueError:
            print("Error: Cannot convert to integer.")

    elif choice == '3':
        try:
            my_list = [1, 2, 3]
            index = int(input("Enter index to access (0-2): "))
            print(f"Value: {my_list[index]}")
        except IndexError:
            print("Error: Index out of range.")
        except ValueError:
            print("Error: Invalid index.")

    elif choice == '4':
        try:
            my_dict = {"a": 1, "b": 2}
            key = input("Enter key (a or b): ")
            print(f"Value: {my_dict[key]}")
        except KeyError:
            print("Error: Key not found.")

    elif choice == '5':
        try:
            filename = input("Enter filename to open: ")
            with open(filename, "r") as f:
                content = f.read()
                print("File content:", content[:50])
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"Error: {e}")

print("\nDone.")