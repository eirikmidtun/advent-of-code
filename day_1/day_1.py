sum_task_1 = 0
sum_task_2 = 0
left = []
right = []
occurrence_map = {}

with open('day_1.txt', 'r') as file:
    for line in file:
        split = line.split()

        left.append(int(split[0]))
        right.append(int(split[1]))

left = sorted(left)
right = sorted(right)

sum_task_1 = sum(abs(l-r) for l,r in zip(left, right))

for num in left:
    occurrence_map[num] = 0

for num in right:
    if num in occurrence_map:
        occurrence_map[num] +=1

sum_task_2 = sum(num*occurrence_map[num] for num in left)

print(f"Day one task 1: {sum_task_1}")
print(f"Day one task 2: {sum_task_2}")