
import operator
add = operator.add
sub = operator.sub

with open("day 4/word_search.txt", "r") as f:
    matrix = f.readlines()
line_len = len(matrix[0]) 


def check_horiz(Xpos, op):
    if op(1,1) == 2:
        if Xpos[1] > line_len - 4:
            return False
    else:
        if Xpos[1] < 3:
           return False
    if matrix[Xpos[0]][op(Xpos[1],1)] == "M" and  matrix[Xpos[0]][op(Xpos[1],2)] == "A" and  matrix[Xpos[0]][op(Xpos[1],3)] == "S":
        return True
    return False

def check_verti(Xpos, op):
    if op(1,1) == 2:
        if Xpos[0] > len(matrix) - 4:
            return False
    else:
        if Xpos[0] < 3:
           return False
    if matrix[op(Xpos[0], 1)][Xpos[1]] == "M" and  matrix[op(Xpos[0], 2)][Xpos[1]] == "A" and  matrix[op(Xpos[0], 3)][Xpos[1]] == "S":
        return True
    return False

# (horiz, verti)
def check_diagn(Xpos, op1, op2):
    # rightdown
    if op1(1,1) == 2 and op2(1,1) == 2:
        if Xpos[1] > line_len - 4 or Xpos[0] > len(matrix) - 4:
            return False
    # rightup
    elif op1(1,1) == 2 and op2(1,1) == 0:
        if Xpos[1] > line_len - 4 or Xpos[0] < 3:
           return False
    # leftup
    elif op1(1,1) == 0 and op2(1,1) == 0:
        if Xpos[1] < 3 or Xpos[0] < 3:
           return False
    # leftdown
    elif op1(1,1) == 0 and op2(1,1) == 2:
        if Xpos[1] < 3 or Xpos[0] > len(matrix) - 4:
           return False
        
    if matrix[op2(Xpos[0], 1)][op1(Xpos[1],1)] == "M" and  matrix[op2(Xpos[0], 2)][op1(Xpos[1],2)] == "A" and  matrix[op2(Xpos[0], 3)][op1(Xpos[1],3)] == "S":
        return True
        
    return False

def check_all(Xpos):
    num_matches = 0
    for op1 in [add, sub]:
        if check_verti(Xpos, op1): num_matches += 1
        if check_horiz(Xpos, op1): num_matches += 1
        for op2 in [add, sub]:
            if check_diagn(Xpos, op1, op2): num_matches += 1
    return num_matches


result = 0 
for line_ind, line in enumerate(matrix):
    for char_ind, char in enumerate(line):
        if char == "X":
            result += check_all([line_ind, char_ind])
print(result)

    