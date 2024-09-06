# banking project

def showbalance(balance):
    print("****************")
    print(f"your balance is RS:{balance:2f}")
    print("****************")

def deposit():
    print("****************")
    amount = float(input("Enter the amount to be deposit:"))
    print("****************")

    if amount < 0:
        print("****************")
        print("invalid amount !!!!!")
        print("****************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("****************")
    amount = float(input("Enter the amount to be withdrawn:"))
    print("****************")

    if amount > balance:
        print("****************")
        print("Insufficient balance")
        print("****************")
        return 0
    elif amount < 0 :
        print("****************")
        print("Amount must to be greater than 0")
        print("****************")
        return 0
    else:
        return amount
    

def main():
    balance = 0

    running = True

    while running:

        print("-----------------")
        print("Banking Project")
        print("-----------------")

        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.Exit")


        #input options
        choice = input("Enter your choice:")

        if choice == '1':
            showbalance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            running = False
        else:
            print("****************")
            print("that is invalid!")
            print("****************")

    
    print("--------------------------")
    print("Thank you ! Have a nice day")
    print("--------------------------")

if __name__ == '__main__':
    main()