import random
import csv

# List of possible random names
names = ["Mario", "Luigi", "Peach", "Bowser", "Toad", "Waluigi", "Wario", "Huesitos", "DK", "Yoshi"]

# Shuffle the list of names
random.shuffle(names)

# Create a list of 10 rows, each containing 6 random values between 0 and 1
data = [[random.uniform(0, 1) for i in range(6)] for j in range(10)]

# Insert the unique random names in the first column
for i in range(len(data)):
    data[i].insert(0, names[i])

# Write the data to a CSV file
with open('random_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Soccer', 'Basketball', 'Kungfu', 'F1', 'Table Tenis', 'Archery'])
    for row in data:
        writer.writerow(row)
