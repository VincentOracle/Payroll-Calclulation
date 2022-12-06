# NAME:Were Vincent
# SECTION:2
# DATE COMPLETED:22/11/2022

# PROBLEM 1:Simple Pay Calculation

# Function to calculate the Amount Pay for the Payroll
def amount_Pay():
    # Prompts for Employee name
    EmployeeName = input("Enter Employee name:")

    # Prompts for Hours Worked
    print("Enter Hours Worked: ")
    HoursWorked = float(
        input())

    # Prompts for Hourly Rate
    print("Enter Hourly Rate:")
    HourlyRate = float(
        input())

# Calculating payroll
    pay = HourlyRate*HoursWorked
    # Displaying  OUTPUT information
    print("Employee Name:"+EmployeeName)
    print("Hourly Rate : " + str(HourlyRate)+" Per Hour")
    print("Hours worked : " + str(HoursWorked))
    print("PAY : " + str(pay))


# Function Call
amount_Pay()


# PROBLEM 2:Calculating the average Miles per Gallon Obtained In A trip

# Function to calculate the Miles Per Gallon (MPG)
def miles_PerGallon():
    # Prompts for Car  name
    Car_Name = input("Enter Car name:")

    # Prompts for the A mount of Gas Used
    print("Enter the Amount of Gas Used: ")
    Amount_GasUsed = float(
        input())

    # Prompts for the Number Of Miles Driven
    print("Enter Number Of Miles Driven:")
    Number_MilesDriven = float(
        input())

# Calculating the Average Miles Per Gallon Obtained
    Miles_PerGallon = Number_MilesDriven / Amount_GasUsed
    # Displaying  OUTPUT information
    print("Car Name:"+Car_Name)
    print("Gas Used : " + str(Amount_GasUsed))
    print("Miles Driven: " + str(Number_MilesDriven))
    print("Miles Per Gallon: " + str(Miles_PerGallon))


    # Function call
miles_PerGallon()
# THE END
