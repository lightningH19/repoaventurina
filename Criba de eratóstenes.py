import time as w

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False

    return [x for x in range(n + 1) if primes[x]]

def save_to_file(primes, filename):
    with open(filename, 'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')

# Obtener el número del usuario
user_input = int(input("Introduce un número para generar la criba de Eratóstenes: "))

# Generar la criba
result = sieve_of_eratosthenes(user_input)

# Imprimir la criba
print(f"Criba de Eratóstenes hasta {user_input}:", result)

print("¿Quieres guardar la criba, SI o NO?")
voluntad = input()

if voluntad == "SI":

    filename = 'criba_eratostenes.txt'
    save_to_file(result, filename)
    print(f"Criba guardada en el archivo {filename}.")
