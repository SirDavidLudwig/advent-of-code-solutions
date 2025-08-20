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

def find_file_ids(data):
    i = len(data) - 1
    j = len(data) - 1
    while i >= 0:
        while i >= 0 and data[i] == data[j]:
            i -= 1
        if data[i+1] != -1:
            yield (data[i+1], i+1, j-i)
        j = i

def find_block(size, max_index):
    i = 0
    j = 0
    while i < max_index:
        while data[i] != -1:
            i += 1
        j = i+1
        while j-i < size and data[j] == -1:
            j += 1
        if j-i >= size:
            return i
        i = j
    return None

from tqdm import tqdm
for (file_id, start, size) in tqdm(list(find_file_ids(data))):
    dest_i = find_block(size, start)
    if dest_i is None:
        continue
    data[dest_i:dest_i+size] = file_id
    data[start:start+size] = -1

ans = 0
for i, x in enumerate(data):
    if x == -1:
        continue
    ans += i*int(x)
print(ans)


# print(data)

#           9758677756397
# too high: 6336067657790
# incorrect: 6335973512055
# incorrect: 6335973512055

# print(ans)
