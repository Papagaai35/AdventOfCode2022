import numpy as np

content = """30373
25512
65332
33549
35390"""


demo_on = input("Do you want the demo? [y/N] ").lower()
if "y" not in demo_on:
    with open("inputs/input_d08.txt","r") as fh:
        content = fh.read()

forest = np.array(list(map(list,content.split("\n")))).astype(int)
visable = np.zeros(forest.shape).astype(int)

for r in range(forest.shape[0]):
    lv, lvp = -1, -1
    rv, rvp = -1, forest.shape[1]
    for c,t in enumerate(forest[r,:]):
        if t > lv:
            visable[r,c] = 1
            lv = t
            lvp = c
    for C,t in enumerate(forest[r,::-1]):
        c = forest.shape[1] - C - 1
        if t > rv:
            visable[r,c] = 1
            rv = t
            rvp = c
for c in range(forest.shape[1]):
    uv, uvp = -1, -1
    dv, dvp = -1, forest.shape[0]
    for r,t in enumerate(forest[:,c]):
        if t > uv:
            visable[r,c] = 1
            uv = t
            uvp = c
    for R,t in enumerate(forest[::-1,c]):
        r = forest.shape[0] - R - 1
        if t > dv:
            visable[r,c] = 1
            dv = t
            dvp = c
print("Part 1", visable.sum())

los = np.zeros(forest.shape).astype(int)
for y in range(forest.shape[0]):
    for x in range(forest.shape[1]):
        val = forest[y,x]
        left,right = forest[y,:x][::-1],forest[y,(x+1):]
        up,down = forest[:y,x][::-1],forest[(y+1):,x]
        if (left>=val).any():
            left = left[:(np.argmax(left>=val)+1)]
        if (right>=val).any():
            right = right[:(np.argmax(right>=val)+1)]
        if (up>=val).any():
            up = up[:(np.argmax(up>=val)+1)]
        if (down>=val).any():
            down = down[:(np.argmax(down>=val)+1)]
        los[y,x] = len(left)*len(right)*len(up)*len(down)
print("Part 2", np.amax(los))