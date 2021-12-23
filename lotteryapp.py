from lotterygenerator import randomticket  # needed for the random generator
from lotteryreader import winningnumbers   # needed for the csv reader
from timer import Timer                    # needed for timing functions

# Start timer and call the random function
gentime = Timer()
gentime.start()
myticket = randomticket()
gentime.stop()

# Start another timer and call the reader function
readtime = Timer()
readtime.start()
dataset01 = winningnumbers("Lottery-numbers-csv/lotto-results-2001.csv")
dataset02 = winningnumbers("Lottery-numbers-csv/lotto-results-2002.csv")
dataset03 = winningnumbers("Lottery-numbers-csv/lotto-results-2003.csv")
readtime.stop()
