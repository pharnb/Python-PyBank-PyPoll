#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards 
# for accounting so the records are simple.)

import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')
#* Your task is to create a Python script that analyzes the records to calculate each of the following:
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    totalmonths = 0
    netamount = 0
    averagechangesum = 0
    lastmonth = 0
    monthchange = 0
    profit = 0
    losses = 0 
    for row in csvreader:
        thismonth = int(row[1])
        #print(f'this month {thismonth}')
        #  * The total number of months included in the dataset
        totalmonths += 1
        #  * The net total amount of "Profit/Losses" over the entire period
        netamount += thismonth
        #  * The average of the changes in "Profit/Losses" over the entire period part 1
        # thismonth - lastmonth, except first row
        if lastmonth == 0:
            lastmonth = thismonth
            #print(f'1 {row[0]} {lastmonth}')
        else:
            monthchange = thismonth - lastmonth
            lastmonth = thismonth
            #print(f'2 {row[0]} {monthchange}')
            averagechangesum += monthchange
        #  * The greatest increase in profits (date and amount) over the entire period
        if monthchange > profit:
            profit = monthchange
            profitmonth = row[0]
        #  * The greatest decrease in losses (date and amount) over the entire period
        if monthchange < losses:
            losses = monthchange
            lossesmonth = row[0]

    #  * The average of the changes in "Profit/Losses" over the entire period part 2
    # totalmonths-1 because (month2 - month1)/(1 month)
    averagechange = averagechangesum/(totalmonths-1)
    averagechange = round(averagechange, 2)
#* As an example, your analysis should look similar to the one below:

print("Financial Analysis")
print("-------------------")
print(f"Total Months:     {totalmonths}")
print(f"Total:            ${netamount}")
print(f"Average Change:   ${averagechange}")
print(f"Greatest Profits: {profitmonth} (${profit})")
print(f"Greatest Losses:  {lossesmonth} (${losses})")


#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
file1 = open("output.txt", "a")
file1.write("Financial Analysis\n")
file1.write("-------------------\n")
#file1.write("%s %i test\n" % (profitmonth, profit))
file1.write("Total Months:     %i\n" % (totalmonths))
file1.write("Total:            $%i\n" % (netamount))
file1.write("Average Change:   $%6.2f\n" % (averagechange))
file1.write("Greatest Profits: %s $%i\n" % (profitmonth, profit))
file1.write("Greatest Losses:  %s $%i\n" % (lossesmonth, losses))


file1.close()