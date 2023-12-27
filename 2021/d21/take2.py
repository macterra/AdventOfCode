

def diracDice(n, p1, s1, p2, s2, d):
    print(n, p1, s1, p2, s2)

    d = (d+1)%100
    r = d
    d = (d+1)%100
    r += d
    d = (d+1)%100
    r += d

    p1 = 1 + (p1-1 + r)%10
    s1 += p1

    print("  ", r, p1, s1)

    if s1 >= 1000:
        print(f"p1 wins with {s1} vs {s2} and {n*6+3} rolls")
        return 1
        
    d = (d+1)%100
    r = d
    d = (d+1)%100
    r += d
    d = (d+1)%100
    r += d

    p2 = 1 + (p2-1 + r)%10
    s2 += p2

    print("  ", r, p2, s2)

    if s2 >= 1000:
        print(f"p2 wins with {s1} vs {s2} and {n*7} rolls")
        return 2

    return diracDice(n+1, p1, s1, p2, s2, d)    

winner = diracDice(0, 4, 0, 8, 0, 0)
print(f"winner {winner}")
