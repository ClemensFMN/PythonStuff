import redis
import time

h = redis.Redis()
h.set('mykey1', 1)
print(h.get('mykey1'))


h.set('mykey2', 2, ex=3)
print(h.get('mykey2'))
time.sleep(5)
print('continue')
print(h.get('mykey2'))

