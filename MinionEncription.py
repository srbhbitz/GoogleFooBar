def solution(x):
    i = 0
    ans = []
    a = 'abcdefghijklmnopqrstuvwxyz'
    while i < len(x):
        if x[i] in a:
            ans.append(a[25-a.index(x[i])])
        else:
            ans.append(x[i])
        i = i + 1
    return "".join(ans)
