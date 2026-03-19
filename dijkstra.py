import heapq

graph = {
    "Delhi": {"Agra": 233, "Jaipur": 280, "Lucknow": 555},
    "Agra": {"Delhi": 233, "Kanpur": 290},
    "Jaipur": {"Delhi": 280, "Udaipur": 395},
    "Lucknow": {"Delhi": 555, "Kanpur": 90},
    "Kanpur": {"Agra": 290, "Lucknow": 90},
    "Udaipur": {"Jaipur": 395}
}

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
