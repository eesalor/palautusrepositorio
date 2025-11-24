class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def _score_to_text(self, score):
        scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return scores[score]

    def get_advantage_or_win(self, difference):
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            if self.player1_score < 3:
                score = self._score_to_text(self.player1_score) + "-All"
            else:
                score = "Deuce"

        else:
            if self.player1_score >= 4 or self.player2_score >= 4:
                difference = self.player1_score - self.player2_score
                score = self.get_advantage_or_win(difference)
            else:
                score = self._score_to_text(self.player1_score) + "-" + self._score_to_text(self.player2_score)

        return score
