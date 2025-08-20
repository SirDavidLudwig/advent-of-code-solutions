from re import X
from aoc import *

inp = sys.stdin.read().rstrip()

def mix(secret, value):
    return secret ^ value

def prune(secret):
    return secret % 16777216

def next_secret(secret):
    secret = prune(mix(secret, secret*64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret*2048))
    return secret

ans = 0
from tqdm import tqdm
for secret in tqdm(map(int, inp.split('\n'))):
    for _ in range(2000):
        secret = next_secret(secret)
    ans += secret
# print(inp)

print(ans)
