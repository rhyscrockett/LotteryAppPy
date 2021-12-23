import csv

dataset = []

def winningnumbers(filename):
    with open(filename) as csv_file:                                      # open the csv file parameter using an alias csv_file
        csv_reader = csv.reader(csv_file, delimiter=",")                  # create a csv_reader using the file and a delimiter
        line_count = 0                                                    # line counter set to 0
        for row in csv_reader:                                            # for every row in the csv_reader
            if line_count == 0:                                           # if the line counter == 0
                line_count += 1                                           # increment line counter so the reader can start to read the data
            else:                                                         # if line_counter is anything but 0
                dataset.append(row[2])                                    # append numbers 1 through 7 to the dataset
                dataset.append(row[3])
                dataset.append(row[4])
                dataset.append(row[5])
                dataset.append(row[6])
                dataset.append(row[7])
                dataset.append(row[8])
                line_count += 1                                           # increment the line_counter

        csv_file.close()                                                  # close the csv reader
        print(f"Processed {line_count}")                                  # final print statment displaying how many lines have been counted. Error checking.
        
        numbers = [dataset[i:i+7] for i in range(0, len(dataset), 7)]     # slice magic to carve up the huge dataset of all winning numbers into each winning ticket
        print(numbers)                                                    # print the new formatted ticket numbers
