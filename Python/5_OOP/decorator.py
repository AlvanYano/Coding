def only_positive(func):
    def wrapper(n):
        if n < 0:
            return "Angka harus positif"
        return func(n)
    return wrapper

@only_positive
def akar(n):
    return n ** 0.5

print(akar(9))     # 3.0
print(akar(-4))    # Angka harus positif