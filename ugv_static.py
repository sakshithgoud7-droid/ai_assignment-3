import heapq
import random

def create_grid(n, density):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if random.random() < density:
                grid[i][j] = 1
    return grid

def astar(grid, start, goal):
    open_list = [(0, start)]
    g_cost = {start: 0}
    parent = {}

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        x, y = current

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1
                neighbor = (nx, ny)

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f_cost = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    parent[neighbor] = current

    return None

grid = create_grid(70, 0.25)
start = (0, 0)
goal = (69, 69)

path = astar(grid, start, goal)

if path:
    print("Path length:", len(path))
else:
    print("No path found")
