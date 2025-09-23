from collections import defaultdict
# Take two lists as separate inputs, sort them in ASCENDING order and pair those numbers with the corresponding number from the other list. Find the difference of each pair for every entry in the list and total that up. 

# Get the puzzle input from input.txt and assign it to raw_data.
with open("input.txt") as puzzleinput:
    raw_data = puzzleinput.read()

rows = [row.split() for row in raw_data.split('\n') if row]
rows = [(int(l), int(r)) for l, r in rows]

# Part 1;

left, right = zip(*rows)
left, right = sorted(left), sorted(right)

total = 0
for i in range(len(rows)):
    total += abs(left[i] - right[i])

print(total) 

# Part 2 - find how many times numbers from the left list repeat in the right list and multiply that number by the amount of times it repeats. Then find the sum of those numbers added together.

r_counts = defaultdict(int)

for l, r in rows:
    r_counts[r] += 1

total = 0
for l, _ in rows:
    if l in r_counts:
        total += (l * r_counts[l])

print(total)
