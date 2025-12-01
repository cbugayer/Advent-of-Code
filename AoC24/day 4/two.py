
import operator
add = operator.add
sub = operator.sub

with open("day 4/word_search.txt", "r") as f:
    matrix = f.readlines()
line_len = len(matrix[0]) 
matx_len = len(matrix)



def check_space(Apos):
    if Apos[0] == 0 or Apos [0] == matx_len - 1 or Apos[1] == 0 or Apos[1] == line_len - 1:
        return False
    return True

# Apos[line_ind, char_ind]
# \
def check_diagn(Apos, op1, op2):
    if not check_space(Apos): return False    
    if matrix[op1(Apos[0], 1)][op1(Apos[1],1)] == "M" and  matrix[op2(Apos[0], 1)][op2(Apos[1],1)] == "S":
        return True
    
    if matrix[op1(Apos[0], 1)][op1(Apos[1],1)] == "S" and  matrix[op2(Apos[0], 1)][op2(Apos[1],1)] == "M":
        return True
        
    return False
# /
def check_same(Apos):
    if matrix[add(Apos[0], 1)][add(Apos[1],1)] == "M" and  matrix[sub(Apos[0], 1)][sub(Apos[1],1)] == "S":
        return True
    if matrix[add(Apos[0], 1)][add(Apos[1],1)] == "S" and  matrix[sub(Apos[0], 1)][sub(Apos[1],1)] == "M":
        return True
    
    return False

def check_diff(Apos):
    if matrix[add(Apos[0], 1)][sub(Apos[1],1)] == "M" and  matrix[sub(Apos[0], 1)][add(Apos[1],1)] == "S":
        return True
    if matrix[add(Apos[0], 1)][sub(Apos[1],1)] == "S" and  matrix[sub(Apos[0], 1)][add(Apos[1],1)] == "M":
        return True
    
    return False

def check_cross(Apos):
    return check_same(Apos) and check_diff(Apos)


result = 0 
for line_ind, line in enumerate(matrix):
    for char_ind, char in enumerate(line):
        if char == "A" and check_space([line_ind, char_ind]) and check_cross([line_ind, char_ind]):
            result += 1
print(result)

    