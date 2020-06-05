def np(n):
    c = 0
    while n > 1:
        if n%2 == 0:
            n = n/2
            c += 1
        else:
            n += 1
            c += 1
    return c

def nn(n):
    c = 0
    while n > 1:
        if n%2 == 0:
            n = n/2
            c += 1
        else:
            n -= 1
            c += 1
    return c
def solution(n):
    if np(n) > nn(n):
        return nn(n)
    else:
        return np(n)
