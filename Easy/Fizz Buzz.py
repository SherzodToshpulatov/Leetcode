# https://leetcode.com/problems/fizz-buzz/
def fizzbuzz(n):
    strlist = []
    for i in range(n):
        if (i+1) % 15 == 0:
            strlist.append("FizzBuzz")
        elif (i+1) % 5 == 0:
            strlist.append("Buzz")
        elif (i+1) % 3 == 0:
            strlist.append("Fizz")
        else:
            strlist.append(str(i+1))
    return strlist


print(fizzbuzz(15))
