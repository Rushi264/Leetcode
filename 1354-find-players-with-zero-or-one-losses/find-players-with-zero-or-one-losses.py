class Solution:
    def findWinners(self, matches):
        if not matches:
            return [[], []]

        win_count = {}
        lose_count = {}

        for winner, loser in matches:
            win_count[winner] = win_count.get(winner, 0) + 1
            lose_count[loser] = lose_count.get(loser, 0) + 1

        # Players who never lost
        never_lost = [player for player in win_count if player not in lose_count]

        # Players who lost exactly once
        lost_once = [player for player, count in lose_count.items() if count == 1]

        return [sorted(never_lost), sorted(lost_once)]
