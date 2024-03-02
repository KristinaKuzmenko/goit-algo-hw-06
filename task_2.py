from collections import deque
import networkx as nx


# Функція для пошуку шляху в графі між двома вершинами методом DFS
def find_way_dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []  # зберігаємо шлях до вершини

    visited.add(start)
    path.append(start)  # Додаємо поточну вершину до шляху

    if start == end:
        print("Шлях знайдено:", " -> ".join(path))
        return path

    for neighbor in set(graph.neighbors(start)) - visited:
        result = find_way_dfs(graph, neighbor, end, visited, path)
        if result:
            return result

    path.pop()  # Видаляємо вершину зі шляху, якщо вона не веде до кінцевої вершини
    return False


# Функція для пошуку шляху в графі між двома вершинами методом BFS
def find_way_bfs(graph, start, end):
    visited = {start}
    queue = deque([(start, [start])])  # Зберігаємо вершину та шлях до неї

    while queue:
        current_vertex, path = queue.popleft()
        if current_vertex == end:
            print("Шлях знайдено:", " -> ".join(path))
            return path

        for neighbor in graph.neighbors(current_vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print("Шлях не існує")
    return None
