# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:06:37 2023

@author: 700001473
"""

def prime_sieve(max_n):
    sieve = [True] * max_n
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True

    for i in range(2, max_n):
        #print("i = ", i)
        if sieve[i] == True:
            factor = 2
            while(True):
                number = factor * i
                #print("    number: ", number)
                if(number >= max_n):
                    break
                sieve[number] = False
                factor += 1
    # print(sieve)
    primes = [number for number, state in enumerate(sieve) if state]
    return primes


# try out how large max_n has to be
ps = prime_sieve(200000)

sol = ps[10000]                     
