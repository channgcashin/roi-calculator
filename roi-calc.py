class ROI:
    def calcIncome(self):
        rental_income = int(input("What is your rental income: "))
        misc_income = int(input("Enter any other income ammounts if there are any: "))
        print("Total property income is " + str(rental_income + misc_income) + ".")
        print()
        return rental_income + misc_income

    def calcExpenses(self):
        tax = int(input("Enter property tax: "))
        insurance = int(input("Enter insurance cost: "))
        utilities_input = input("Do you pay for utilities (Y/N): ")

        if utilities_input.lower() == 'y':
            utilities_cost = int(input("How much do you spend on utilities: "))
        else:
            utilities_cost = 0
        
        vacancy = int(input("What is the vacancy cost: "))
        repairs = int(input("What is the repair cost: "))
        capex = int(input("What is your capital expenditure: "))
        manage = int(input("What is your property manage cost: "))
        mortgage = int(input("What is the property's mortgage: "))

        print("Total property expense is " + str(tax + insurance + utilities_cost + vacancy + repairs + capex + manage + mortgage) + ".")
        print()
        return tax + insurance + utilities_cost + vacancy + repairs + capex + manage + mortgage

    def calcInvestment(self):
        down = int(input("What was the down payment on the property: "))
        closing = int(input("What was the closing cost for the property: "))
        rehab = int(input("What was the rehabilitation budget for the property: "))
        
        print("Total property investment is " + str(down + closing + rehab) + ".")
        print()
        return down + closing + rehab

    def calcRoi(self, income, expenses, investment):
        cashflow = (income - expenses) * 12
        roi = (cashflow / investment) * 100
        
        print("Your return on invesment on this property is " + str(roi) + "%")
        print()
        return roi

roi = ROI()

user_income = roi.calcIncome()
user_expenses = roi.calcExpenses()
user_investment = roi.calcInvestment()

roi.calcRoi(user_income, user_expenses, user_investment)