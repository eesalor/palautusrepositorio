from player_reader import PlayerReader
from player_stats import PlayerStats
from console_io import ConsoleIO
from rich.console import Console
from rich.table import Table

def main():
    console = Console()
    while True:
        io = ConsoleIO()

        console.print("[cyan]Season[/cyan]", end=" ")
        console.print("[magenta][2018-19/2019-20/2020-21/2021-22/" \
        "2022-23/2023-24/2024-25/2025-26][/magenta] ", end="")
        season = io.read("")

        console.print("[cyan]Nationality[/cyan]", end=" ")
        console.print("[magenta][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/" \
        "SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/magenta] ", end="")
        nationality = io.read("")

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)

        table = Table(title=f"Season {season} NHL players from {nationality}")
        table.add_column("Player", justify="left", style="cyan", no_wrap=True)
        table.add_column("Team", justify="left", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="bold yellow")

        players = stats.top_scorers_by_nationality(nationality)

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        console.print(table)


if __name__ == "__main__":
    main()
