def sample(s):
    res = ""
    for i in range(len(s)+1):
        res += s[:i:]
    return res

print(sample("abc"))