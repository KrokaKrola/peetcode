class WordFinder:
    grid: list[str]

    directions = [
        [1, 0],  # top
        [0, 1],  # right
        [-1, 0],  # bottom
        [0, -1],  # left
        [1, 1],  # bottom-right
        [-1, -1],  # top-left
        [-1, 1],  # bottom-right
        [1, -1],  # bottom-left
    ]

    def set_grid(self, grid: list[str]):
        self.grid = grid

    def count(self, word: str) -> int:
        results = set()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                for di, dj in self.directions:
                    for m in range(len(word)):
                        r, c = i + di * m, j + dj * m

                        if (
                            r < 0
                            or r >= len(self.grid)
                            or c < 0
                            or c >= len(self.grid[r])
                        ):
                            break

                        if self.grid[r][c] != word[m]:
                            break
                    else:
                        start = (i, j)
                        end = (i + (len(word) - 1) * di, j + (len(word) - 1) * dj)
                        results.add((min(start, end), max(start, end)))

        return len(results)


grid = ["TIRATIRA", "IRATIRAT", "RATIRATI", "ATIRATIR"]
finder = WordFinder()
finder.set_grid(grid)

print(finder.count("TIRA"))  # 7
print(finder.count("TA"))  # 13
print(finder.count("RITARI"))  # 3
print(finder.count("A"))  # 8
print(finder.count("AA"))  # 6
print(finder.count("RAITA"))  # 0
