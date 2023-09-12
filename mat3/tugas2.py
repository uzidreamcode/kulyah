def hammingDistance(x,y):

    ans = 0
    m = max(x,y)
    while (m):
        c1 = x & 1
        c2 = y & 1
        if (c1 != c2):
            ans += 1
        m = m >> 1
        x = x >> 1
        y = y >> 1
    return ans


n1 = 4 
n2 = 8 
hdsit = hammingDistance(n1, n2)
print(hdsit)