data1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
data2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
data3 = "nppdvjthqldpwncqszvftbrmjlhg"
data4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
data5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def findMarker(buffer):
    print(buffer)
    X= 14
    for i in range(X, len(buffer)):
        packet = buffer[i-X:i]
        #print(i, packet, set(packet), len(set(packet)))
        if len(set(packet)) == X:
            return i

print(findMarker(data1))
print(findMarker(data2))
print(findMarker(data3))
print(findMarker(data4))
print(findMarker(data5))

data = open('data', 'r').read()
print(findMarker(data))
