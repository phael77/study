from functools import lru_cache

@lru_cache(maxsize=3)
def compute(x):
    print(f"Computing {x}")
    return x * x


print(compute(2))
print(compute(3))
print(compute(2))
print(compute(4))
print(compute(5))

print(compute.cache_info())