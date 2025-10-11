n = int(input().strip())
s = input().strip()

pushed = [(i, ch) for i, ch in enumerate(s) if ch != '.']
if not pushed:
    print(n)
else:
    standing = 0

    first_i, first_ch = pushed[0]
    if first_ch == 'R':
        standing += first_i

    for (i, a), (j, b) in zip(pushed, pushed[1:]):
        gap = j - i - 1
        if gap <= 0:
            continue
        if a == 'L' and b == 'R':
            standing += gap
        elif a == 'R' and b == 'L':
            if gap % 2 == 1:
                standing += 1

    last_i, last_ch = pushed[-1]
    tail = (n - 1) - last_i
    if last_ch == 'L':
        standing += tail

    print(standing)
