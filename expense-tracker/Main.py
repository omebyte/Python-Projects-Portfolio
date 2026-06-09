import json

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return {"income": 0, "expenses": []}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def add_income(data):
    amount = float(input("Enter income: "))
    data["income"] += amount
    save_data(data)

def add_expense(data):
    category = input("Category (food, transport, etc): ")
    amount = float(input("Amount: "))
    data["expenses"].append({"category": category, "amount": amount})
    save_data(data)

def show_summary(data):
    total_expense = sum(item["amount"] for item in data["expenses"])
    balance = data["income"] - total_expense

    print("\n--- SUMMARY ---")
    print("Income:", data["income"])
    print("Total Expenses:", total_expense)
    print("Balance:", balance)

def main():
    data = load_data()

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            show_summary(data)
        elif choice == "4":
            break

main()
