def fibonacci_recursive(n):
    """Menghitung bilangan Fibonacci menggunakan metode rekursif."""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = 10
print("Fibonacci Series:", end=" ")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
