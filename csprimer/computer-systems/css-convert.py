def normalize_hex(code: str) -> str:
    if len(code) == 8:
        return code

    if len(code) == 6:
        return code + "ff"

    res = []

    for el in code:
        res.append(el + el)

    if len(code) == 3:
        res.append("ff")

    return "".join(res)


print(normalize_hex("f0a"))  # "ff00aaff"
print(normalize_hex("f0a8"))  # "ff00aa88"
print(normalize_hex("fe830a"))  # "fe830aff"
print(normalize_hex("fe830aC0"))  # "fe830aC0"
print("-----------------")


def parse_hex(hex_color: str) -> tuple[int, int, int, int]:
    """Convert #RRGGBB to (r, g, b)."""

    code = hex_color.removeprefix("#")

    if len(code) not in {3, 4, 6, 8}:
        raise ValueError

    res = []

    code = normalize_hex(code)

    for lp in range(0, len(code), 2):
        chan = code[lp : lp + 2]
        res.append(int(chan, 16))

    return tuple(res)


print(parse_hex("#fe830a"))  # (254, 131, 10)
print(parse_hex("#000000"))  # (0, 0, 0)
print(parse_hex("#ffffff"))  # (255, 255, 255)
print(parse_hex("#FE830A"))  # (254, 131, 10)

try:
    print("should fail", parse_hex("#gg0000"))  # (254, 131, 10)
except ValueError:
    print("got value error for #gg0000")

try:
    print("should fail", parse_hex("##fe830a"))  # (254, 131, 10)
except ValueError:
    print("got value error for ##fe830a")

# print(parse_hex("#fe830a0"))  # (254, 131, 10)
