def read_file(file):
    with open(file, "r") as f:
        lines = f.readlines()
    return lines

lines = read_file(("day 6/input_map.txt"))
# lines = read_file(("day 6/sample.txt"))
height = len(lines)
width = len(lines[0])

def initial_caret():
    for y, line in enumerate(lines):
        for x, spot in enumerate(line):
            if spot == "^":
                return x, y

def bust(pos):
    x, y = pos
    if x == -1 or y == -1 or x == width or y == height:
        return True
    return False
    
def barrier(pos):
    x, y = pos
    if lines[y][x] == "#":
        return True
    return False

# 0-1 up, 10 right, 01 down, -10 left  
def rotate(x_dir, y_dir):
    if y_dir == -1:
        return 1, 0
    if x_dir == 1:
        return 0, 1
    if y_dir == 1:
        return  -1, 0
    if x_dir == -1:
        return 0, -1

def move(cur_pos, direction, new_barrier):
    x_dir, y_dir = direction    
    places_set = set()  # x, y, direction
    places_list = []

    while not bust(cur_pos):
        x, y = cur_pos
        next_pos = x+x_dir, y+y_dir
        if bust(next_pos): 
            return places_list
        while barrier(next_pos) or next_pos == new_barrier:
            x_dir, y_dir = rotate(x_dir, y_dir)
            next_pos = x+x_dir, y+y_dir
        cur_pos = next_pos
        if (cur_pos, (x_dir, y_dir)) in places_set:
            return {}  # Denotes loop
        places_list.append((cur_pos, (x_dir, y_dir)))
        places_set.add((cur_pos, (x_dir, y_dir)))
        # print(cur_pos, (x_dir, y_dir))

    return places_list

initial_x, initial_y = initial_caret()
default_places_list = move((initial_x, initial_y), (0,-1), None)

count = 0
attempted_barrs = set()
for i, (pos, dir) in enumerate(default_places_list):
    print(i)
    if i == 0: 
        print(pos,dir)
    barr = pos
    if barr in attempted_barrs or barr == initial_caret: 
        continue
    pos =  pos[0]-dir[0], pos[1]-dir[1]
    if barr == initial_caret():
        print("What")
    if pos == initial_caret():
        print("Hey")
    if not move(pos, dir, barr):
        count += 1
    attempted_barrs.add(barr)

print(count)