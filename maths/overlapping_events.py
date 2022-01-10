import numpy.random as rnd

wA = 0.3
wB = 0.3

RUNS = 10000
cnt = 0

for i in range(RUNS):
    tA1 = rnd.uniform(0.0,1.0)
    tA2 = tA1 + wA

    tB1 = rnd.uniform(0.0,1.0)
    tB2 = tB1 + wB

    #print(tA1, tA2)
    #print(tB1, tB2)

    # overlap = (tB1 < tA1 < tB2) or (tB1 < tA2 < tB2) or (tA1 < tB1 < tA2) or (tA1 < tB2 < tA2)
    overlap = (tB1 < tA1 < tB2) or (tA1 < tB1 < tA2)
    # print(overlap)
    if overlap:
        cnt += 1


analytical = wA + wB - 0.5*wA**2 - 0.5*wB**2
print(cnt/RUNS, analytical)
