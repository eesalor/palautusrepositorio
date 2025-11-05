import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append(player)

    def sort_by_points(player: Player):
        return player.points

    print("Players from FIN:")
    print()

    for player in sorted(players, key=sort_by_points, reverse=True):
        print(player)


if __name__ == "__main__":
    main()
