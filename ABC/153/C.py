n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

print(sum(h[:n-k]) if k < n else 0)
