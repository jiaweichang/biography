def gcd(p, q):
    if p < q:
        tmp = p
        p = q
        q = tmp
    r = p % q
    if r == 0:
        return q
    else:
        return gcd(q, r)

print(gcd(8, 12))
