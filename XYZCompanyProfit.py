
# NAME:
# FACULTY:
# NUMBER:
# WELCOME TO XYZ COMPANY PROFIT CALCULATION SYSTEM
# The System Helps in calculating the total profit generated by the end of the year by the Company.
# The System prompts for the value of total sales earned and calculate the profit generated.
# It then displays it to the Screen after Calculation.

# Total profit earned is calculated by the function total_profit()
def total_profit():
    # Prompts for sales person name
    name = input("Enter sales person name:")

# Prompts the entry of total sales projected
    print("Hello " + name + "!" +
          "Please Enter the Projected Total Sales Amount: ")

    TototalSalesAmt = float(
        input())

    print("Total sales Amount : " + str(TototalSalesAmt))

# Calculates the total Pofit Generated
    salesTax = (32.5/100)
    profit = TototalSalesAmt * float(salesTax)
# Calculates the total Expenses back to the Company
    expenses = TototalSalesAmt-profit
    print("Total Expenses is:" + str(expenses))
    print("Annual Profits :"+str(profit))


total_profit()