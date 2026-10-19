arr = [10,10,20,30,20,40,50]
pairs = 0
counts = {}
for sock in arr:
    counts[sock] = counts.get(sock,0)+1
    if counts[sock] % 2 == 0:
        pairs += 1
print(pairs)