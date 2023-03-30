import csv
from rich.console import Console
from rich.table import Table

# create console object
console = Console()

# create table object
table = Table()

# open CSV file
with open('file.csv', 'r') as csvfile:
    # create a CSV reader object
    csvreader = csv.reader(csvfile)

    # get header row and add to table
    header = next(csvreader)
    table.add_column(header[0], justify='left', no_wrap=True)
    table.add_column(header[1], justify='left', no_wrap=True)
    table.add_column(header[2], justify='left', no_wrap=True)
    table.add_column(header[3], justify='left', no_wrap=True)

    # loop through rows in CSV file and add to table
    for row in csvreader:
        table.add_row(row[0], row[1], row[2], row[3])

# print table to console
console.print(table)