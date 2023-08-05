from rental_art import logo

class CashOnCash:
    def __init__(self):
        self.income_types = {}
        self.total_income = 0
        





#step 1: Income method

    def income(self):

        while True:
            try:
                print(self.income_types)
                print(self.total_income)
                #Rental income
                rent_income = int(input("Enter the rental income amount or enter '000' to stop: "))
                if rent_income > 1 and rent_income < 999999999:
                    self.income_types.update({"Rent": rent_income})
                    self.total_income += rent_income
                elif rent_income == 000:
                    break
                else:
                    print("\nPlease enter a valid rental income amount.\n")
                    continue

                #Additional Income
                other_income = int(input("\nEnter any other additional income. (Laundry, Storage, etc): "))
                if other_income > 1 and other_income < 999999999:
                    self.income_types.update({"Other": other_income})
                    self.total_income += other_income
                else:
                    print("\nPlease enter a valid additional income amount.\n")

                done_adding_income = input("Add more income? (type 'y' or 'n'): ")
                if done_adding_income == 'n':
                    break
                else:
                    continue

            except ValueError:
                print("Enter a number!")



#step 2: Expenses method

    def expenses(self):
        pass








#step 3: Cash flow method

    def cash_flow(self):
        pass







#step 4: Cash on Cash ROI

    def roi_calc(self):
        pass




#rental_roi method

    def rental_roi(self):
        print(logo)
        print("Welcome to the Rental Property Return on Investment (RoI) Calculator.")
        print("This calculator calculates RoI based on Income, Expenses, and Cash Flow.")
        while True:
            menu_selection = input("""Please choose from the following menus: \n
                1. Income
                2. Expenses
                3. Cash Flow
                4. RoI Calculation (Cash on Cash)
                5. Reset Values
                6. Quit \n""")
            
            try:

                menu_selection = int(menu_selection)

                if 1 <= menu_selection <= 6:

                    if menu_selection == 1:
                        self.income()
                    elif menu_selection == 2:
                        self.expenses()
                    elif menu_selection == 3:
                        self.cash_flow()
                    elif menu_selection == 4:
                        self.roi_calc()
                    elif menu_selection == 5:
                        print("Reset values")
                    elif menu_selection == 6:
                        print("\nThank you for using the Rental Income Calculator.")
                        break
                else:
                    print("\nInvalid choice. Please enter a number from 1 to 6.\n")
            except ValueError:
                print("\nInvalid input. Please enter a valid number jackass.\n")






#main function

def main():
    calc_roi = CashOnCash()
    calc_roi.rental_roi()



if __name__ == "__main__":
    main()