#!/bin/python3

import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

horizontal_max = max(grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3] for i in range(20) for j in range(17))

vertical_max = max(grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j] for i in range(17) for j in range(20))

diagonal1_max = max(grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3] for i in range(17) for j in range(17))

diagonal2_max = max(grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3] for i in range(3,20) for j in range(17))

max_max = max(horizontal_max, vertical_max, diagonal1_max, diagonal2_max)

print(max_max)