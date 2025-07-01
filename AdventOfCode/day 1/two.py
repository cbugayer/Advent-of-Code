with open("day 1/list1.txt", "r") as l1:
    list1 = [int(x) for x in l1.read().splitlines()]

with open("day 1/list2.txt", "r") as l2:
    list2 = [int(x) for x in l2.read().splitlines()]

result = 0
j = 0
dic = {}
for i, a in enumerate(list1):
    if a in dic.keys():
        result += dic[a]
        continue
    while j < len(list2) and list2[j] < a:
        j += 1
    while j < len(list2) and a == list2[j]:
        dic[a] = dic.get(a, 0) + a
        j += 1
    result += dic.get(a, 0)
print(result)


# Or simply
res = 0
for k in list1:
    res += k * list2.count(k)
print(res)


