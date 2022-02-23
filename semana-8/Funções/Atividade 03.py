def fibonacci(num):
    if num <= 1:
        return num
    
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

pos = int(input("Informe a Posição do Fibonacci: "))
resultado = fibonacci(pos)

print("O Fibonacci é %d" % (resultado))

# Fibonacci: 1 1 2 3 5 8 13