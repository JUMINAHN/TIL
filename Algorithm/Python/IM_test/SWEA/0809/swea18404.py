data = list(map(int, input().split()))
bit = [0] * len(data) #bit 0개 개수만큼 일단 만들어
result = []
for a in data:
    bit[0] = a
    for b in data:
        bit[1] = b
        for c in data:
            bit[2] = c
            for d in data:
                bit[3] = d
                for e in data:
                    bit[4] = e
                    for f in data:
                        bit[5] = f
                        for g in data:
                            bit[6] = g
                            for h in data:
                                bit[7] = h
                                for i in data:
                                    bit[8] = i
                                    for j in data:
                                        bit[9] = j
                                        result.append(bit.copy())
print(result)
