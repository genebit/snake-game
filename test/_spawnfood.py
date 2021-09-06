
import random

window_width = 100
window_height = 100

x_grid = []
y_grid = []

for x in range(0, window_width, 10):
    x_grid.append(x)
    for y in range(0, window_height, 10):
        y_grid.append(y)        

# Pick a random position
x_picker = random.randint(0, len(x_grid)-1)
y_picker = random.randint(0, len(y_grid)-1)

print('Spawned food at:', x_grid[x_picker], y_grid[y_picker])