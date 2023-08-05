from rental_art import logo

class CashOnCash:
    def __init__(self):
        self.income_types = {}
        self.income_total = 0.0
        self.expense_types = {}
        self.expense_total = 0.0
        self.cashflow_total = 0.0
        self.investment_total = 0.0


    def income(self):
        '''
        income() is a method that asks about the rental and 
        other income received from the property.
        '''
        while True:
            try:
                #Rental income
                rent_income = float(input("\nEnter the rental income amount or enter '000' to stop: "))
                if rent_income >= 1 and rent_income < 999999999:
                    self.income_types.update({"Rent": rent_income})
                    self.income_total += rent_income
                elif rent_income == 000:
                    break
                else:
                    print("\nPlease enter a valid rental income amount.\n")
                    continue

                #Additional Income
                other_income = float(input("\nEnter any other additional income. (Laundry, Storage, etc): "))
                if other_income > 1 and other_income < 999999999:
                    self.income_types.update({"Other": other_income})
                    self.income_total += other_income
                else:
                    print("\nPlease enter a valid additional income amount.\n")

                add_more_income = input("\nAdd more income? (type 'y' or 'n'): ").lower()
                if add_more_income == 'n':
                    income_rounded = round(self.income_total, 2)
                    print(f"\nIncome total: ${income_rounded}\n")
                    break
                else:
                    continue

            except ValueError:
                print("\nEnter a number!\n")


    def expenses(self):
        '''
        expenses() provides a lengthy conditional check for users to 
        input their monthly expenses in several different categories.
        '''
        while True:
            try:
                begin_expenses = input("Begin expense calculation? 'y' or 'n': ").lower()

                if begin_expenses == 'n':
                    break

                elif begin_expenses == 'y':
                    tax_exp = float(input("Enter property tax: "))
                    if tax_exp >= 0 and tax_exp < 99999:
                        self.expense_types.update({"Taxes": tax_exp})
                        self.expense_total += tax_exp
                    else:
                        print("\nPlease enter a valid tax amount.\n")
                    
                    ins_exp = float(input("Enter insurance cost: "))
                    if ins_exp >= 0 and ins_exp < 99999:
                        self.expense_types.update({"Insurance": ins_exp})
                        self.expense_total += ins_exp
                    else:
                        print("\nPlease enter a valid insurance amount.\n")
                    
                    util_exp = float(input("Enter Utility cost: "))
                    if util_exp >= 0 and util_exp < 9999:
                        self.expense_types.update({"Utilities": util_exp})
                        self.expense_total += util_exp
                    else:
                        print("\nPlease enter a valid utility amount.\n")

                    hoa_exp = float(input("Enter HOA fees: "))
                    if hoa_exp >= 0 and hoa_exp < 9999:
                        self.expense_types.update({"HOA": hoa_exp})
                        self.expense_total += hoa_exp
                    else:
                        print("\nPlease enter a valid HOA amount.\n")
                    
                    grounds_exp = float(input("Enter groundskeeping cost: "))
                    if grounds_exp >= 0 and grounds_exp < 9999:
                        self.expense_types.update({"Groundskeeping": grounds_exp})
                        self.expense_total += grounds_exp
                    else:
                        print("\nPlease enter a valid groundskeeping amount.\n")
                    
                    vac_exp = float(input("Enter vacancy expense (savings for vacant periods): "))
                    if vac_exp >= 0 and vac_exp < 999999:
                        self.expense_types.update({"Vacancy": vac_exp})
                        self.expense_total += vac_exp
                    else:
                        print("\nPlease enter a valid vacancy amount.\n")
                        
                    repair_exp = float(input("Enter repair expense: "))
                    if repair_exp >= 0 and repair_exp < 9999999:
                        self.expense_types.update({"Repairs": repair_exp})
                        self.expense_total += repair_exp
                    else:
                        print("\nPlease enter a valid repairs amount.\n")
                        
                    cap_exp = float(input("Enter Capital Expenditures amount: "))
                    if cap_exp >= 0 and cap_exp < 9999999:
                        self.expense_types.update({"CapEx": cap_exp})
                        self.expense_total += cap_exp
                    else:
                        print("\nPlease enter a valid CapEx amount.\n")

                    mgmt_exp = float(input("Enter property management amount: "))
                    if mgmt_exp >= 0 and mgmt_exp < 999999:
                        self.expense_types.update({"Prop Mgmt": mgmt_exp})
                        self.expense_total += mgmt_exp
                    else:
                        print("\nPlease enter a valid property management amount.\n")

                    mort_exp = float(input("Enter your mortgage: "))
                    if mort_exp >= 0 and mort_exp < 999999999:
                        self.expense_types.update({"Mortgage": mort_exp})
                        self.expense_total += mort_exp
                    else:
                        print("\nPlease enter a valid utility amount.\n")

                    expense_rounded = round(self.expense_total, 2)
                    print(f"\nExpenses total: ${expense_rounded}\n")

                else:
                    print("\nInvalid amount entered.\n")
                    continue

            except ValueError:
                print("\nPlease enter a valid value!\n")
            


    def cash_flow(self):
        '''
        cash_flow() is a simple method to calculate the monthly cash flow of the 
        rental.
        '''
        cash_flow_result = round((self.income_total - self.expense_total), 2)
        self.cashflow_total += cash_flow_result

        print(f"\nYour monthly cash flow is ${cash_flow_result}")



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
                        self.cash_flow()
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