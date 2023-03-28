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

layout["Header"].size = 3
layout["Lower"].size = 3
layout["Header"].update(Header())


print(layout)