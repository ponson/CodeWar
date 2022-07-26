N = 100
cnt = 0

for l in range(N+1):
    for r in range(l, N+1):
        if l > r - l:
            if l != N - r:
                cnt+=1
        elif l < r - l:
            if r - l != N - r:
                cnt+=1
        else:
            if (l < N - r):
                cnt += 1

print(f"cnt={cnt}")