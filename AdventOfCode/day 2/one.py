
def check_dif(dif, pos):
    if dif == 0: return False
    if (abs(dif) == dif) != pos: return False
    if abs(dif) > 3: return False
    return True

result = 0
unsafes = []
with open("day 2/reports.txt", "r") as f:
    mat = [list(map(int, l.split())) for l in f.read().splitlines()]
    for line in mat:
        length = len(line)
        diffs = []
        for i in range(length):
            if i == length - 1:
                break
            diffs.append(line[i] - line[i+1])
        if all(check_dif(dif, abs(diffs[0]) == diffs[0]) for dif in diffs):
            result += 1
        else:
            unsafes.append(diffs)
with open("day 2/unsafe_diffs.txt", "w") as f:
    [f.write(f"{' '.join((str(x) for x in unsafe))}\n") for unsafe in unsafes]
print(result)
