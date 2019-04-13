class Solution:
    def solve(self):
        input()
        ans = ''
        for c in input():
            ans += 'E' if c == 'S' else 'S'
        return ans


T = int(input())
for i in range(T):
    print("Case #{}: {}".format(i + 1, Solution().solve()))
