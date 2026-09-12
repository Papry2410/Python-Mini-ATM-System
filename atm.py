print("Welcome to MY ATM")

Correct_Pin = 1234
Pin = int(input("Please Enter Your PIN: "))

# Check PIN
if Correct_Pin == Pin:
    print("Login Successful!")

    # Starting balance
    balance = 15000

    # Start loop here
    while True:

        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit\n")

        option = input("Choose an option: ")

        # Check balance
        if option == "1":
            print(f"Your Current Balance is: {balance} Tk")

        # Deposit
        elif option == "2":
            deposite = float(input("Enter Deposit Amount: "))

            # Update balance
            balance = balance + deposite

            print("Your New Balance is:", balance)

        # Withdraw
        elif option == "3":
            withdraw_money = float(input("Enter Withdraw Amount: "))

            # Update balance
            balance = balance - withdraw_money

            print("Your Current Balance is:", balance)

        # Exit
        elif option == "4":
            print("Thank You for using MY ATM")

            # Stop the loop
            break

        else:
            print("Invalid Option. Please try again!")

else:
    print("Invalid Password! Please try again.")
