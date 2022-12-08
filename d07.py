import os

commands = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

demo_on = input("Do you want the demo? [y/N] ").lower()
if "y" not in demo_on:
    with open("input_d07.txt","r") as fh:
        commands = fh.read()
    
commandlist = commands.strip().split("\n")
current_path = ""
directories = {}
files = {}

def join_paths(*args):
    join_path_relative = os.path.join(*args).strip()
    return os.path.abspath(join_path_relative)

for l in commandlist:
    l = l.strip()
    if l.startswith("$ ls"):
        continue
    elif l.startswith("$ cd"):
        dirname = l[5:]
        current_path = join_paths(current_path,dirname)
        if current_path not in directories:
            directories[current_path] = None
    elif l.startswith("dir "):
        dirname = l[5:]
        dirpath = join_paths(current_path,dirname)
        directories[dirpath] = None
    else:
        # File entry from a ls command
        size, file = l.split()
        filepath = join_paths(current_path,file)
        files[filepath] = int(size)

result = []
dirs = list(directories.keys())
for d in dirs:
    dirsize = sum([v for k,v in files.items() if k.startswith(d)])
    directories[d] = dirsize
    if dirsize <= 100000:
        result.append(dirsize)
print("Part 1:",sum(result))

free_bytes = 70000000 - directories['/']
needed = 30000000 - free_bytes

dcanidates = {}
for d,s in directories.items():
    if s-needed > 0:
        dcanidates[d] = s
delete_dir = min(dcanidates, key=dcanidates.get)
print("Part 2:", delete_dir, dcanidates[delete_dir])