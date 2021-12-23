import csv

def winningnumbers(filename):
    with open(filename) as csv_file:                                                                        # open the csv file parameter using an alias csv_file
        csv_reader = csv.reader(csv_file, delimiter=",")                                                    # create a csv_reader using the file and a delimiter
        line_count = 0                                                                                      # line counter set to 0
        for row in csv_reader:                                                                              # for every row in the csv_reader
            if line_count == 0:                                                                             # if the line counter == 0
                line_count += 1                                                                             # increment line counter so the reader can start to read the data
            else:                                                                                           # if line_counter is anything but 0
                print(f'{row[1]}: {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}')    # print each column data: data, then all 7 winning numbers
                line_count += 1                                                                             # increment the line_counter
        print(f'Processed {line_count} lines.\n')                                                           # final print statment displaying how many lines have been counted. Error checking.
