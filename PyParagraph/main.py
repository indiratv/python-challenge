import os
import re

totalwords =0
noofletters =0
printsummary =[]

filename = input("Enter the file name:( Both txt and .py file should be in the same folder (Ex:'xxxxx.txt')) ")
# Read in the text file
with open(filename, 'r') as txtreader:
	para = txtreader.read()
#Split at '.' to get no. of sentences
	noofsent = len(para.split(".")) - 1
#Split at '' to get no. of words
	noofword = len(para.split())
#Store all words in a list to count no. of letters
	wordlist = para.split()
#Prepare Summary data list
	printsummary.append("Paragraph Analysis")
	printsummary.append("-------------------------")
	printsummary.append("Approximate Word Count:     " + str(noofword))
	printsummary.append("Approximate Sentence Count:   " + str(noofsent))
	
#loop throughthe word list
	for word in wordlist:
#Get no. of letters
		noofletters = noofletters + len(word)
#Calculate avg. letter count
	avglettercount = noofletters/noofword
	printsummary.append("Average Letter Count:   " + str(avglettercount))	
#Calculate avg. sentence length
	avgsentencelength = noofword/noofsent
	printsummary.append("Average Sentence Length: " + str(avgsentencelength))
#Print and Write Summary List
with open("Output.txt", "w") as text_file:
    for sent in printsummary:
#Write to an Output .txt file
        text_file.write(sent)
        text_file.write('\n')
#Print to terminal
        print(sent)