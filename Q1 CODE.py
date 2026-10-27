def to_binary(n):
    return format(n & 0xFF, '08b')

def from_binary(b):
    n = int(b, 2)
    if n >= 128:
        n -= 256
    return n

def arithmetic(a, b, operation):
    bin_a = to_binary(a)
    bin_b = to_binary(b)

    print("\nFirst operand:", a, "=", bin_a)
    print("Second operand:", b, "=", bin_b)

    if operation == '-':
        result = a - b
    else:
        result = a + b

    bin_result = to_binary(result)
    signed_result = from_binary(bin_result)

    print("Binary result:", bin_result)
    print("Decimal result:", signed_result)

    if result < -128 or result > 127:
        print("Arithmetic Overflow: Yes")
    else:
        print("Arithmetic Overflow: No")

# Expression (a): 45 - (+19)
print("Expression (a): 45 - (+19)")
arithmetic(45, 19, '-')

# Expression (b): (-35) - (-12)
print("\nExpression (b): (-35) - (-12)")
arithmetic(-35, -12, '-')