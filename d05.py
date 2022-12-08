content_demo = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".strip("\n")

with open("inputs/input_d05.txt","r") as fh:
    content = fh.read()
    
### PART 1
def part_1(content):
    stackstr, instructions = content.split("\n\n")
    stacks = {}
    
    #Check on the bottom row where the stacks are defined, then extract them
    for pos,stack_id in enumerate(stackstr.split("\n")[-1]):
        if stack_id==" ":
            continue
        stacks[int(stack_id)] = []
        for level in stackstr.split("\n")[:-1]:
            if level[pos]==" ":
                continue
            stacks[int(stack_id)].append(level[pos])
    stacks = {k:list(reversed(list(v))) for k,v in stacks.items()}
    
    #Loop over the instructions
    for instruct in instructions.split("\n"):
        movestr, number, fromstr, frompos, tostr, topos = instruct.split()
        number, frompos, topos = int(number), int(frompos), int(topos)
        for i in range(number):
            container = stacks[frompos].pop()
            stacks[topos].append(container)
    top_of_stacks = "".join([v[-1] for k,v in stacks.items()])
    return top_of_stacks

print("Demo 1:",part_1(content_demo))
print("Part 1:",part_1(content))

### PART 2
def part_2(content):
    stackstr, instructions = content.split("\n\n")
    stacks = {}
    
    #Check on the bottom row where the stacks are defined, then extract them
    for pos,stack_id in enumerate(stackstr.split("\n")[-1]):
        if stack_id==" ":
            continue
        stacks[int(stack_id)] = []
        for level in stackstr.split("\n")[:-1]:
            if level[pos]==" ":
                continue
            stacks[int(stack_id)].append(level[pos])
    stacks = {k:list(reversed(list(v))) for k,v in stacks.items()}
    
    #Loop over the instructions
    for instruct in instructions.split("\n"):
        movestr, number, fromstr, frompos, tostr, topos = instruct.split()
        number, frompos, topos = int(number), int(frompos), int(topos)

        stacks[frompos], containers = stacks[frompos][:-number], stacks[frompos][-number:]
        stacks[topos] = stacks[topos] + containers
    top_of_stacks = "".join([v[-1] for k,v in stacks.items()])
    return top_of_stacks

print("Demo 2:",part_2(content_demo))
print("Part 2:",part_2(content))
