a = ['jerit baiju', 'joyal bobby', 'jojit thomas', 'anit baiju']
a = sorted(a)

index = []

for _ in a:
    if _[0] not in index:
        index.append(_[0])

print(index)