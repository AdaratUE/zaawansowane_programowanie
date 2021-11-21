def numbers(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


czy = numbers(8)

if not czy:
    print("Liczba nie jest parzysta")
else:
    print("Liczba jest parzysta")
