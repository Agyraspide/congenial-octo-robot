s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cnt = 1
while cnt < 1000000:
    for i in range(len(s) - 1, -1, -1):
        if s[i] > s[i - 1]:
            m = min([m for m in s[i - 1:] if m > s[i - 1]])
            idx = s.index(m)
            s[i - 1], s[idx] = s[idx], s[i - 1]
            s[i:] = reversed(s[i:])
            break
    cnt += 1

print(''.join([str(i) for i in s]))
