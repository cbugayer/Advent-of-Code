import os

script_dir = os.path.dirname(os.path.abspath(__file__))
# with open(os.path.join(script_dir, 'sample.txt')) as f:
with open(os.path.join(script_dir, 'input.txt')) as f:
    lines = f.readlines()

rotations = []
for turn in lines:
    dir = -1 if turn[0] == "L" else 1
    mag = int(turn[1:].strip())
    rotations.append(mag*dir)


def count_zeros_in_turn(start, rotation):
    count = 0
    no_remainder = start + rotation
    times_around = abs(no_remainder // 100)
    end = no_remainder % 100
    count += times_around
    if end == 0 and rotation < 0:
        count += 1
    if start == 0 and rotation < 0:
        count -= 1
    return count, end

final = 0
start = 50
for rotation in rotations:
    if rotation == 0: 
        continue
    count, remainder = count_zeros_in_turn(start, rotation)
    final += count
    start = remainder
    # print(rotation, final, remainder)

print (final)

# testing
assert (1, 30) == count_zeros_in_turn(95, 35)
assert (2, 30) == count_zeros_in_turn(95, 135)
assert (0, 30) == count_zeros_in_turn(0, 30)
assert (1, 30) == count_zeros_in_turn(0, 130)
assert (3, 0) == count_zeros_in_turn(0, 300)
assert (1, 0) == count_zeros_in_turn(95, 5)
assert (0, 30) == count_zeros_in_turn(60, -30)
assert (1, 30) == count_zeros_in_turn(60, -130)
assert (2, 30) == count_zeros_in_turn(60, -230)
assert (0, 70) == count_zeros_in_turn(0, -30)
assert (1, 70) == count_zeros_in_turn(1, -31)
assert (1, 0) == count_zeros_in_turn(1, -1)
assert (3, 0) == count_zeros_in_turn(1, -201)
assert (3, 0) == count_zeros_in_turn(0, -300), count_zeros_in_turn(0, -300)
assert (0, 95) == count_zeros_in_turn(0, -5), count_zeros_in_turn(0, -5)
assert (1, 0) == count_zeros_in_turn(0, -100), count_zeros_in_turn(0, -100)
assert (1, 99) == count_zeros_in_turn(0, -101), count_zeros_in_turn(0, -101)
assert (3, 0) == count_zeros_in_turn(0, 300)

