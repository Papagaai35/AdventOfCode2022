content = """A Y
B X
C Z"""

with open("inputs/input_d02.txt","r") as fh:
    content = fh.read()
    
games = content.strip().split("\n")

gametable_1 = {
    'A X': 3+1,
    'B X': 0+1,
    'C X': 6+1,
    'A Y': 6+2,
    'B Y': 3+2,
    'C Y': 0+2,
    'A Z': 0+3,
    'B Z': 6+3,
    'C Z': 3+3,
    '': 0
}

score = 0
for game in games:
    score += gametable_1[game.strip()]
print("Score (Part 1):", score)

gametable_2 = {
    'A X': 0+3,
    'B X': 0+1,
    'C X': 0+2,
    'A Y': 3+1,
    'B Y': 3+2,
    'C Y': 3+3,
    'A Z': 6+2,
    'B Z': 6+3,
    'C Z': 6+1,
    '': 0
}

score = 0
for game in games:
    score += gametable_2[game.strip()]
print("Score (Part 2):", score)
