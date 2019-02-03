import os
import csv

csv_path = 'O:/Bootcamp/UCFLM201901DATA2/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv'


def pypoll(test):
	total_votes = 0
	candidate_list = []
	
	#The total number of votes cast
	for row in test:
		total_votes += 1

	# A complete list of candidates who received votes
		if row[2] not in candidate_list:
			candidate_list.append(row[2])
	
	# The percentage of votes each candidate won

	# The total number of votes each candidate won
		for item in candidate_list:
			print(sum(row[1])


	# The winner of the election based on popular vote.



	print("Election Results")
	print("-------------------")
	print(f'"Total Votes: "{total_votes}')
	print(candidate_list)

with open (csv_path, 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	csv_header = next(csv_file)

	pypoll(csv_reader)