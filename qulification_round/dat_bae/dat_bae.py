import sys

T = int(input())

for _ in range(T):
    N, B, F = [int(e) for e in input().split(' ')]

    arr = []
    for j in range(32):
        arr.append(format(j, '#07b')[2:])

    res_arr = [''] * (N - B)
    for j in range(5):
        send = ''
        i = 0
        while len(send) < N:
            send += arr[i][j]
            i = (i + 1) % 32

        print(send)
        sys.stdout.flush()
        res = input()
        for i, c in enumerate(res):
            res_arr[i] += c

    broken = []
    i = j = 0
    curr = 0
    while j < len(res_arr):
        c = res_arr[j]
        if int(c, 2) != i:
            broken.append(str(curr))
        else:
            j += 1

        i = (i + 1) % 32
        curr += 1

    while len(broken) < B:
        broken.append(str(curr))
        curr += 1

    ans = ' '.join(broken)
    print(ans)
    sys.stdout.flush()
    input()
