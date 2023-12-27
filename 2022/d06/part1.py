data1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
data2 = "nppdvjthqldpwncqszvftbrmjlhg"
data3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
data4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def findMarker(buffer):
    print(buffer)
    for i in range(4, len(buffer)):
        packet = buffer[i-4:i]
        #print(i, packet, set(packet), len(set(packet)))
        if len(set(packet)) == 4:
            return i

print(findMarker(data1))
print(findMarker(data2))
print(findMarker(data3))
print(findMarker(data4))

data = open('data', 'r').read()
print(findMarker(data))
