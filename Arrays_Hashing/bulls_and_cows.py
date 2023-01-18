class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_counts = [0] * 10
        guess_counts = [0] * 10
        bulls = 0

        for sc, gc in zip(secret, guess):
            if sc == gc:
                bulls += 1
            else:
                secret_counts[int(sc)] += 1
                guess_counts[int(gc)] += 1

        cows = 0
        for i in range(10):
            cows += min(secret_counts[i], guess_counts[i])

        return str(bulls) + "A" + str(cows) + "B"
