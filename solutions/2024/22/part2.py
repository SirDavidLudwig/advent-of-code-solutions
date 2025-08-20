from aoc import *

inp = sys.stdin.read().rstrip()

print("Input", inp)

def mix(secret, value):
    return secret ^ value

def prune(secret):
    return secret % 16777216

def next_secret(secret):
    secret = prune(mix(secret, secret*64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret*2048))
    return secret

sequence_counters = []

ans = 0
from tqdm import tqdm
for secret in tqdm(map(int, inp.split('\n'))):
    data = [secret]
    for _ in range(2000):
        secret = next_secret(secret)
        data.append(secret)
    diff = tuple(np.diff(np.array(data) % 10))
    counter = Counter()
    for i in range(0, len(diff) - 4):
        sequence = tuple(diff[i:i+4])
        if sequence in counter:
            continue
        counter[sequence] += data[i+4]%10
    sequence_counters.append(counter)

counter = Counter()
for c in sequence_counters:
    counter.update(c)

print(max(counter.items(), key=lambda x: x[1])[1])

print(ans)
