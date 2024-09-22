from sympy.ntheory import sqrt_mod, prime
from numpy.random import randint

max = 1000000
RUNS = 1000

# count the fraction of modular sqrts for a given prime
def cnt_sqrt_mod(p, RUNS):
    cnt = 0
    for i in range(RUNS):

        a = randint(max)
        #print(a)
        #print(sqrt_mod(a, p))
        if(sqrt_mod(a, p) == None):
            cnt += 1
    return(cnt)


def seq_sqrt_mod(p, N):
    a = randint(max)
    for i in range(a, a+N):
        print(i, " -> ", sqrt_mod(i, p))


# generate the n-th prime
n = randint(max)
p = prime(n)
print("Prime: ", p)

#cnt = cnt_sqrt_mod(p, RUNS)
#print(cnt / RUNS)

seq_sqrt_mod(p, 20)
