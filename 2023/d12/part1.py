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
        report = [int(x) for x in report.split(',')]
        unknowns = [i for i in range(len(springs)) if springs[i] == '?']
        rows.append((springs, report, unknowns))
    return rows

def generateOptions(N, options=""):
    if N == 0:
        return [options]
    else:
        return generateOptions(N-1, options + ".") + generateOptions(N-1, options + "#")

def generateReport(arrangement):
    report = []
    n = len(arrangement)
    i = 0
    c = 0
    while i < n:
        if arrangement[i] == '.':
            if c > 0:
                report.append(c)
                c = 0
        else:
            c += 1
        i += 1
    if c > 0:
        report.append(c)
    return report

def test(row):
    springs, report, unknowns = row
    options = generateOptions(len(unknowns))
    #print(row, len(unknowns))
    #print(options)
    n = 0
    for option in options:
        arrangement = [x for x in springs]
        for i in range(len(unknowns)):
            arrangement[unknowns[i]] = option[i]
        #print(option, arrangement)
        if generateReport(arrangement) == report:
            n += 1
    return n

data = open('data', 'r').read()
rows = parse(data)
print(sum([test(row) for row in rows]))
