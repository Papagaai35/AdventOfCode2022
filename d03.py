rugsacks_demo = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip().split("\n")

with open("inputs/input_d03.txt","r") as fh:
    rugsacks = fh.readlines()

def calc_prio_sum(rugsacks):
    score = 0
    for rugsack in rugsacks:
        rugsack = rugsack.strip()
        if rugsack=="":
            continue
        compartment1 = rugsack[:(len(rugsack)//2)]
        compartment2 = rugsack[(len(rugsack)//2):]
        for lower_nr in range(26):
            lower_char = chr(lower_nr+97)
            if lower_char in compartment1 and lower_char in compartment2:
                score += lower_nr + 1
                break
        else:
            for upper_nr in range(26):
                upper_char = chr(upper_nr+65)
                if upper_char in compartment1 and upper_char in compartment2:
                    score += upper_nr + 27
                    break
            else:
                raise ValueError(rugsack)
    return score

print("Demo 1",calc_prio_sum(rugsacks_demo))
print("Part 1",calc_prio_sum(rugsacks))

def calc_group_prio_sum(rugsacks):
    score = 0
    for group in range(len(rugsacks)//3):
        rugsack1, rugsack2, rugsack3 = rugsacks[group*3:group*3+3]
        for lower_nr in range(26):
            lower_char = chr(lower_nr+97)
            if (    lower_char in rugsack1 and
                    lower_char in rugsack2 and
                    lower_char in rugsack3):
                score += lower_nr + 1
                break
        else:
            for upper_nr in range(26):
                upper_char = chr(upper_nr+65)
                if (    upper_char in rugsack1 and
                        upper_char in rugsack2 and
                        upper_char in rugsack3):
                    score += upper_nr + 27
                    break
            else:
                raise ValueError(rugsack1, rugsack2, rugsack3)
    return score

print("Demo 2",calc_group_prio_sum(rugsacks_demo))
print("Part 2",calc_group_prio_sum(rugsacks))
