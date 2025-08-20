from aoc import *

inp = sys.stdin.read().rstrip()
# print(inp)

files = list(map(int, inp[::2]))
free = list(map(int, inp[1::2]))

n = np.sum(files) + np.sum(free)
data = np.full(n, -1)


i = 0
file_id =0
for k, l in enumerate(inp):
    l = int(l)
    if k % 2 == 0:
        data[i:i+l] = file_id
        file_id += 1
    i += l

n = np.sum(data != -1)

i = 0
j = len(data) - 1

while i < j:
    while data[i] != -1:
        i += 1
    while data[j] == -1:
        j -= 1
    if i >= j:
        break
    data[i], data[j] = data[j], data[i]

# print(data)
ans = np.sum(data[:n]*np.arange(n))


print(ans)
