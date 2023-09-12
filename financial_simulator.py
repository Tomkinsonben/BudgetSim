import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Initialize a dictionary to store projected savings for different scenarios
projected_savings_dict = {}

def perform_analysis(monthly_income, expenses, scenario):
    # Calculate total expenses and remaining income
    total_expenses = sum(expenses.values())
    remaining_income = monthly_income - total_expenses
    
    # Display financial position
    print(f"Your monthly income is ${monthly_income}")
    print("Your expenses are:")
    for name, amount in expenses.items():
        print(f"{name}: ${amount}")
    print(f"Your remaining income after expenses is ${remaining_income}")

    # Analyze financial situation and provide recommendations
    if remaining_income < 0:
        print("You're running a deficit. Consider cutting down on some expenses.")
    elif remaining_income > 0 and remaining_income < 500:
        print("You're barely making ends meet. Consider creating an emergency fund.")
    elif remaining_income >= 500:
        print("You're in a good financial position. Consider investing.")
    
    # Create a pie chart for expenses
    labels = list(expenses.keys())
    sizes = list(expenses.values())
    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Distribution of Expenses')
    plt.show()

    # Create a bar chart for income vs total expenses
    labels = ['Income', 'Total Expenses']
    values = [monthly_income, total_expenses]
    plt.figure(figsize=(8, 5))
    sns.barplot(x=labels, y=values)
    plt.title('Income vs Total Expenses')
    plt.show()

    # Create a line graph for projected savings over 12 months
    months = list(range(1, 13))
    projected_savings = [remaining_income * month for month in months]
    projected_savings_dict[scenario] = projected_savings
    plt.figure(figsize=(10, 6))
    plt.plot(months, projected_savings)
    plt.xlabel('Months')
    plt.ylabel('Projected Savings')
    plt.title('Projected Savings Over 12 Months')
    plt.show()

    # Create a gauge chart for remaining income
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=remaining_income,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Remaining Income"},
        gauge={
            'axis': {'range': [None, monthly_income]},
            'steps': [
                {'range': [0, monthly_income * 0.3], 'color': "red"},
                {'range': [monthly_income * 0.3, monthly_income * 0.6], 'color': "yellow"},
                {'range': [monthly_income * 0.6, monthly_income], 'color': "green"}
            ]
        }
    ))
    fig.show()

# Initialize variables
monthly_income = float(input("Enter your monthly income: "))
expenses = {}
more_expenses = 'Y'

# Get expenses
while more_expenses.upper() == 'Y':
    expense_name = input("Enter the name of the expense: ")
    expense_amount = float(input(f"Enter the amount for {expense_name}: "))
    expenses[expense_name] = expense_amount
    more_expenses = input("Do you have more expenses? (Y/N): ")

# Call perform_analysis initially for the "current" scenario
perform_analysis(monthly_income, expenses, "current")

# Ask the user if they want to modify data
modify_data = input("Would you like to modify your income or expenses? (Y/N): ")

# Loop to allow the user to modify data
while modify_data.upper() == 'Y':
    choice = input("Would you like to modify 'income' or an 'expense'? ")
    
    if choice.lower() == 'income':
        monthly_income = float(input("Enter your new monthly income: "))
    elif choice.lower() == 'expense':
        expense_name = input("Which expense would you like to modify? ")
        if expense_name in expenses:
            new_amount = float(input(f"Enter the new amount for {expense_name}: "))
            expenses[expense_name] = new_amount
        else:
            print("That expense doesn't exist.")
    
    # Call perform_analysis after any modifications for the "new" scenario
    perform_analysis(monthly_income, expenses, "new")
    
    modify_data = input("Would you like to modify anything else? (Y/N): ")

# Plot comparison line graph if both scenarios exist
if "current" in projected_savings_dict and "new" in projected_savings_dict:
    months = list(range(1, 13))
    plt.figure(figsize=(10, 6))
    plt.plot(months, projected_savings_dict["current"], label='Current Scenario')
    plt.plot(months, projected_savings_dict["new"], label='New Scenario')
    plt.xlabel('Months')
    plt.ylabel('Projected Savings')
    plt.title('Projected Savings Comparison')
    plt.legend()
    plt.show()
