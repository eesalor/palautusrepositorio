from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats
from console_io import ConsoleIO

def prompt_season(io: ConsoleIO, console: Console):
    console.print("[cyan]Season[/cyan]", end=" ")
    console.print("[magenta][2018-19/2019-20/2020-21/2021-22/" \
    "2022-23/2023-24/2024-25/2025-26][/magenta] ", end="")
    season = io.read("")
    return season

def prompt_nationality(io: ConsoleIO, console: Console):
    console.print("[cyan]Season[/cyan]", end=" ")
    console.print("[magenta][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/" \
    "SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/magenta] ", end="")
    nationality = io.read("")
    return nationality

def make_table(title: str):
    table = Table(title=title)
    table.add_column("Player", justify="left", style="cyan", no_wrap=True)
    table.add_column("Team", justify="left", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="bold yellow")
    return table

def run_once(season, nationality, console):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    table = make_table(f"Season {season} NHL players from {nationality}")
    players = stats.top_scorers_by_nationality(nationality)
    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    console.print(table)

def main():
    console = Console()
    io = ConsoleIO()
    while True:
        season = prompt_season(io, console)
        nationality = prompt_nationality(io, console)
        run_once(season, nationality, console)

if __name__ == "__main__":
    main()
