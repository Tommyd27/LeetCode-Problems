def addBinary(a: str, b: str) -> str:
    m, n = len(a), len(b)
    if m < n:
        m, n = n, m
        a, b = b, a
    a = a[::-1], b[::-1]
    carry_bit = 0
    out = ""
    for i, a_bit in enumerate(a):
        s = int(a_bit) + carry_bit + (int(b[i]) if i < n else 0)
        carry_bit = 1 if s >= 2 else 0
        out += "1" if s % 2 else "0"

    if carry_bit:
        out += "1"
    return out[::-1]
addBinary("1010", "1011")