# The Fibonacci Sequence
from functools import lru_cache


@lru_cache(maxsize=3)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    for i in range(500):
        print(i, fib(i))
    print("Done")


if __name__ == "__main__":
    main()

# END
