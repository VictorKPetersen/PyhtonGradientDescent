import csv


class CsvHandler:

    def __init__(self): pass

    def readCSV(self):
        with open('\csvData\housePriceData.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)



