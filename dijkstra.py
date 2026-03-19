import heapq
import csv
from collections import defaultdict

def load_graph(filename):
    graph = defaultdict(dict)

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            src = row['source'].strip()
            dest = row['destination'].strip()
            dist = int(row['distance'])

            graph[src][dest] = dist
            graph[dest][src] = dist

    return graph

def dijkstra(graph, start):
    distances = {city: float('inf') for city in graph}
    parent = {city: None for city in graph}

    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        for neighbor in graph[current_city]:
            weight = graph[current_city][neighbor]
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = current_city
                heapq.heappush(pq, (new_distance, neighbor))

    return distances, parent

def get_path(parent, end):
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    return path[::-1]

graph = load_graph("cities.csv")

start = input("Enter start city: ")
end = input("Enter destination city: ")

distances, parent = dijkstra(graph, start)

if end in distances and distances[end] != float('inf'):
    path = get_path(parent, end)
    print("Shortest distance:", distances[end], "km")
    print("Path:", " -> ".join(path))
else:
    print("No path found")
