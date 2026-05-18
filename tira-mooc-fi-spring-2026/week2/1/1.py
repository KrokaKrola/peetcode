import time


def list_efficiency_1(n: int):
    test_list = []
    start = time.perf_counter()

    for i in range(n):
        test_list.append(i)

    elapsed = time.perf_counter() - start
    print(f"{elapsed:.6f} seconds")

    start = time.perf_counter()

    for i in range(n):
        test_list.pop()

    elapsed = time.perf_counter() - start
    print(f"{elapsed:.6f} seconds")


def list_efficiency_2(n: int):
    test_list = []
    start = time.perf_counter()

    for i in range(n):
        test_list.append(i)

    elapsed = time.perf_counter() - start
    print(f"{elapsed:.6f} seconds")

    start = time.perf_counter()

    for i in range(n):
        test_list.pop(0)

    elapsed = time.perf_counter() - start
    print(f"{elapsed:.6f} seconds")


list_efficiency_1(10**5)
print("----")
list_efficiency_2(10**5)
