with open("day1.txt", "r") as file:
    lines = file.readlines()
LL = []
RR = []

for line in lines:
    L,R = line.split()
    L,R = int(L),int(R)
    LL.append(L)
    RR.append(R)

LL = sorted(LL)
RR = sorted(RR)

answer = 0
for l, r in zip(LL, RR):
    answer += abs(l-r)

print(answer)