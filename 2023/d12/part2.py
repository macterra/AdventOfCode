# https://adventofcode.com/2023/day/12

data = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

def parse(data):
    rows = []
    for line in data.strip().split('\n'):
        springs, report = line.split(' ')
        springs = springs
        springs = springs + '?'
        springs = springs * 5
        springs = springs[:-1]
        report = [int(x) for x in report.split(',')]
        report = report * 5
        rows.append((springs, report))
    return rows

def matchn(pattern, n):
    l = len(pattern)

    if l < n:
        return False

    for i in range(n):
        if pattern[i] == '.':
            return False

    if l > n:
        return pattern[n] != '#'
    else:
        return True

Memo = {}

def count(springs, report):
    global Memo

    if not springs:
        if not report:
            return 1
        else:
            return 0

    if springs[0] == '.':
        return count(springs[1:], report)

    if springs[0] == '?':
        x = '#' + springs[1:]
        y = '.' + springs[1:]
        z = ",".join(map(str, report))

        if not x+z in Memo:
            a = count(x, report)
            Memo[x+z] = a
        else:
            a = Memo[x+z]

        if not y+z in Memo:
            b = count(y, report)
            Memo[y+z] = b
        else:
            b = Memo[y+z]

        return a + b

    if not report:
        return 0

    n = report[0]
    if matchn(springs[:n+1], n):
        return count(springs[n+1:], report[1:])
    else:
        return 0

data = open('data', 'r').read()

rows = parse(data)
total = 0
for row in rows:
    springs, report = row
    x = count(springs, report)
    print(row, x)
    total += x

print(total)
