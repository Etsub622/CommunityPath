class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = zip(*matches)

        unique_winners = set(winners)
        unique_losers = set(losers)

        final_winners = []
        for w in unique_winners:
            if w not in unique_losers:
                final_winners.append(w)
        final_losers_counter = Counter(losers)

        final_losers = []
        for l, count in final_losers_counter.items():
            if count == 1:
                final_losers.append(l)


        final_winners.sort()
        final_losers.sort()

        output = [final_winners, final_losers]

        return output  















        