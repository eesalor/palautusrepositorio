from player import Player

class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
        self._players = reader.get_players()
    
    def nationality(self, nationality_name):
        players_of_team = filter(
            lambda player: player.nationality == nationality_name,
            self.players
        )
        return list(players_of_team)
    
    def sort_by_points(self, player: Player):
        return player.points

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player in self._players:
            if player.nationality == nationality:
                players.append(player)
    
        return sorted(players, key=self.sort_by_points, reverse=True)