"""Print a 24-bit BMP as colored text so you can see a rotation happened."""
import sys

SYM = {
    (255, 0, 0): "R", (0, 255, 0): "G", (0, 0, 255): "B",
    (255, 255, 0): "Y", (255, 255, 255): ".", (0, 0, 0): "#",
}


def show(path: str) -> None:
    data = open(path, "rb").read()
    pixel_data_offset = int.from_bytes(data[10:14], "little")
    width = int.from_bytes(data[18:22], "little", signed=True)
    height = int.from_bytes(data[22:26], "little", signed=True)
    row_size = ((width * 3 + 3) // 4) * 4

    print(f"{path}: {width}x{height}  row_size={row_size} "
          f"pad={row_size - width*3}  file_size={len(data)}")
    for y in range(height):
        file_row = height - 1 - y  # bottom-up
        start = pixel_data_offset + file_row * row_size
        line = ""
        for x in range(width):
            b, g, r = data[start + x*3 : start + x*3 + 3]
            line += SYM.get((r, g, b), "?")
        print("   ", line)
    print()


for p in sys.argv[1:]:
    show(p)
