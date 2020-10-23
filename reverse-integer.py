#Given an integer, return the integer with reversed digits.
#Note: the integer could be either postive or negative.

def solution(x):
    string = str(x)

    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])
print(solution(-231))
print(solution(345))