from rental_art import logo

class CashOnCash:
    def __init__(self):
        self.income_types = {}
        self.income_total = 0.0
        self.expense_types = {}
        self.expense_total = 0.0
        self.cashflow_total = 0.0
        self.cashoncash_roi = 0.0




#step 1: Income method

    def income(self):

        while True:
            try:
                #debug
                # print(self.income_types)
                # print(self.income_total)
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

                add_more_income = input("\nAdd more income? (type 'y' or 'n'): ")
                if add_more_income == 'n':
                    income_rounded = round(self.income_total, 2)
                    print(f"\nIncome total: {income_rounded}\n")
                    break
                else:
                    continue

            except ValueError:
                print("\nEnter a number!\n")


#step 2: Expenses method

    def expenses(self):
        # debug
        # print(self.expense_types)
        # print(self.expense_total)

        while True:
            try:
                begin_expenses = input("Begin expense calculation? 'y' or 'n': ")

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
                    print(f"\nExpenses total: {expense_rounded}\n")

                else:
                    print("\nInvalid amount entered.\n")
                    continue

            except ValueError:
                print("\nPlease enter a valid value!\n")
            

#step 3: Cash flow method

    def cash_flow(self):
        cash_flow_result = round((self.income_total - self.expense_total), 2)
        self.cashflow_total += cash_flow_result

        print(f"\nYour monthly cash flow is {cash_flow_result}")



#step 4: Cash on Cash ROI

    def roi_calc(self):
        pass




#rental_roi method

    def rental_roi(self):
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
                        print(f"\nIncome Total: {self.income_total}\n")
                        print(f"\nExpenses Total: {self.expense_total}\n")
                        print(f"\nMontly Cash Flow: {self.cashflow_total}")
                    elif menu_selection == 6:
                        print("Reset values")
                    elif menu_selection == 7:
                        print("\nThank you for using the Rental Income Calculator.")
                        break
                else:
                    print("\nInvalid choice. Please enter a number from 1 to 7.\n")

            except ValueError:
                print("\nInvalid input. Please enter a valid number jackass.\n")






#main function

def main():
    calc_roi = CashOnCash()
    calc_roi.rental_roi()



if __name__ == "__main__":
    main()