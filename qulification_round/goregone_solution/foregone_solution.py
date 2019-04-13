T = int(input())

for i in range(T):
    N = input()
    A, B = '', ''
    for c in N:
        if c == '4':
            A += '1'
            B += '3'
        else:
            A += c
            B += '0'
    print("Case #{}: {} {}".format(i + 1, int(A), int(B)))
