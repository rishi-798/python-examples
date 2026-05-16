# Simple Bank System with PIN login

correct_pin = "1234"
attempts = 3

balance = 0

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("\nLogin successful!\n")
        break
    else:
        attempts -= 1
        print("Wrong PIN. Attempts left:", attempts)

if attempts == 0:
    print("Too many failed attempts. Account locked.")
else:

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposited:", amount)
            else:
                print("Invalid amount!")

        elif choice == "2":
            amount = float(input("Enter withdraw amount: "))
            if amount > balance:
                print("Not enough money!")
            elif amount > 0:
                balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Invalid amount!")


        elif choice == "3":
            print("Current balance:", balance)


        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")