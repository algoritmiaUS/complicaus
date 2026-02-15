n = int(input())

surnames = []
for _ in range(n):
    surname = input().strip()
    surnames.append(surname)

def dutch_key(name):
    for i, c in enumerate(name):
        if c.isupper():
            return name[i:]  # Return from the first uppercase letter
    return name  # In case there is no uppercase letter (although the problem guarantees there is one)

sorted_surnames = sorted(surnames, key=dutch_key)

for s in sorted_surnames:
    print(s)
