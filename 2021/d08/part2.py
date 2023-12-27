input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

#input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
input = open('data', 'r').read()
lines = input.split('\n')

def normalize(symbols):
    return ["".join(sorted(s)) for s in symbols]

def combine(s1, s2):
    combo = set(s1).union(s2)
    combo = sorted(combo)
    combo = "".join(combo)
    return combo

def common(s1, s2):
    return len(set(s1).intersection(s2))

def parse(line):
    print(line)
    signals, output = line.split(" | ")
    signals = normalize(signals.split(' '))
    output = normalize(output.split(' '))
    print(signals, output)

    code = {}
    fives = []
    sixes = []

    for s in signals:
        l = len(s)
        if l == 2:
            code[1] = s
        elif l == 3:
            code[7] = s
        elif l == 4:
            code[4] = s
        elif l == 7:
            code[8] = s
        elif l == 5:
            fives.append(s)
        elif l == 6:
            sixes.append(s)

    print('code', code)
    print('fives', fives)
    for f in fives:
        if common(f, code[1]) == 2:
            code[3] = f
            break

    print('sixes', sixes)
    for s in sixes:
        if common(s, code[1]) < 2:
            code[6] = s
            break

    code[9] = combine(code[3], code[4])
    sixes.remove(code[6])
    sixes.remove(code[9])
    code[0] = sixes[0]

    fives.remove(code[3])
    if common(code[6], fives[0]) == 5:
        code[5] = fives[0]
        code[2] = fives[1]
    else:
        code[5] = fives[1]
        code[2] = fives[0]

    digits = [len(x) for x in signals]
    print(signals, output, digits)
    print(code)
    print(fives, sixes)
    inv = {v: k for k, v in code.items()}
    print(inv)
    x = [str(inv[o]) for o in output]
    print(x)
    y = int("".join(x))
    return y

sum = 0
for line in lines:
    sum += parse(line)
print(sum)    
