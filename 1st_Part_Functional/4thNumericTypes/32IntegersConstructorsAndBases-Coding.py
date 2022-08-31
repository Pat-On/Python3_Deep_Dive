import fractions

a = fractions.Fraction(22, 7)

print(a)
print(float(a))
print(int(a))

# print(int("B", base=10))  # <---ValueError: invalid literal for int() with base 10: 'B'


print(bin(10))


def from_base10(n, b):
    if b < 2:
        raise ValueError("Base b must be >= 2")
    if n < 0:
        raise ValueError("Number must be >= 0")
    if n == 0:
        return [0]

    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        n, m = divmod(n, b)
        # m, n = n % b, n//b   # <- tuple notation
        digits.insert(0, m)

    return digits


print(from_base10(10, 2))


def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("Digit map is not long enough")

    encoding = ''
    for d in digits:
        # not efficient
        # encoding += digit_map[d]

        encoding = ''.join([digit_map[d] for d in digits])
    return encoding


print(encode(from_base10(255, 16), '0123456789ABCDEF'))


def rebase_from10(number, base):
    digit_map = "0123456789abcdefghijklmnopqrstuvwxyz"
    if base < 2 or base > 36:
        raise ValueError("invalid id base: 2 <= base <= 36")

    # ternary syntax
    sign = -1 if number < 0 else 1

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding

    return encoding


print(rebase_from10(10, 2))

print(rebase_from10(1000000, 16))
e = rebase_from10(1000000, 16)
print(int(e, base=16))
