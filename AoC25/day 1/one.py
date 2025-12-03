with open('day 1/input.txt') as f:
    lines = f.readlines()

def do_turn(start, rotation):
    non_remainder = start + rotation
    if non_remainder <= 99 and non_remainder >= 0:
        return non_remainder
    else:
        return non_remainder % 100

count = 0
start = 50
for turn in lines:
    dir = -1 if turn[0] == "L" else 1
    mag = int(turn[1:].strip())
    start = do_turn(start, mag*dir)
    if start == 0:
        count += 1 
print(count)