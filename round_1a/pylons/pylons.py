from random import shuffle

class Solution:
    def dfs(self, i, j, M, path):
        path.append((i + 1, j + 1))
        if len(path) == self.len:
            return "POSSIBLE", path

        shuffle(self.arr)
        for n in self.arr:
            i1, j1 = n // self.C, n % self.C
            if i1 == i or j1 == j or i - j == i1 - j1 or i + j == i1 + j1 or M[i1][j1] == 1:
                continue
            M[i1][j1] = 1
            ans, ans2 = self.dfs(i1, j1, M, path)
            M[i1][j1] = 0
            if ans2:
                return ans, ans2

        path.pop()
        return "IMPOSSIBLE", []

    def solve(self):
        self.R, self.C = map(int, input().split())
        self.len = self.R * self.C
        self.arr = list(range(self.len))

        M = [[0] * self.C for _ in range(self.R)]
        shuffle(self.arr)

        for n in self.arr:
            i, j = n // self.C, n % self.C
            M[i][j] = 1
            ans, arr = self.dfs(i, j, M, [])
            M[i][j] = 0
            if arr:
                return ans, arr
        return "IMPOSSIBLE", []


t = int(input())

for i in range(1, t + 1):
    ans, arr = Solution().solve()
    print("Case #{}: {}".format(i, ans))
    for i, j in arr:
        print(i, j)
