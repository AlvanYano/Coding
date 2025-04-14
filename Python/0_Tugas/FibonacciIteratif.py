def fibonacci_iterative(n):
    """Menghitung bilangan Fibonacci menggunakan metode iteratif."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Contoh penggunaan
n = 10
print("Fibonacci Series:", end=" ")
fibonacci_iterative(n)
