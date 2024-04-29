#hotel
import csv
with open("hotelRooms.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['roomType'], row['bed/s'])

menu=input ("***welcome to the hotel system***\n   please pick one of the following options\n 1 list of rooms ")
   
