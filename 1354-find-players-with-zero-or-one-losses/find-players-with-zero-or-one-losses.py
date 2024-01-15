class Solution:
    def findWinners(self, matches):
        if matches is None:
            return [[], []]

        hashmap = {}
        total_set = set()

        for winner, loser in matches:
            # Update total set with winner and loser
            total_set.update([winner, loser])

            # Update hashmap for losers
            hashmap[loser] = hashmap.get(loser, 0) + 1

        list1 = [player for player in total_set if player not in hashmap]
        list2 = [loser for loser, count in hashmap.items() if count == 1]

        return [sorted(list1), sorted(list2)]
