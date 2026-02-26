import heapq

def dijkstra(graph, start, goal):
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)
        if node == goal:
            return cost
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            heapq.heappush(queue, (cost + weight, neighbor))
    return float('inf')