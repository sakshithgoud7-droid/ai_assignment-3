import heapq
import random

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

def navigate(n):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    start = (0, 0)
    goal = (n - 1, n - 1)
    current = start

    while current != goal:
        if random.random() < 0.2:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            grid[x][y] = 1

        path = astar(grid, current, goal)

        if not path:
            print("No path available")
            return

        if len(path) > 1:
            current = path[1]

    print("Goal reached")

navigate(70)
