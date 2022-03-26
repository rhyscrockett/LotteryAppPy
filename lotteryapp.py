from lotterygenerator import randomticket     # needed for the random generator
from lotteryreader import winningnumbers      # needed for the csv reader
from lotterychecker import findwinningnumbers # needed for the checker function
from timer import Timer                       # needed for timing functions

def main():
    #start timer and call the random function
    #gentime = Timer()
    #gentime.start()
    myticket = randomticket() # this is a set (unique numbers)
    #gentime.stop()

    print("Your ticket numbers: ", myticket)

    #readtime = Timer()
    #readtime.start()
    # these datasets are lists
    dataset01 = winningnumbers("Lottery-numbers-csv/lotto-results-2001.csv")
    dataset02 = winningnumbers("Lottery-numbers-csv/lotto-results-2002.csv")
    dataset03 = winningnumbers("Lottery-numbers-csv/lotto-results-2003.csv")
    #readtime.stop()

    # quick function to cycle through items in the compare dataset (will return a list of class: set)
    #ls = [type(item) for item in compare]
    #print(ls)

    #compare = [set(i) for i in dataset01] # set: unordered set unique
    #print(compare) # print the new set list

    #import glob
    #path = 'Lottery-numbers-csv'
    #datasets = glob.glob(path + "/*.csv")
    #for d in datasets:
    #    findwinningnumbers(myticket, d)

    findwinningnumbers(myticket, dataset01)  # print using function the winning nos from ticket and dataset
    findwinningnumbers(myticket, dataset02)
    findwinningnumbers(myticket, dataset03)

if __name__ == '__main__':
    main()
