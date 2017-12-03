import os
import csv
import string


totalvotes = 0
candunique = []
candvotecount = []
candvotepercent = []
electsummary = []
candsummary = []
prevotepercent = 0
precand = ''

 # Grab electiondata CSV file
electdataCSV = input("Enter the file name:( Both csv and .py file should be in the same folder (Ex:'xxxxx.csv')) ")

# Open electiondata csv file
with open(electdataCSV, 'r') as csvFile:

    csvReader = csv.reader(csvFile, delimiter=',')
    # Skip headers
    next(csvReader, None)

#Looping through each line of csv file        
    for row in csvReader:
#Get Total Votes and Increment
        totalvotes = totalvotes + 1
        candidatex = row[2]
#Collect all unique candidates into a list
        if (candidatex not in candunique):
            candunique.append(candidatex)
#Pepare Summary data list
electsummary.append("Election Results")
electsummary.append("-------------------------")
electsummary.append("Total Votes: " + str(totalvotes))
electsummary.append("-------------------------")

#Looping through candidate list
for candidate in candunique:
    votecount = 0
    votespercent = 0
# Open current electiondata file
    with open(electdataCSV, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        # Skip headers
        next(csvReader, None)
        for row in csvReader:
# Determine no. of votes and % votes for each candidate
            if (str(row[2]) == str(candidate)):
                votecount = votecount + 1
        votespercent = round((votecount/totalvotes)*100,2)
#Determine Winner
        if (votespercent > prevotepercent):
            winner = candidate
        precand = candidate
        prevotepercent = votespercent 
        candvotesummary = str(candidate) + ":   " + str(votespercent) + "%     (" + str(votecount) + ")"                  
        electsummary.append(candvotesummary)
#Write to Summary List
electsummary.append("-------------------------")
electsummary.append("Winner:    " + str(winner))
electsummary.append("-------------------------")
#Print and Write Summary List
with open("Output.txt", "w") as text_file:
    for sent in electsummary:
#Write to an Output .txt file
        text_file.write(sent)
        text_file.write('\n')
#Print to terminal
        print(sent)

