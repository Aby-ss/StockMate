from datetime import datetime
import csv

from rich import print
from rich import box
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
    stock_grid = Table.grid(expand=True)
    stock_grid.add_column("Product", justify="left")
    stock_grid.add_column("Prod. Date", justify="center")
    stock_grid.add_column("Exp. Date", justify="right")
    stock_grid.add_column("Supplier", justify="right")
    stock_grid.add_column("Amount / Units", justify="right")
    stock_grid.add_row("Product", "Prod. Date", "Exp. Date", "Supplier", "Amount / Units")
    stock_grid.add_row(" ", " ", " ", " ", " ")
    
    stock_grid.add_row("Oreos", "12/03/2023", "24/05/2023", "Mondelēz International, Inc", "500 boxes")
    stock_grid.add_row("Lays crisps", "26/03/2023", "19/04/2023", "PepsiCo", "200 boxes")
    stock_grid.add_row("Almarai Milk", "29/03/2023", "12/05/2023", "Almarai", "250 bottles")
    stock_grid.add_row("H/S Shampoo", "25/03/2023", "13/12/2023", "Procter & Gamble", "200 bottles")
    stock_grid.add_row("Soap", "26/03/2023", "30/07/2023", "XYZ International", "400 boxes")
    stock_grid.add_row("Arwa Water", "25/03/2023", "11/12/2023", "Al Ahlia Group", "1000 bottles")
    stock_grid.add_row("Masafi Water", "16/03/2023", "18/11/2023", "Masafi Group", "1000 bottles")
    stock_grid.add_row("Show Cleaner", "29/03/2023","28/06/2023", "Lulu HyperMarket", "500 boxes")
    stock_grid.add_row("Cloth Detergent", "25/03/2023", "26/06/2023", "Arial Group Int.", "400 bottles")
    stock_grid.add_row("Sweet Biscuits", "25/03/2023", "15/09/2023", "Nestle Group", "700 boxes")
    stock_grid.add_row("Cake Rusk", "16/03/2023", "25/06/2023", "Nestle Group", "800 boxes")
    
    
    expirations = Panel(stock_grid, title = "Expiration Database", title_align = "left", box = box.SQUARE, border_style = "bold white")
    
    return expirations

def Stores():
    stat_grid = Table.grid(expand=True)
    stat_grid.add_column("Store No.", justify="left")
    stat_grid.add_column("Location", justify="left")
    stat_grid.add_column("Status", justify="center")
    stat_grid.add_column("Overall Stock", justify="center")
    
    stat_grid.add_row("Store No.", "Location", "Status", "Overall Stock")
    stat_grid.add_row(" ", " ", " ", " ")
    stat_grid.add_row(" ", " ", " ", " ")

    stat_grid.add_row("01", "45th Law Street, North", "[b green]Open[/]", "[b green]Strong[/]")
    stat_grid.add_row("02", "66th street alleyway, South", "[b red]Close[/]", "[b red]Weak[/]")
    stat_grid.add_row("03", "City Center Mall, East", "[b green]Open[/]", "[b green]Strong[/]")
    stat_grid.add_row("04", "55th Wall Street Zafron Buildg., South", "[b red]Close[/]", "[b yellow]Sustainable[/]")
    stat_grid.add_row("05", "City Center Mall, South", "[b red]Close[/]", "[b green]Strong[/]")
    stat_grid.add_row("06", "Global Island street 55th, West", "[b green]Open[/]", "[b red]Weak[/]")
    stat_grid.add_row("07", "90th street Platinum Business Center, South-east", "[b green]Open[/]", "[b yellow]Sustainable[/]")
    stat_grid.add_row("08", "98th streeet Dukeburg, South", "[b red]Close[/]", "[b yellow]Sustainable[/]")
    stat_grid.add_row("09", "115th street alleyway Dukenburg, South-east", "[b green]Open[/]", "[b green]Strong[/]")
    stat_grid.add_row("010", "87th street alleyway, South", "[b red]Close[/]", "[b red]Weak[/]")
    stat_grid.add_row("011", "59th Broker House street, North", "[b green]Open[/]", "[b yellow]Empty[/]")
    stat_grid.add_row("012", "69th street alleyway 420th Buildg., South", "[b red]Close[/]", "[b red]Weak[/]")
        
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