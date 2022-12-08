content_demo = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

with open("input_d04.txt","r") as fh:
    content = fh.read()

# Converts to list of tuples<4 x int>
def pairstr_to_list(content):
    return list(map(
        lambda pair: tuple(map(int,
                           pair.replace('-',',').split(','))),
        content.split("\n")))
pairs_demo = pairstr_to_list(content_demo)
pairs = pairstr_to_list(content)

fully_contain = (lambda p: 
                 (p[0]<=p[2] and p[1]>=p[3]) or
                 (p[2]<=p[0] and p[3]>=p[1]))
print("Demo 1:",len(list(filter(fully_contain,pairs_demo))))
print("Part 1:",len(list(filter(fully_contain,pairs))))

range_overlap = lambda p: max(p[0],p[2])<=min(p[1],p[3])
print("Demo 2:",len(list(filter(range_overlap,pairs_demo))))
print("Part 2:",len(list(filter(range_overlap,pairs))))
