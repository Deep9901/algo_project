from functools import lru_cache
import math

def held_karp(dist):
    n = len(dist)

    @lru_cache(None)
    def tsp(mask, last):
        if mask == (1 << n) - 1:
            return dist[last][0]  # return to start

        best = math.inf
        for nxt in range(n):
            if mask & (1 << nxt):
                continue
            new_cost = dist[last][nxt] + tsp(mask | (1 << nxt), nxt)
            best = min(best, new_cost)
        return best

    return tsp(1, 0)
