from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    row = len(image)
    col = len(image[0])
    val = image[sr][sc]
    list = [[0 for i in range(col)] for j in range(row)]
    search_fill(image, sr, sc, newColor, val, row - 1, col - 1, list)

    return image

def search_fill(image: List[List[int]], sr: int, sc: int, newColor: int, value: int, row: int, col: int, record: List[List[int]]):
    if sr < 0 or sc < 0 or sr > row or sc > col or image[sr][sc] != value: return
    if record[sr][sc] == 0:
        image[sr][sc] = newColor
        record[sr][sc] = 1
        search_fill(image, sr - 1, sc, newColor, value, row, col, record)
        search_fill(image, sr + 1, sc, newColor, value, row, col, record)
        search_fill(image, sr, sc - 1, newColor, value, row, col, record)
        search_fill(image, sr, sc + 1, newColor, value, row, col, record)

grid = [[1,1,1],[1,1,0],[1,0,1],[1,0,1]]

print(floodFill(grid, 1, 1, 2))