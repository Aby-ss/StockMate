from datetime import datetime

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
    stocklvl = Table.grid(expand=True)
    stocklvl.add_column("Product", justify="left")
    stocklvl.add_column("Supplier", justify="left")
    stocklvl.add_column("Amount / Units", justify="right")
    
    stocklvl.add_row("Product", "Supplier", "Amount / Units")
    stocklvl.add_row(" ", " ", " ")

    stocklvl.add_row("Oreo", "Mondelēz International, Inc", "500 boxes")
    stocklvl.add_row("Lays crisps", "PepsiCo", "200 boxes")
    stocklvl.add_row("Almarai Milk", "Almarai", "250 bottles")
    stocklvl.add_row("H/S Shampoo", "Procter & Gamble", "200 bottles")
    stocklvl.add_row("Soap", "XYZ International", "400 boxes")
    stocklvl.add_row("Arwa Water", "Al Ahlia Group", "1000 bottles")

    stock_levels = Panel(stocklvl, title = "Stock Levels", title_align = "left", box = box.SQUARE, border_style = "bold white")
    
    return stock_levels

def expiration():
    stock_grid = Table.grid(expand=True)
    stock_grid.add_column("Product", justify="left")
    stock_grid.add_column("Prod. Date", justify="center")
    stock_grid.add_column("Exp. Date", justify="right")
    stock_grid.add_row("Product", "Prod. Date", "Exp. Date")
    stock_grid.add_row(" ", " ", " ")
    
    stock_grid.add_row("Oreos", "12/03/2023", "24/05/2023")
    stock_grid.add_row("Lays crisps", "26/03/2023", "19/04/2023")
    stock_grid.add_row("Almarai Milk", "29/03/2023", "12/05/2023")
    stock_grid.add_row("H/S Shampoo", "25/03/2023", "13/12/2023")
    stock_grid.add_row("Soap", "26/03/2023", "30/07/2023")
    stock_grid.add_row("Arwa Water", "25/03/2023", "11/12/2023")
    
    
    expirations = Panel(stock_grid, title = "Expiration Database", title_align = "left", box = box.SQUARE, border_style = "bold white")
    
    return expirations

def Stores():
    stat_grid = grid.Table(expand=True)
    stat_grid.add_column("Store No.", justify="left")
    stat_grid.add_column("Location", justify="left")
    stat_grid.add_column("Status", justify="center")
    stat_grid.add_column("Overall Stock", justify="center")
    
    stat_grid.add_row("Store No.", "Location", "Status", "Overall Stock")
    stat_grid.add_row(" ", " ", " ", " ")
    stat_grid.add_row(" ", " ", " ", " ")

    stat_grid.add_row("01", "45th Law Street, North", "[b green]Open[/]", "[b yellow]Sustainable[/]")
        
    store_stats = Panel(stat_grid, title = "Store Database", title_align = "left", box = box.SQUARE, border_style = "bold white")
    
    return store_stats

layout["Header"].size = 3
layout["Lower"].size = 3
layout["Header"].update(Header())

layout["upper_Box1"].update(stock_level())
layout["upper_Box2"].update(expiration())
layout["Box2"].update(Stores())


print(layout)