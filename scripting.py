import csv
import psycopg2

connect = psycopg2.connect("host=localhost dbname=home_db user=postgres")

cursor = connect.cursor()

with open("homes.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # Skip the header row.
    for row in csv_reader:
        cursor.execute("INSERT INTO home (sell, list, living, rooms, beds, baths, age, acres, taxes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
        connect.commit()
