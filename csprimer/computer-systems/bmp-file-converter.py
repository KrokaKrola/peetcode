from dataclasses import dataclass


class BmpImage:
    @dataclass
    class FileHeader:
        magic_bm: bytes
        file_size: int
        reserved_bytes: int
        pixel_data_offset: int

        @classmethod
        def from_bytes(cls, data: bytes) -> "BmpImage.FileHeader":
            magic_bm = data[0:2]
            if magic_bm != b"BM":
                raise ValueError("magic value is not equal to BM")

            file_size = int.from_bytes(data[2:6], "little")
            reserved_bytes = int.from_bytes(data[6:10], "little")
            pixel_data_offset = int.from_bytes(data[10:14], "little")

            return BmpImage.FileHeader(
                magic_bm, file_size, reserved_bytes, pixel_data_offset
            )

    @dataclass
    class InfoHeader:
        header_size: int
        width: int
        height: int
        color_planes: int
        bits_per_pixel: int
        compression: int
        image_data_size: int

        @classmethod
        def from_bytes(cls, data: bytes) -> "BmpImage.InfoHeader":
            header_size = int.from_bytes(data[0:4], "little")
            width = int.from_bytes(data[4:8], "little", signed=True)
            height = int.from_bytes(data[8:12], "little", signed=True)
            color_planes = int.from_bytes(data[12:14], "little")
            bits_per_pixel = int.from_bytes(data[14:16], "little")
            if bits_per_pixel != 24:
                raise ValueError("bits per pixel value is not equal to 24")

            compression = int.from_bytes(data[16:20], "little")
            if compression != 0:
                raise ValueError("compression is not 0")

            image_data_size = int.from_bytes(data[20:24], "little")

            return BmpImage.InfoHeader(
                header_size,
                width,
                height,
                color_planes,
                bits_per_pixel,
                compression,
                image_data_size,
            )

    @dataclass
    class Data:
        data: bytes

        def to_matrix(self, width: int, height: int) -> list[list[bytes]]:
            row_size = ((width * 3 + 3) // 4) * 4

            matrix = []

            for row_idx in range(height - 1, -1, -1):
                start = row_idx * row_size
                data_row = self.data[start : start + width * 3]
                row = [data_row[x * 3 : x * 3 + 3] for x in range(width)]
                matrix.append(row)

            return matrix

        def rotate_matrix_90deg(
            self, matrix: list[list[bytes]], width: int, height: int
        ) -> list[list[bytes]]:
            reversed_matrix: list[list[bytes]] = []

            for col in range(width):
                new_row = []
                for row in range(height - 1, -1, -1):
                    new_row.append(matrix[row][col])
                reversed_matrix.append(new_row)

            return reversed_matrix

        def to_bytes(self, matrix: list[list[bytes]]) -> bytes:
            width = len(matrix[0])
            row_size = ((width * 3 + 3) // 4) * 4
            padding = row_size - width * 3

            out = bytearray()
            for row in reversed(matrix):
                for pixel in row:
                    out += pixel
                out += b"\x00" * padding

            return bytes(out)

        def rotate(self, width: int, height: int) -> None:
            matrix = self.to_matrix(width, height)
            rotated = self.rotate_matrix_90deg(matrix, width, height)
            self.data = self.to_bytes(rotated)

    def __init__(
        self,
        file_header: FileHeader,
        info_header: InfoHeader,
        data: Data,
        raw_header: bytes,
    ) -> None:
        self.file_header = file_header
        self.info_header = info_header
        self.data = data
        self.raw_header = raw_header

    def rotate(self) -> None:
        self.data.rotate(self.info_header.width, self.info_header.height)
        self.info_header.width, self.info_header.height = (
            self.info_header.height,
            self.info_header.width,
        )
        self.info_header.image_data_size = len(self.data.data)
        self.file_header.file_size = (
            self.file_header.pixel_data_offset + self.info_header.image_data_size
        )

    def to_bytes(self) -> bytes:
        out = bytearray(self.raw_header)

        out[2:6] = self.file_header.file_size.to_bytes(4, "little")
        out[18:22] = self.info_header.width.to_bytes(4, "little", signed=True)
        out[22:26] = self.info_header.height.to_bytes(4, "little", signed=True)
        out[34:38] = self.info_header.image_data_size.to_bytes(4, "little")
        out += self.data.data

        return bytes(out)

    def save(self, path: str) -> None:
        open(path, "wb").write(self.to_bytes())

    @classmethod
    def from_path(cls, path: str) -> "BmpImage":
        raw = open(path, "rb").read()

        file_header = BmpImage.FileHeader.from_bytes(raw[0:14])

        info_header = BmpImage.InfoHeader.from_bytes(raw[14:38])

        data = BmpImage.Data(raw[file_header.pixel_data_offset :])

        return cls(
            file_header, info_header, data, raw[: file_header.pixel_data_offset]
        )


bmp_image = BmpImage.from_path("./test_corners_10x10.bmp")
bmp_image.rotate()
bmp_image.save("./rotated.bmp")
