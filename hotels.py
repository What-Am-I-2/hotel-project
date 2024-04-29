#hotel
import csv
# Provide the full path to the CSV file
with open("hotelRooms.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
menu = input("***welcome to the hotel system***\n   please pick one of the following options\n 1 list of rooms ")
