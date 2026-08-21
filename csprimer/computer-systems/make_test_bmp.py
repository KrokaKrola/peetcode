"""Generate small 24-bit BI_RGB BMPs with known pixel patterns for rotation testing."""

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def write_bmp(path: str, pixels: list[list[tuple[int, int, int]]]) -> None:
    """pixels[0] is the TOP row; written bottom-up as BMP requires."""
    height = len(pixels)
    width = len(pixels[0])
    row_size = ((width * 3 + 3) // 4) * 4
    padding = row_size - width * 3
    image_data_size = row_size * height
    pixel_data_offset = 54  # 14 file header + 40 BITMAPINFOHEADER
    file_size = pixel_data_offset + image_data_size

    out = bytearray()
    out += b"BM"
    out += file_size.to_bytes(4, "little")
    out += (0).to_bytes(4, "little")
    out += pixel_data_offset.to_bytes(4, "little")

    out += (40).to_bytes(4, "little")
    out += width.to_bytes(4, "little", signed=True)
    out += height.to_bytes(4, "little", signed=True)
    out += (1).to_bytes(2, "little")
    out += (24).to_bytes(2, "little")
    out += (0).to_bytes(4, "little")
    out += image_data_size.to_bytes(4, "little")
    out += (2835).to_bytes(4, "little")
    out += (2835).to_bytes(4, "little")
    out += (0).to_bytes(4, "little")
    out += (0).to_bytes(4, "little")

    for row in reversed(pixels):
        for r, g, b in row:
            out += bytes([b, g, r])  # BGR on disk
        out += b"\x00" * padding

    open(path, "wb").write(out)


def corners_10x10() -> list[list[tuple[int, int, int]]]:
    """White field, one distinctly colored 2x2 block in each corner."""
    grid = [[WHITE for _ in range(10)] for _ in range(10)]
    for y in range(2):
        for x in range(2):
            grid[y][x] = RED            # top-left
            grid[y][9 - x] = GREEN      # top-right
            grid[9 - y][x] = BLUE       # bottom-left
            grid[9 - y][9 - x] = YELLOW # bottom-right
    grid[0][4] = BLACK                  # asymmetry marker on the top edge
    return grid


def stripes_7x3() -> list[list[tuple[int, int, int]]]:
    """Non-square, width 7 -> row_size 24 (3 padding bytes). Each row one color."""
    return [
        [RED] * 7,
        [GREEN] * 7,
        [BLUE] * 7,
    ]


write_bmp("test_corners_10x10.bmp", corners_10x10())
write_bmp("test_stripes_7x3.bmp", stripes_7x3())
print("wrote test_corners_10x10.bmp and test_stripes_7x3.bmp")
