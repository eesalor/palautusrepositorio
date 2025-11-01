import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual("Kurri", player.name)
    
    def test_search_returns_none_when_player_not_found(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(3, len(team_players))

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(5)
        self.assertEqual(5, len(top_players))

    def test_top_returns_players_in_correct_order(self):
        top_players = self.stats.top(3)
        self.assertEqual("Gretzky", top_players[0].name)
        self.assertEqual("Lemieux", top_players[1].name)
        self.assertEqual("Yzerman", top_players[2].name)

    def test_top_with_points_sorting(self):
        top_players = self.stats.top(3, sort_by=SortBy.POINTS)
        self.assertEqual("Gretzky", top_players[0].name)
        self.assertEqual("Lemieux", top_players[1].name)
        self.assertEqual("Yzerman", top_players[2].name)

    def test_top_with_goals_sorting(self):
        top_players = self.stats.top(3, sort_by=SortBy.GOALS)
        self.assertEqual("Lemieux", top_players[0].name)
        self.assertEqual("Yzerman", top_players[1].name)
        self.assertEqual("Kurri", top_players[2].name)

    def test_top_with_assists_sorting(self):
        top_players = self.stats.top(3, sort_by=SortBy.ASSISTS)
        self.assertEqual("Gretzky", top_players[0].name)
        self.assertEqual("Yzerman", top_players[1].name)
        self.assertEqual("Lemieux", top_players[2].name)

    def test_top_with_invalid_sorting_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.stats.top(3, sort_by="INVALID_SORTING")