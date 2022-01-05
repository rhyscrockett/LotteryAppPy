from lotterygenerator import randomticket     # needed for the random generator
from lotteryreader import winningnumbers      # needed for the csv reader
from lotterychecker import findwinningnumbers # needed for the checker function
from timer import Timer                       # needed for timing functions

# Start timer and call the random function
gentime = Timer()
gentime.start()
myticket = randomticket() # this is a set
gentime.stop()

# Start another timer and call the reader function
readtime = Timer()
readtime.start()
# these datasets are lists
dataset01 = winningnumbers("Lottery-numbers-csv/lotto-results-2001.csv")
#dataset02 = winningnumbers("Lottery-numbers-csv/lotto-results-2002.csv")
#dataset03 = winningnumbers("Lottery-numbers-csv/lotto-results-2003.csv")
readtime.stop()

print(myticket)

compare = [set(i) for i in dataset01] # set: unordered set unique
#print(compare) # print the new set list

# quick function to cycle through items in the compare dataset (will return a list of class: set)
ls = [type(item) for item in compare]
#print(ls)

print(findwinningnumbers(myticket, dataset01))  # print using function the winning nos from ticket and dataset
