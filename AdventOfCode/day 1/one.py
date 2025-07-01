list1, list2 = [], []

def solve(): 
    with open('day 1/input.txt') as f:
        for line in f:
            first, second = line.split("   ")
            list1.append(first)
            list2.append(second)
    list1int = list(map(int, list1))
    list2int = list(map(int, list2))

    list1int.sort()
    list2int.sort()

    result = 0
    for a, b in zip(list1int, list2int):
        result += abs(a - b)

    l1 = open("day 1/list1.txt", "w")
    l2 = open("day 1/list2.txt", "w")
    [l1.write(f"{num}\n") for num in list1int]
    [l2.write(f"{num}\n") for num in list2int]
    l1.close()
    l2.close()
    return result
print(solve())
