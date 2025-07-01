old_safe = 463

def neg(diffs, sign_dif):
    if diffs[sign_dif] == abs(diffs[sign_dif]): return False
    return True


def same_sign(resulting_option, previous_sign_diff):
    if (resulting_option > 0 and previous_sign_diff < 0) or (resulting_option < 0 and previous_sign_diff > 0):
        return False
    if previous_sign_diff == 0:
        return False
    return True

def xtrem(dif):
    if abs(dif) > 3: return True
    return False


def xtremes(diffs):
    result_inds = []
    for i, dif in enumerate(diffs):
        if xtrem(dif):
            result_inds.append(i)    
    return result_inds
            
        

    # if xtrem(beg) or xtrem(end):
    #     if not (xtrem(beg) and xtrem(end)):
    #         return True
    # return False

# 400 more than one, 404 is no sign diff
def one_sign_off(diffs):
    result_ind = 404
    positives, negatives, zeros = 0, 0, 0
    first_zero, first_pos, first_neg = -1, -1, -1
    more_than_1 = 10000
    for i, dif in enumerate(diffs):
        if dif == 0:
            zeros += 1
            if zeros == 1: 
                first_zero = i
            else: 
                first_zero = more_than_1
        elif abs(dif) == dif:
            positives += 1
            if positives == 1: 
                first_pos = i 
            else: 
                first_pos = more_than_1
        elif abs(dif) != dif:
            negatives += 1
            if negatives == 1: 
                first_neg = i 
            else: 
                first_neg = more_than_1
    one_diff = False
    two_multiples = False
    for first_diff in [first_zero, first_pos, first_neg]:
        # print("  ", first_diff)
        if first_diff != more_than_1 and first_diff != -1:
            if one_diff == True:  # already found a sign diff and we can't have 2
                result_ind = 400
                break
            else:
                result_ind = first_diff
                one_diff = True
        if first_diff == more_than_1 and two_multiples == True: return 400
        if first_diff == more_than_1: two_multiples = True
    return result_ind

def calc_res(diffs):
    end = len(diffs)  - 1
    sign_diff = one_sign_off(diffs)
    extremes = xtremes(diffs)
    # more than 2 extremes - impossible
    if len(extremes) > 2: return False
    # multiple sign diffs (0 -1 1 1 1) or multiple multiple signs (-1 -1 1 1) - impossible
    if sign_diff == 400: return False
    # no sign diffs - must be one extreme which is at an edge
    if sign_diff == 404:
        if len(extremes) == 1 and (extremes[0] == 0 or extremes[0] == end):
            return True
        else:
            return False
        
    # now we have 1 sign diff
    
    # if we have no extremes
    if not extremes:
        #  if sign diff is at the edge
        if sign_diff == 0 or sign_diff == end:
            return True
        # else GoTo 0/1 extreme
        
    # if we have 2 extremes ...
    if len(extremes) == 2:
        # they must be adjacent, they must add to <= 3, and the sign diff must be one of them
        if extremes[0] + 1 == extremes[1] and \
         abs(diffs[extremes[0]] + diffs[extremes[1]]) <= 3 and \
         sign_diff in extremes: 
            return True
        else:
            return False
        
    # now we have 1 sign diff and 0/1 extreme
    if extremes and (extremes[0] == sign_diff + 1 or extremes[0] == sign_diff - 1):
        opt = diffs[sign_diff] + diffs[extremes[0]]
        if not xtrem(opt) and opt != 0 and not same_sign(opt, diffs[sign_diff]):
            return True
    elif not extremes:
        opt1 = diffs[sign_diff] + diffs[sign_diff + 1]
        opt2 = diffs[sign_diff] + diffs[sign_diff - 1]
        if not xtrem(opt1) and opt1 != 0 and not same_sign(opt1, diffs[sign_diff]):
            return True
        if not xtrem(opt2) and opt2 != 0 and not same_sign(opt2, diffs[sign_diff]):
            return True
 
    return False
            

with open("day 2/unsafe_diffs.txt", "r") as f:
    mat = [list(map(int, line.split(" "))) for line in f.read().splitlines()]
    result = old_safe
    for diffs in mat:
        # print(diffs, "Sign: ", one_sign_off(diffs), "Xtreme: ", xtremes(diffs))
        safe = calc_res(diffs)
        if safe: result += 1
        # print(safe)
        # pass
    print(result)
    # print(calc_res([3, 3, -1, -4]))


                
