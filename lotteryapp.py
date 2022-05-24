from lotterygenerator import random_ticket     # needed for the random generator
from lotteryreader import winning_numbers      # needed for the csv reader
from lotterychecker import find_winning_numbers # needed for the checker function
from timer import Timer                       # needed for timing functions
import os

def main():
    """Main loop."""
    # Start timer and call the random function
    gentime = Timer()
    gentime.start()
    myticket = randomticket() # this is a set
    print("Your ticket numbers:", myticket)
    gentime.stop()

    # Start another timer and call the reader function
    readtime = Timer()
    # main loop (for each file in dir, if filename ends with csv
    for filename in os.listdir("Lottery-numbers-csv/"):
        if filename.endswith(".csv"):
            readtime.start()
            # parse CSV file and return 
            dataset = winningnumbers("Lottery-numbers-csv/" + filename)
            find_winning_numbers(myticket, dataset)
            readtime.stop()

if __name__ == '__main__':
    main()
