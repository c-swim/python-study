#제너레이터와 yield
def genFunc():
    yield 1
    yield 2
    yield 3
    
print(list(genFunc()))