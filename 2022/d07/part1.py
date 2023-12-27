data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def add2fs(fs, path, name, val):    
    d = fs
    for key in path:
        d = d.get(key)
    d[name] = val
    print(d)

def parse(lines):
    fs = {}
    cwd = []
    for line in lines:
        print(line)
        if line[0] == '$':
            cmd = line[2:]
            print(cmd)
            if cmd[:2] == 'cd':
                dir = cmd[3:]
                if dir == '/':
                    cwd = []
                elif dir == '..':
                    cwd.pop()
                else:
                    cwd.append(dir)
                print("cwd", cwd)
        else:
            if line[:3] == 'dir':
                dir = line[4:]
                print("add dir", dir)
                add2fs(fs, cwd, dir, {})
            else:
                size, name = line.split(' ')
                size = int(size)
                print("add file", name, "with size", size)
                add2fs(fs, cwd, name, size)
    return fs

def calcSize(fs, sizes):
    size = 0
    for key in fs:
        val = fs[key]
        if type(val) is dict:
            size += calcSize(val, sizes)
        else:
            size += val
    sizes.append(size)
    return size

data = open('data', 'r').read()
lines = data.split('\n')
fs = parse(lines)
print(fs)
sizes = []
calcSize(fs, sizes)
print(sizes)

sum = 0
for size in sizes:
    if size <= 100000:
        sum += size
print(sum)
