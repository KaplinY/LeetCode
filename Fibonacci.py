import time

def cache(func):
    cache = {}
    def wrapper(*args):
        key = (*args,)
        if key in cache:
            return cache[key]
        result = func(*args)
        cache[key]=result

        return result
    return wrapper

@cache
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    start = time.monotonic()
    num = fib(40)
    print(f"Fib number: {num}")
    print(time.monotonic() - start)