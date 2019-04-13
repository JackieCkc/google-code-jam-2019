class Solution:
    def gcd(self, a, b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def solve(self, arr):
        arr2 = set()
        for i, j in zip(arr, arr[1:]):
            if i != j:
                v = self.gcd(i, j)
                arr2.add(i//v)
                arr2.add(j//v)

        d = {}
        curr = 0
        arr2 = sorted(list(arr2))
        for e in arr2:
            d[e] = curr
            curr += 1

        for j in range(26):
            v = arr2[j]
            ok = True
            ans = ''

            for k in arr:
                if k % v != 0:
                    ok = False
                    break
                ans += chr(d[v] + ord('A'))
                v = k // v

            ans += chr(d[v] + ord('A'))

            if ok:
                return ans


t = int(input())
s = Solution()

for i in range(t):
    N, L = [int(e) for e in input().split(' ')]
    arr = [int(e) for e in input().split(' ')]
    print("Case #{}: {}".format(i + 1, s.solve(arr)))
