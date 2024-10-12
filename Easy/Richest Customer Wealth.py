
def maximumWealth(accounts):
    max = 0
    for account in accounts:
        if sum(account) > max:
            max = sum(account)

    return max

a = [[1,5],[7,3],[3,5]]
print(maximumWealth(a))
