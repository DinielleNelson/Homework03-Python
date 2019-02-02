import os
import csv

csvpath = os.path.join("..","..","UCFLM201901DATA2","03-Python","Homework",
	"Instructions","PyBank","Resources","budget_data.csv")

def PyBank(test):

#The total number of months included in the dataset
	monthCount = sum(1 for line in test)

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period


	print("Financial Analysis")
	print("---------------------")
	print(f'Total Months: {monthCount}')

with open (csvpath,'r') as csvfile:
	csvreader = csv.reader(csvpath,delimiter=",")
	csvheader = next(csvreader)

	PyBank(csvreader)