import os
import csv

csv_path = 'O:/Bootcamp/UCFLM201901DATA2/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv'



def pypoll(test):
	total_votes = 0
	vote_0 = 0
	vote_1 = 0
	vote_2 = 0
	vote_3 = 0
	vote_4 = 0
	vote_5 = 0

	candidate_list = []

	
	#The total number of votes cast
	for row in test:
		total_votes += 1

	# A complete list of candidates who received votes
		if row[2] not in candidate_list:
			candidate_list.append(row[2])
	
		# The total number of votes each candidate won
		elif row[2]==candidate_list[0]:
			vote_0 += 1
		elif row[2]==candidate_list[1]:
			vote_1 += 1
		elif row[2]==candidate_list[2]:
			vote_2 += 1
		elif row[2]==candidate_list[3]:
			vote_3 += 1
		#elif row[2]==candidate_list[4]:
		#	vote_4 += 1
		#elif row[2]==candidate_list[5]:
		#	vote_5 += 1
	
	
	# The percentage of votes each candidate won
	perc_0 = vote_0/total_votes * 100
	perc_1 = vote_1/total_votes * 100
	perc_2 = vote_2/total_votes * 100
	perc_3 = vote_3/total_votes * 100
	#perc_0 = vote_0/total_votes * 100	
	#perc_0 = vote_0/total_votes * 100

	vote_list = [vote_0, vote_1, vote_2, vote_3]

	# The winner of the election based on popular vote.	
	winner_votes = max(vote_list)

	for idx, val in enumerate(vote_list):
		if val == winner_votes:
			winner = candidate_list[idx]

	#print to terminal
	print("Election Results")
	print("-------------------")
	print(f'"Total Votes: "{total_votes}')
	print("-------------------")
	print(candidate_list)
	print(f'{candidate_list[0]}: {perc_0}% ({vote_0})')
	print(f'{candidate_list[1]}: {perc_1}% ({vote_1})')
	print(f'{candidate_list[2]}: {perc_2}% ({vote_2})')
	print(f'{candidate_list[3]}: {perc_3}% ({vote_3})')
	#print(f'{candidate_list[4]}: {perc_0}% ({vote_0})')
	#print(f'{candidate_list[5]}: {perc_0}% ({vote_0})')
	print("-------------------")
	print(f'"Winner: "{winner}')

	#print values to .txt
	outF = open("pyPoll.txt", "w")
	outF.write("Election Results\n")
	outF.write("-------------------\n")
	outF.write(f'"Total Votes: "{total_votes}\n')
	outF.write("-------------------\n")
	outF.write(f'{candidate_list[0]}: {perc_0}% ({vote_0})\n')
	outF.write(f'{candidate_list[1]}: {perc_1}% ({vote_1})\n')
	outF.write(f'{candidate_list[2]}: {perc_2}% ({vote_2})\n')
	outF.write(f'{candidate_list[3]}: {perc_3}% ({vote_3})\n')
	outF.write("-------------------\n")
	outF.write(f'"Winner: "{winner}')



with open (csv_path, 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	csv_header = next(csv_file)

	pypoll(csv_reader)