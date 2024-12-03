from collections import defaultdict, Counter

with open("day1.txt", "r") as file:
    lines = file.readlines()
left_list = []
right_list = Counter()

for line in lines:
    left,right = line.split()
    left,right = int(left),int(right)
    left_list.append(left)
    right_list[right] += 1

left_list = sorted(left_list)

answer = 0
for l in left_list:
    answer += l * right_list.get(l, 0)
print(answer)