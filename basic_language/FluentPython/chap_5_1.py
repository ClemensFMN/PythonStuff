from inspect import signature


def f1(x):
    "Some dummy test function"
    return x+1

def f2(x,y=10):
    return x+y

def f3(x:int, y:str) -> int:
    return x+1


print(f1(3))

# what else does the function provide?
print(dir(f1))

# doc string
print(f1.__doc__)

# print signature
print(signature(f1))

sig = signature(f2)
# iterate over signature data
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)


sig = signature(f3)
# if the function contains type hints, we get more info out of the signature object
for name, param in sig.parameters.items():
    print(param.annotation, ':', name, '=', param.default)
