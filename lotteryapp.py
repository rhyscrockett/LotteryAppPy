from lotterygenerator import random_ticket     # needed for the random generator
from lotteryreader import winning_numbers      # needed for the csv reader
from lotterychecker import find_winning_numbers # needed for the checker function
from timer import Timer                       # needed for timing functions
import os

def clean_results():
    open("results.txt", "w").close() # wipe the contents of results txt for each program execution

def main():
    # Start timer and call the random function
    gentime = Timer()
    gentime.start()
    myticket = random_ticket() # this is a set
    gentime.stop()

    print("Your ticket numbers:", myticket)
    
    # Start another timer and call the reader function
    readtime = Timer()
    # main loop (for each file in dir, if filename ends with csv
    for filename in os.listdir("Lottery-numbers-csv/"):
        readtime.start()
        if filename.endswith(".csv"):
            # parse CSV file and return 
            dataset = winning_numbers("Lottery-numbers-csv/" + filename)
            find_winning_numbers(myticket, dataset) # this should return totalmatchingnumbers to be used by the write to file function
            ### have the write to file function here (timer either side)
        readtime.stop()

if __name__ == '__main__':
    clean_results() # ensure results are clean before executing the code
    main()
    
