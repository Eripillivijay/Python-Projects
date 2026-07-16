# Expense Tracker

expensesList = []
print(" Welcome to the Expense Tracker : ")

while True:
    print("==MENU==")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))

    # 1. Add Expenses
    if(choice == 1):
        date = input("Expenses Date?: ")
        category = input("Catergory? : (Food, Travel, Entertainment, Books): ")
        description = input("Description: ")
        amount=float(input("Enter the Amount: "))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        expensesList.append(expense)
        print(" \n Done. Expense is addede successfully")

    # 2. View All Expenses
    elif(choice == 2):
        if(len(expensesList)== 0):
            print("No Expenses Added...")
        else:
            print("-----Here is the Expenses List------")
            count = 1
            for totalExpenses in expensesList:
                print(
                    f"Count {count} -> "
                    f"{totalExpenses['date']}, "
                    f"{totalExpenses['category']}, "
                    f"{totalExpenses['description']}, "
                    f"{totalExpenses['amount']}"
                )
                count = count + 1

    # 3. View Total Expenses
    elif(choice == 3):
        total = 0
        for eachExpense in expensesList:
            total = total + eachExpense["amount"]
        print(" \n TOTAL EXPENSES = ", total)

    # 4. Exit
    elif(choice == 4):
        print("Thank you for using our system")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")