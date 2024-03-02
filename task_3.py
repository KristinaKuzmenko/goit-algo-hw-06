import networkx as nx
import matplotlib.pyplot as plt
import random


G = nx.Graph()

stops_2 = [
    "парк ім. Тараса Шевченко",
    "вул. Успенська",
    "вул. Тираспольська",
    "пл. Льва Толстого",
    "вул. Пастера",
    "Вул. Новосельського",
]
stops_3 = [
    "парк ім. Тараса Шевченко",
    "вул. Канатна",
    "вул. Катерининська",
    "вул. Преображенська",
    "вул. Прохоровська",
    "вул. Степова",
    "вул. Балківська",
    "Станція Застава 2",
    "вул. Стовпова",
    "Станція Застава 1",
]
stops_5 = [
    "вул. Новосельського",
    "вул. Преображенська",
    "вул. Троїцька",
    "вул. Канатна",
    "Куликово поле",
    "Залізничний вокзал",
    "проспект Шевченка",
    "Палац Спорту",
    "Аркадія",
]
stops_7 = [
    "вул. Архітекторська",
    "вул. Корольова",
    "3-тя станція Люстдорфської дороги",
    "1-а станція Люстдорфської дороги",
    "5-а станція Великого Фонтану",
    "Палац Спорту",
    "проспект Шевченка",
    "Куликово поле",
    "Залізничний вокзал",
    "вул. Пушкінська",
    "вул. Грецька",
    "вул. Преображенська",
    "пл. Льва Толстого",
]
stops_8 = [
    "вул. Хімічна",
    "вул. Грушевського",
    "вул. Розумовська",
    "вул. Прохоровська",
    "вул. Преображенська",
    "вул. Рішельєвська",
    "Залізничний вокзал",
]
stops_9 = [
    "вул. Космонавтів",
    "1-а станція Люстдорфської дороги",
    "5-а станція Великого Фонтану",
    "Палац Спорту",
    "проспект Шевченка",
    "Куликово поле",
    "вул. Канатна",
    "вул. Грецька",
]


all_stops = set(stops_2 + stops_3 + stops_5 + stops_7 + stops_8 + stops_9)

for stop in all_stops:
    G.add_node(stop)

routes = [stops_2, stops_3, stops_5, stops_7, stops_8, stops_9]

for route in routes:
    for i in range(len(route) - 1):
        G.add_edge(route[i], route[i + 1], weight=random.randint(1, 10))


def draw_weighted_graph(graph):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=800,
        node_color="lightblue",
        font_size=5,
        edge_color="gray",
        font_weight="bold",
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=4)
    plt.title("Тролейбусна мережа м. Одеса", fontsize=14)
    plt.show()


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float("infinity") for vertex in graph.nodes}
    distances[start] = 0
    unvisited = set(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float("infinity"):
            break

        for neighbor in graph[current_vertex]:
            # Перевірка наявності ваги ребра, якщо немає - використовується вага за замовчуванням 1
            weight = graph[current_vertex][neighbor].get("weight", 1)
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


# Тестування функції
if __name__ == "__main__":
    draw_weighted_graph(G)
    distances = dijkstra(G, "Палац Спорту")
    print('\n  Довжини найкоротших шляхів від зупинки "Палац Спорту" до всіх інших:')
    print(f"| {'Напрям поїздки':<35} | {'Відстань':<20} |")
    print(f"| {'-'*35} | {'-'*20} |")
    for station, path in distances.items():
        if station != "Палац Спорту":
            print(f"| {station:<35} | {path:^20} |")

    # Знаходження найкоротших шляхів від зупинки "Палац Спорту" до всїх інших за допомогою NetworkX
    shortest_paths_dict = nx.single_source_dijkstra_path(
        G, "Палац Спорту", cutoff=None, weight="weight"
    )
    shortest_paths_length_dict = nx.single_source_dijkstra_path_length(
        G, "Палац Спорту", cutoff=None, weight="weight"
    )
    combined_dict = {
        station: (shortest_paths_dict[station], shortest_paths_length_dict[station])
        for station in shortest_paths_dict
    }

    print("\n  Найкоротші шляхи від зупинки \"Палац Спорту\" до всіх інших:")	
    for station, (path, length) in combined_dict.items():
        if station != "Палац Спорту":
           print(f"\n Прямуємо до зупинки {station}. Довжина шляху: {length}. Шлях: {" -> ".join(path)}")
