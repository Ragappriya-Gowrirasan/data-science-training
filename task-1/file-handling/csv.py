import csv

# Data to write to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 22, 'Los Angeles']
]

# Open the CSV file for writing
with open('output.csv', 'w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    
    # Write the data to the CSV file
    for row in data:
        writer.writerow(row)
