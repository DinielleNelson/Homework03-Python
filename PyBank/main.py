import os
import csv

csv_path = os.path.join("..","..","UCFLM201901DATA2","03-Python","Homework",
	"Instructions","PyBank","Resources","budget_data.csv")

def pybank(test):

	month_count = 0
	net_total = 0
	net_last = 867884
	net_list = []
	net_max = 867884
	month_max = 1/1/2010
	net_min = 867884
	month_min = 1/1/2010

	for row in test:
		#The total number of months included in the dataset
		#Alternative: month_count = sum(1 for row in test)
		month_count +=1
		
		#The net total amount of "Profit/Losses" over the entire periods
		net_total += int(row[1])
		
		#The average of the changes in "Profit/Losses" over the entire period
		#net_list.append(row[1]+(row+1)[1])
		net_cur = int(row[1])
		net_diff = net_cur-net_last
		net_last = net_cur
		net_list.append(net_diff)
		net_avg = sum(net_list)/(month_count)

		#for row in net_list:
			#The greatest increase in profits (date and amount) over the entire period
		#	if int(row[1]) > net_max:
		#		month_max = row[0]
		#		net_max = int(row[1])

			#The greatest decrease in losses (date and amount) over the entire period
		#	if int(row[1]) < net_min:
		#		month_min = row[0]
		#		net_min = int(row[1])


	print("Financial Analysis")
	print("---------------------")
	print(f'Total Months: {month_count}')
	print(f'Net Total: ${net_total}')
	print(f'Average Change: ${net_avg}')
#	print(f'Greatest Increase in Profits: {month_max} (${net_max})')
#	print(f'Greatest Decrease in Profits: {month_min} (${net_min})')

with open (csv_path,'r') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=",")
	csv_header = next(csv_reader)

	pybank(csv_reader)