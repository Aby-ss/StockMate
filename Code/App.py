from datetime import datetime
import csv

from rich import print
from rich import box
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.live import Live

from rich.traceback import install
install(show_locals=True)

layout = Layout()

layout.split_column(
    Layout(name = "Header"),
    Layout(name = "Body"),
    Layout(name = "Lower")
)

layout["Body"].split_row(
    Layout(name = "Box1"),
    Layout(name = "Box2")
)

layout["Box1"].split_column(
    Layout(name = "upper_Box1"),
    Layout(name = "upper_Box2")
)

layout["Box2"].split_column(
    Layout(name = "lower_Box1"),
    Layout(name = "lower_Box2")
)

class Header:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Stock[/]Mate",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="green on black")
    
def stock_level():

    stock_levels = Panel("", title = "Stock Levels", title_align = "left", box = box.SQUARE, border_style = "bold white")
    
    return stock_levels

def stock():
    stock_grid = Table()

    # open CSV file
    with open('file.csv', 'r') as csvfile:
        # create a CSV reader object
        csvreader = csv.reader(csvfile)

        # get header row and add to table
        header = next(csvreader)
        stock_grid.add_column(header[0], justify='left', no_wrap=True)
        stock_grid.add_column(header[1], justify='left', no_wrap=True)
        stock_grid.add_column(header[2], justify='left', no_wrap=True)
        stock_grid.add_column(header[3], justify='left', no_wrap=True)

        # loop through rows in CSV file and add to table
        for row in csvreader:
            stock_grid.add_row(row[0], row[1], row[2], row[3])
    
    
    stocklvl = Panel(stock_grid, title = "Stock Database", title_align = "left", box = box.SQUARE, border_style = "bold white")
    
    return stocklvl

def style_cell(cell_value):
    if cell_value.lower() == 'open':
        text = Text(cell_value, style="bold green")
    elif cell_value.lower() == 'close':
        text = Text(cell_value, style="bold red")
    elif cell_value.lower() == 'full':
        text = Text(cell_value, style="green")
    elif cell_value.lower() == 'empty':
        text = Text(cell_value, style="red")
    elif cell_value.lower() == 'medium':
        text = Text(cell_value, style="yellow")
    else:
        text = Text(cell_value)
    return text

def Stores():
    stat_grid = Table(show_header=True, header_style="bold")

    # Open the CSV file and read the contents
    with open('StoreData.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)

        # Add the headers to the table
        for header in headers:
            stat_grid.add_column(header)

        # Add the data to the table
        for row in reader:
            stat_grid.add_row(*[style_cell(cell) for cell in row])

    store_stats = Panel(stat_grid, title = "Store Database", title_align = "left", box = box.SQUARE, border_style = "bold white")
    
    return store_stats

def test_table():
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
            
        return Panel(table, title = "Random Test", box = box.SQUARE, border_style = "bold white")

layout["Header"].size = 3
layout["Lower"].size = 3
layout["Header"].update(Header())

layout["upper_Box1"].update(stock())
layout["upper_Box2"].update(test_table())
layout["lower_Box1"].update(Stores())


print(layout)