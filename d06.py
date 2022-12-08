with open("inputs/input_d06.txt","r") as fh:
    content = fh.read().strip()
    
tests = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',
    content
]

def get_marker_pos(message,marker_len):
    for i in range(marker_len-1,len(message)):
        substr = message[i-marker_len:i]
        if len(set(substr)) == marker_len:
            return i

print("Marker Length = 4")
for ti, test in enumerate(tests):
    print(f"Demo {ti:d}:" if ti <= 4 else "Part 1:",get_marker_pos(test,4))
    
print("\nMarker Length = 14")
for ti, test in enumerate(tests):
    print(f"Demo {ti:d}:" if ti <= 4 else "Part 2:",get_marker_pos(test,14))
