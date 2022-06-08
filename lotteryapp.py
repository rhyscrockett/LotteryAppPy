from lotterygenerator import random_ticket                            # needed for the random generator
from lotteryreader import winning_numbers                             # needed for the csv reader
from lotterychecker import find_winning_numbers, save_winning_numbers # needed for the checker function
from timer import Timer                                               # needed for timing functions
import os

def clean_results():
    """Wipe the contents of results.txt for the program to append multiple datasets to one file during execution"""
    open("lotteryresults.txt", "w").close() # wipe the contents of results txt for each program execution

def main():
    """Main function. Generate a random ticket, start a timer, read CSV dataset, check for winning numbers, save file, stop timer."""
    # generate a random ticket to be used in the comparison with datasets
    ticket = random_ticket() # this is a set

    # Create timer and call the reader function
    readtime = Timer()
    # main loop (for each file in dir, if filename ends with csv
    for filename in os.listdir("Lottery-numbers-csv/"):
        if filename.endswith(".csv"):
            print("Reading", '"'+filename+'"')
            readtime.start()
            dataset = winning_numbers("Lottery-numbers-csv/" + filename) # parse file in folder using filename.csv
            fetch = find_winning_numbers(ticket, dataset) # returns totalmatchingnumbers
            save_winning_numbers(fetch, ticket) # save the contents of find_winning_numbers to results.txt
            readtime.stop()

if __name__ == '__main__':
    clean_results() # ensure results are clean before executing the code
    main() # main loop
