import os
import sys
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
def part_2(data):
    dirs = [[0,1],[1,0],[-1,0],[0,-1]]

    def dfs(times):
        l = data
        R = len(l)
        C = len(l[0])

        RR = times * R
        CC = times * C
        D = [[None for _ in range(CC)] for _ in range(RR)]
        Q = [(0, 0, 0)]
        while Q:
            (d, r, c) = heappop(Q)
            if r < 0 or r >= RR or c < 0 or c >= CC:
                continue

            val = l[r % R][c % C] + (r // R) + (c // C)
            while val > 9:
                val -= 9

            cost = d + val

            if D[r][c] is None or cost < D[r][c]:
                D[r][c] = cost
            else:
                continue
            if r == RR - 1 and c == CC - 1:
                break

            for d in dirs:
                rr = r + d[0]
                cc = c + d[1]
                heappush(Q, (D[r][c], rr, cc))
        return D[RR - 1][CC - 1] - l[0][0]

    print(dfs(5))


def part_1(data):
    l = data
    R = len(l)
    C = len(l[0])

    seen = {}
    ans = 0

    def dfs(i, j):
        if (i,j) in seen:
            return seen[(i,j)]

        if i < 0 or i >= R or j < 0 or j >= C:
            return sys.maxsize
        if i == R - 1 and j == C - 1:
            return l[i][j]

        ans = l[i][j] + min(dfs(i+1, j), dfs(i, j+1))
        seen[(i, j)] = ans
        return ans

    print(dfs(0,0) - l[0][0])

def parse(data):
    l = []
    for i in data:
        t = []
        for j in i:
            t.append(int(j))
        l.append(t)
    return l


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)

    part_1(data)
    part_2(data)