
with open("day2.txt", "r") as file:
    lines = file.readlines()

levels = []
safe = 0

for line in lines:
    numbers = list(map(int, line.strip().split()))
    yes = (numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True))
    ok  = True
    for i in range(0, len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if not 1 <= diff <= 3:
            ok = False
    if yes and ok:
        safe = safe+1
print(safe)
