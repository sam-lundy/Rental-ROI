from rental_art import logo

class CashOnCash:
    def __init__(self):
        self.income_type_store = {}
        self.income_total = 0.0
        self.expense_type_store = {}
        self.expense_total = 0.0
        self.cashflow_total = 0.0
        self.investment_total = 0.0


    def income(self):
        '''
        income() is a method that asks about the rental and 
        other income received from the property.
        '''
        income_types = ["Rent", "Laundry", "Storage", "Misc"]
        should_quit = False
        print("Enter 'q' at any time to quit adding income.")

        for income_type in income_types:
            if should_quit:
                break

            while True:
                try:
                    #Rental income
                    get_income = input(f"\nEnter the {income_type.lower()} income amount: ")

                    if get_income.lower() == 'q':
                        should_quit = True
                        break
                    
                    #Convert to float and check for valid amounts, add to dictionary and total
                    get_income = float(get_income)

                    #better way than 'if income >= 0 and income < 99999 imo'
                    if 0 <= get_income < 999999999:
                        self.income_type_store.update({income_type: get_income})
                        self.income_total += get_income
                        break

                    else:
                        print(f"\nPlease enter a valid {income_type} income amount.\n")
                        continue

                except ValueError:
                    print("\nEnter a number or 'q' to quit.\n")
                    continue

    def expenses(self):
        '''
        expenses() provides a lengthy conditional check for users to 
        input their monthly expenses in several different categories.
        '''
        expense_types = ["Tax", "Insurance", "Utilities", "HOA", "Groundskeeping", "Vacancy", 
                         "Repairs", "Capital Expenditure", "Property Management", "Morgage"]
        should_quit = False
        print("Enter 'q' at any time to quit adding income.")

        for expense_type in expense_types:
            if should_quit:
                break

            while True:
                try:
                    get_expense = input(f"\nEnter {expense_type} amount: ")

                    if get_expense.lower() == 'q':
                        should_quit = True
                        break

                    get_expense = float(get_expense)

                    if 0 <= get_expense < 999999:
                        self.expense_type_store.update({"Taxes": get_expense})
                        self.expense_total += get_expense
                        break

                    else:
                        print(f"\nPlease enter a valid {expense_type} income amount.\n")
                        continue

                except ValueError:
                    print("\nPlease enter a valid value!\n")
                    continue


    def roi_calc(self):
        '''
        roi_calc() provides an input/calculation structure to determine the 
        Return on Investment for the above values.
        '''
        while True:
            try:
                down_pmt = float(input("Enter your down payment: "))
                if down_pmt >= 0 and down_pmt < 9999999999:
                    self.investment_total += down_pmt
                closing_cost = float(input("Enter your closing costs: "))
                if closing_cost >= 0 and closing_cost < 999999:
                    self.investment_total += closing_cost
                rehab_budget = float(input("Enter your remodel budget: "))
                if rehab_budget >= 0 and rehab_budget < 99999999:
                    self.investment_total += rehab_budget
                misc_cost = float(input("Enter any miscellaneous costs: "))
                if misc_cost >= 0 and misc_cost < 9999999:
                    self.investment_total += misc_cost
                else:
                    print("\nPlease enter a valid amount.")
                    continue

                annual_flow = round(((self.cashflow_total * 12) / self.investment_total) * 100, 2)

                print(f"\nYour Cash on Cash Return on Investment (RoI) is: %{annual_flow}\n")
                break

            except ValueError:
                print("\nEnter a valid amount jackass!\n")
                continue



    def reset_values(self):
        '''
        reset_values provides functionality in order to reset the class attribute values to zero.
        '''
        while True:
            try:
                user_check = input("Are you sure you want to delete all your saved values? type 'y' or 'n': ").lower()

                if user_check == 'n':
                    break
                elif user_check == 'y':
                    self.income_types = {}
                    self.income_total = 0.0
                    self.expense_types = {}
                    self.expense_total = 0.0
                    self.cashflow_total = 0.0
                    self.cashoncash_roi = 0.0
                    print("Values reset...")
                    break
                else:
                    print("Please enter a valid selection.")
                    continue

            except ValueError:
                print("Enter only either y or n!")



    def rental_roi(self):
        '''
        rental_roi() is the main runner function of the program. Provides menu and 
        calls the methods for each selection provided.
        '''

        print(logo)
        print("Welcome to the Rental Property Return on Investment (RoI) Calculator.")
        print("This calculator calculates RoI based on Income, Expenses, and Cash Flow.")

        while True:
            menu_selection = input("""\nPlease choose from the following menus: \n
                1. Income
                2. Expenses
                3. View Cash Flow
                4. RoI Calculation (Cash on Cash)
                5. Print Values
                6. Reset Values
                7. Quit \n""")
            
            try:
                menu_selection = int(menu_selection)

                if 1 <= menu_selection <= 7:

                    if menu_selection == 1:
                        self.income()

                    elif menu_selection == 2:
                        self.expenses()

                    elif menu_selection == 3:
                        cash_flow_result = round((self.income_total - self.expense_total), 2)
                        self.cashflow_total += cash_flow_result
                        print(f"\nYour monthly cash flow is ${cash_flow_result}")

                    elif menu_selection == 4:
                        self.roi_calc()

                    elif menu_selection == 5:
                        print(f"\nIncome Total: ${self.income_total}")
                        print(f"Expenses Total: ${self.expense_total}")
                        print(f"Montly Cash Flow: ${self.cashflow_total}")
                        print(f"Investment Total: ${self.investment_total}\n")

                    elif menu_selection == 6:
                        self.reset_values()

                    elif menu_selection == 7:
                        print("\nThank you for using the Rental Income Calculator.")
                        break

                else:
                    print("\nInvalid choice. Please enter a number from 1 to 7.\n")

            except ValueError:
                print("\nInvalid input. Please enter a valid number jackass.\n")


def main():
    '''
    The main() function instantiates the object of class CashOnCash() and returns the method of rental_roi
    '''
    calc_roi = CashOnCash()
    calc_roi.rental_roi()


if __name__ == "__main__":
    main()