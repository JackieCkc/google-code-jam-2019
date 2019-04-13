from collections import Counter, defaultdict

class Solution:
    def solve(self):
        n = int(input())
        words = []
        c = Counter()
        d = defaultdict(list)
        substrs = set()

        for _ in range(n):
            word = input()
            l = len(word)
            for i in range(l):
                substr = word[l-i-1:]
                c[substr] += 1
                d[substr].append(word)
                substrs.add(substr)
            words.append(word)

        ans = 0
        used = set()
        substrs = list(substrs)
        substrs.sort(key=lambda s: -len(s))
        for substr in substrs:
            if c[substr] <= 1:
                continue
            ww = d[substr]
            ans_arr = []
            for w in ww:
                if w in used:
                    continue
                ans_arr.append(w)
                if len(ans_arr) == 2:
                    ans += 2
                    used.add(ans_arr[0])
                    used.add(ans_arr[1])
        return ans


t = int(input())

for i in range(1, t + 1):
    ans = Solution().solve()
    print("Case #{}: {}".format(i, ans))
