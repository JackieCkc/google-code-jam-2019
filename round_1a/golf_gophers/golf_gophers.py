from collections import Counter
import sys

T, N, M = map(int, input().split())
for _ in range(T):
    c = Counter()
    nums = [3, 5, 7, 11, 13, 16, 17]
    remainders = []
    for n in nums:
        print(' '.join([str(n)] * 18))
        sys.stdout.flush()
        res = map(int, input().split())
        remainders.append(sum(res) % n)

    ans = M
    for i in range(1, M + 1):
        s = True
        for j, n in enumerate(nums):
            if i % n != remainders[j]:
                s = False
                break
        if s:
            print(i)
            sys.stdout.flush()
            input()
            break
