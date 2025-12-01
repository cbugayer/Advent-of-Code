def read_file(file):
    with open(file, "r") as f:
        lines = f.readlines()
    return lines

lines = read_file(("day 6/input_map.txt"))
# lines = read_file(("day 6/sample.txt"))
height = len(lines)
width = len(lines[0])
covered_spots = set()

def initial_caret():
    for y, line in enumerate(lines):
        for x, spot in enumerate(line):
            if spot == "^":
                return x, y

    
def barrier_or_bust(x,y):
    if x == -1 or y == -1 or x == width or y == height:
        return "bust"
    if lines[y][x] == "#":
        return "barrier"
    return ""

def rotate(x_dir, y_dir):
    if y_dir == -1:
        return 1, 0
    if x_dir == 1:
        return 0, 1
    if y_dir == 1:
        return  -1, 0
    if x_dir == -1:
        return 0, -1

# 0-1 up, 10 right, 01 down, -10 left  
def move(startx, starty, direction):
    while barrier_or_bust(startx, starty) != "bust":
        # print(startx, starty)
        x_dir, y_dir = direction
        while not barrier_or_bust(startx, starty):
            covered_spots.add((startx, starty))
            # print("hi", startx, starty)
            startx += x_dir
            starty += y_dir
            # print("bye", startx, starty)
        if barrier_or_bust(startx, starty) == "barrier":
            # print("barrier at: ", startx, " ", starty)
            # print(x_dir, y_dir)
            startx -= x_dir
            starty -= y_dir
            direction = rotate(x_dir, y_dir)

def get_set_length():
    initial_x, initial_y = initial_caret()
    move(initial_x, initial_y, (0,-1))
    return len(covered_spots)

# print(get_set_length())