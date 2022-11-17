
def deltion_distance(str1, str2):
    memo = {("", ""): 0}

    def dfs(s1, s2):
        tup = (s1, s2)
        if tup in memo:
            return memo[tup]
        if s1 == "":
            memo[tup] = len(s2)
            return memo[tup]
        if s2 == "":
            memo[tup] = len(s1)
            return memo[tup]

        if s1[0] == s2[0]:
            return dfs(s1[1:], s2[1:])

        left = 1 + dfs(s1[1:], s2)
        right = 1 + dfs(s1, s2[1:])
        memo[tup] = min(left, right)
        return memo[tup]


    return dfs(str1, str2)
