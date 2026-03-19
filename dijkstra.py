import heapq# Load graph from CSV
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
    distances = {}
    for city in graph:
        distances[city] = float('inf')

    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        for neighbor in graph[current_city]:
            weight = graph[current_city][neighbor]
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances

start_city = "Delhi"
result = dijkstra(graph, start_city)

print("Shortest distances from", start_city)
for city in result:
    print(city, ":", result[city], "km")
