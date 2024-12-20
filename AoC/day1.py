
with open("day1.txt", "r") as file:
    lines = file.readlines()
left_list = []
right_list = []

for line in lines:
    left,right = line.split()
    left,right = int(left),int(right)
    left_list.append(left)
    right_list.append(right)

left = sorted(left_list)
right = sorted(right_list)

answer = 0
for l, r in zip(left_list, right_list):
    answer += abs(l-r)

print(answer)