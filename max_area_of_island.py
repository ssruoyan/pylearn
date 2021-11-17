from typing import List

def max_area_of_island(island: List[List[int]]) -> int:
    row = len(island)
    col = len(island[0])
    count = 0
    for i in range(0, row):
        for j in range(0, col):
            if island[i][j] == 1:
                count = max(count, search_island(island, i, j))

    return count
    
def search_island(island: List[List[int]], i: int, j: int):
    row = len(island) - 1
    col = len(island[0]) - 1
    if i < 0 or j < 0 or i > row or j > col or island[i][j] == 0: return 0
    island[i][j] = 0
    return 1 + search_island(island, i + 1, j) + search_island(island, i - 1, j) + search_island(island, i, j + 1) + search_island(island, i, j - 1)


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(max_area_of_island(grid))