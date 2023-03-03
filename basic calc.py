# function to add numbers
def add(n1, n2):
    return n1 + n2

# function to subtract numbers
def subtract(n1, n2):
    return n1 - n2

# function to multiply numbers
def multiply(n1, n2):
    return n1*n2

# function to divide numbers
def divide(n1, n2):
    return n1/n2

print("Select an option\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

while True:
    choice = input("Enter your choice: ")
    if choice.isdigit() == False:
        print("You can only enter a number from 1 to 4.")
        continue
    else:
        choice = int(choice)
        if choice < 1 or choice > 4:
            print("You can only enter a number from 1 to 4.")
            continue
        else:
            print("")
            break

while True:
    n1 = input("Enter a number: ")
    if n1.isdigit() == False:
        print("You can only enter a number.")
        continue
    else:
        n1 = int(n1)
        print("")
    n2 = input("Enter another number: ")
    if n2.isdigit == False:
        print("You can only enter a number.")
        continue
    else:
        n2 = int(n2)
    print("")
    if choice == 1:
        print(n1, "+", n2, "=", add(n1, n2))
    elif choice == 2:
        print(n1, "-", n2, "=", subtract(n1, n2))
    elif choice == 3:
        rint(n1, "*", n2, "=", multiply(n1, n2))
    else:
        print(n1, "/", n2, "=", divide(n1, n2))
    again = input("Do you want to perform another calculation (Y/N): ")
    if again.lower() == "y":
        continue
    else:
        break
