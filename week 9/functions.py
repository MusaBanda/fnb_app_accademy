def greet(name):
    print(f"hello, {name}")

greet("musa")

def add(a, b):
    return a + b

result = add(2, 5)
print(result)

def f(n):
    if n == 0:
        return 1
    else:
        return n + f(n-1)

def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")

greet("bob")

