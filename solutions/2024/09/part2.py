from aoc import *
from dataclasses import dataclass
from tqdm import tqdm

inp = sys.stdin.read().rstrip()

sizes = list(map(int, inp[::2]))
free_space = list(map(int, inp[1::2])) + [0]

@dataclass
class File:
    file_id: int
    offset: int
    size: int

files = []
offset = 0
for file_id, (size, gap) in enumerate(zip(sizes, free_space)):
    files.append(File(file_id, offset, size))
    offset += size + gap

i = len(files) - 1
seen = set()
while i >= 0:
    file = files[i]
    if file.file_id in seen:
        i -= 1
        continue
    seen.add(file.file_id)
    for j in range(1, i + 1):
        a = files[j-1]
        b = files[j]
        gap = b.offset - (a.offset + a.size)
        if gap >= file.size:
            files.pop(i)
            files.insert(j, file)
            assert a.offset + a.size < file.offset
            file.offset = a.offset + a.size
            break
    else:
        i -= 1

ans = 0
for f in files:
    ans += np.sum(f.file_id*(f.offset + np.arange(f.size)))
print(ans)
