from collections import defaultdict

def clean_updates(updates):
    for i, line in enumerate(updates):
        string = line.strip()
        string_list = string.split(",")
        int_list = [int(x) for x in string_list]
        updates[i] = int_list

    return updates

def read_file(file):
    rules = []
    updates = []
    with open(file, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line == "\n":
            updates = clean_updates(lines[i+1:])
            break
        rules.append([int(x) for x in line.split("|")])

    return rules, updates
    
def rules_to_dic(rules):
    dic = defaultdict(list)
    for rule in rules:
       before, after = rule
       dic[after].append(before)
    # print(dic)
    return dic

def check_update(update, rule_dic):
    for i, num in enumerate(update):
        for supced in update[i+1:]:
            if supced in rule_dic[num]:
                return False
    # print(update)
    return True

def get_middle(update):
    return update[int(len(update)/2)]

def get_result(file):   
    result = 0
    rules, updates = read_file(file)
    rule_dic = rules_to_dic(rules)
    for update in updates:
        if check_update(update, rule_dic):
            result += get_middle(update)
    return result

# print(get_result("day 5/sample_.txt"))
print(get_result("day 5/ordering_rules.txt"))
# correct_order = [5,2,74,23]
# co_len = len(correct_order)

# def in_correct_order(update):
#     i = 0
#     j = 0
#     u_len= len(update)
#     while i < co_len and j < u_len:
        
#         if update[j] == correct_order[i]:
#             j += 1
#             i += 1
#         else:
#             i += 1

#     if j == u_len:
#         return True
#     return False

