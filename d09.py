content = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

demo_on = input("Do you want the demo? [y/N] ").lower()
if "y" not in demo_on:
    with open("inputs/input_d09.txt","r") as fh:
        content = fh.read()
else:
    demo_1 = input("Part 1 demo or part 2? [1] ").lower()
    if "2" in demo_1:
        content = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
        


def follow_pos(own_pos,follow_pos):
    out_pos = own_pos[:]
    rel_pos = follow_pos[0]-out_pos[0],follow_pos[1]-out_pos[1]
    rel_max = max(abs(rel_pos[0]),abs(rel_pos[1]))
    if rel_max >= 2:
        if rel_pos[0] >= 1:
            out_pos[0] += 1
        if rel_pos[1] >= 1:
            out_pos[1] += 1
        if rel_pos[0] <= -1:
            out_pos[0] -= 1
        if rel_pos[1] <= -1:
            out_pos[1] -= 1
    return out_pos

pos0 = [0,0]
pos1 = [0,0]
pos2 = [0,0]
pos3 = [0,0]
pos4 = [0,0]
pos5 = [0,0]
pos6 = [0,0]
pos7 = [0,0]
pos8 = [0,0]
pos9 = [0,0]
pos0_list = [pos0[:]]
pos1_list = [pos1[:]]
pos9_list = [pos9[:]]

for i,instruction in enumerate(content.split("\n")):
    direction, number = instruction.split()
    number = int(number)
    for n in range(number):
        if direction == 'R':
            pos0[0] += 1
        elif direction == 'U':
            pos0[1] += 1
        elif direction == 'L':
            pos0[0] -= 1
        elif direction == 'D':
            pos0[1] -= 1
        pos0_list.append(pos0[:])
        
        pos1 = follow_pos(pos1,pos0)
        pos2 = follow_pos(pos2,pos1)
        pos3 = follow_pos(pos3,pos2)
        pos4 = follow_pos(pos4,pos3)
        pos5 = follow_pos(pos5,pos4)
        pos6 = follow_pos(pos6,pos5)
        pos7 = follow_pos(pos7,pos6)
        pos8 = follow_pos(pos8,pos7)
        pos9 = follow_pos(pos9,pos8)
        pos1_list.append(pos1[:])
        pos9_list.append(pos9[:])
pos1_set = set(map(lambda pos: "x".join(map(str,pos)),pos1_list))
pos9_set = set(map(lambda pos: "x".join(map(str,pos)),pos9_list))
print("Part 1",len(pos1_set))
print("Part 2",len(pos9_set))