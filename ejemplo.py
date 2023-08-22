
def suma(numbers):
    total = 0
    for x in numbers:
        if isinstance(x, int):
            total += x
    return total


numeros = [1,2,3,4,5,6, 'a']

print(suma(numeros))

