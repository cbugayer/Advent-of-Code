from one import check_update, read_file, rules_to_dic, get_middle
from collections import deque

def get_result(file):   
    result = 0
    rules, updates = read_file(file)
    rule_dic = rules_to_dic(rules)
    for update in updates:
        if not check_update(update, rule_dic):
            # print(update)
            reorder(update, rule_dic)
            # print(update)
            result += get_middle(update)
    return result


def reorder(update, rule_dic):
    length = len(update)
    for i in range(length):
        for j, supced in enumerate(update[i+1:]):
            if supced in rule_dic[update[i]]:
                to_rotate = deque(update[i:j+i+2])
                to_rotate.rotate(1)
                update[i:j+i+2] = list(to_rotate)
                # print("rotated", i, j)
                # print(update)

print(get_result("day 5/ordering_rules.txt"))
# print(get_result("day 5/sample_.txt"))
