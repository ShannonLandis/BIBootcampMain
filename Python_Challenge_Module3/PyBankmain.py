#Python_Challenge_Module3_PyBank
#Shannon Landis
# Dec 26, 2023

#*****************************************************************



#STILL HAVE TO WRITE OUT TO A FILE IN THE ANALYSIS folder
# DOES IT MATTER THAT MY FILE CANNOT BE REACHED USING ..



#*****************************************************************************************



# import libraries
import os
import csv

#read budget_data file stored in Resources folder
#budgetdata_csv = os.path.join("..", "Resources", "budget_data.csv")
budgetdata_csv = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "PyBank_Results.txt")


# create lists
monthRow = []
profitRow = []


# open file note comma delimiter and skip header row
with open(budgetdata_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader) 


    # Read through each row of data after the header and append values to lists
    for row in csv_reader:
        
        monthRow.append(row[0])
        profitRow.append(row[1])


# function to read through rows and calculate the total profit, average profit, min change in profit, max change in profit
def calcProfits(*profits):
    lengthProfits = len(profits)
    totalProfit = 0
    countProfit = 0
    maxProfit = 0
    lastProfit = 0
    changeProfit = 0
    lastChangeMaxProfit = 0
    lastChangeMinProfit = 0
    maxChangeProfit = 0
    minChangeProfit = 0
    totalChangeProfit = 0

    # enumerate is a python function that keeps track of the list row (count will be set to row of list)
    # since I'm passing the profitRow list to the function profitRow will equal the profit column from csv
    for count, profit in enumerate(profitRow): 
        totalProfit += int(profit)
        countProfit += 1

        # since the first row will not have a preceding row to calc a change in profit, set lastProfit to profit of first row
        if count == 0:
            lastProfit = int(profit)

        # now that we are on the second row of the list, we can calculate the change in profit
        if count > 0:
           changeProfit = int(profit) - int(lastProfit)
           totalChangeProfit += changeProfit
           
           lastProfit = int(profit)

        #keep resetting when change > previous max change, final will be max change
        if changeProfit > lastChangeMaxProfit:
            maxChangeProfit = changeProfit
            maxDate = monthRow[count]
          
            lastChangeMaxProfit = changeProfit


        #keep resetting when change < previous min change, final change will be min change
        if changeProfit < lastChangeMinProfit:
            minChangeProfit = changeProfit
            minDate = monthRow[count]
          
            lastChangeMinProfit = changeProfit

    # return results (0,1,2,3,4,5,6)   
    return totalProfit , countProfit, maxChangeProfit, maxDate, minChangeProfit, minDate, totalChangeProfit   # lengthProfits # returns total Profits


# set Total Months equal to the length of the month row list
TotalMonths = len(monthRow)

#print first few rows not set from function
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {TotalMonths}")

#set result variable to results from function
result = calcProfits([profitRow])


# read results from function into variables
totalProfitNew = int(result[0])

changeProfit = int(result[6])
numProfits = int(result[1]) - 1
averageProfit = round((changeProfit / numProfits), 2)
maxChangeProfit = int(result[2])
maxDate = str(result[3])
minChangeProfit = int(result[4])
minDate = str(result[5])


# print out results from function
print(f"Total:  ${totalProfitNew}")
print(f"Average Change:  ${averageProfit}")

print(f"Greatest Increase in Profits:  {maxDate} (${maxChangeProfit})")
print(f"Greatest Decrease in Profits:  {minDate} (${minChangeProfit})")



#Open text file to write out results
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months:  ${totalProfitNew}\n")
    txtfile.write(f"Total:  {TotalMonths}\n")
    txtfile.write(f"Average Change:  ${averageProfit}\n")
    txtfile.write(f"Greatest Increase in Profits:  {maxDate} (${maxChangeProfit})\n")
    txtfile.write(f"Greatest Decrease in Profits:  {minDate} (${minChangeProfit})")





# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)




