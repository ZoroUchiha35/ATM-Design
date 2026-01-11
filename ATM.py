#--ATM Design Implementation--

balance = 6000

while True:
    print("-----------------------------------")
    print("--------- Welcome to the ATM ------")
    print("-----------------------------------")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = input("Please select an option (1-4): ")

    if choice == '1':
        print(f"Your current balance is: ${balance}")

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: $"))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"${amount} withdrawn. New balance is: ${balance}")

    elif choice == '3':
        amount = float(input("Enter the amount to deposit: $"))
        balance += amount
        print(f"${amount} deposited. New balance is: ${balance}")

    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option selected. Please try again.")
