def encode_varint(n):
    out = bytearray()
    while True:
        group = n & 0x7F
        n >>= 7
        if n:
            out.append(group | 0x80)
        else:
            out.append(group)
            return bytes(out)


def decode_varint(data):
    result = 0
    weight = 1
    pos = 0

    while True:
        byte = data[pos]
        pos += 1

        result += (byte & 0x7F) * weight

        if byte < 0x80:
            return result

        weight *= 128


for n in [0, 1, 127, 128, 300, 16384, 2**32, 2**64 - 1]:
    enc = encode_varint(n)
    print(enc)
    dec = decode_varint(enc)
    assert dec == n
