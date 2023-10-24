class Solution:
    # too slow
    def winnerOfGame(self, colors: str) -> bool:
        self.colors = colors

        def helper(char):
            for i in range(len(self.colors)):
                if 0 < i < len(self.colors) - 1 and self.colors[i] == self.colors[i - 1] == self.colors[
                    i + 1] == char:
                    self.colors = self.colors[:i] + self.colors[i + 1:]
                    return True
            return False

        player = 1
        while True:
            if player == 1:
                if not helper('A'):
                    return False
            else:
                if not helper('B'):
                    return True
            player *= -1

    def winnerOfGame(self, colors: str) -> bool:
        aCount = 0
        bCount = 0
        for i in range(1, len(colors)-1):
            if colors[i] == colors[i-1] == colors[i+1]:
                if colors[i] == 'A':
                    aCount += 1
                else:
                    bCount += 1
        if aCount <= bCount:
            return False
        return True
