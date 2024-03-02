import networkx as nx
import matplotlib.pyplot as plt

from task_2 import find_way_dfs, find_way_bfs


G = nx.Graph()

# Ініціалізація назв зупинок за номерами тролейбусних маршрутів
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

# ініціалізація маршрутів
routes = [stops_2, stops_3, stops_5, stops_7, stops_8, stops_9]

for route in routes:
    for i in range(len(route) - 1):
        G.add_edge(route[i], route[i + 1])

# Візуалізація графа
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    node_color="lightblue",
    font_size=5,
    edge_color="gray",
    font_weight="bold",
)
plt.title("Тролейбусна мережа міста Одеса (спрощена)", fontsize=14)
plt.show()

num_edges = G.number_of_edges()
num_nodes = G.number_of_nodes()
is_connected = "Так" if nx.is_connected(G) else "Ні"
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
density = nx.density(G)

print(f"| {'Характеристика графа':<45} | {'Значення':<20} |")
print(f"| {'-'*45} | {'-'*20} |")
print(f"| {"Кількість вершин":<45} | {num_nodes:^20} |")
print(f"| {"Кількість ребер":<45} | {num_edges:^20} |")
print(f"| {"Мережа зв'язна":<45} | {is_connected:^20} |")
print(f"| {"Вузол із максимальною центральністю":<45} | {max(degree_centrality, key=degree_centrality.get):^20} |")
print(f"| {"Вузол із мінімальною центральністю":<45} | {min(degree_centrality, key=degree_centrality.get):^20} |")
print(f"| {"Вузол із максимальною зв'язністю":<45} | {max(closeness_centrality, key=closeness_centrality.get):^20} |")
print(f"| {"Вузол із мінімальною зв'язністю":<45} | {min(closeness_centrality, key=closeness_centrality.get):^20} |")
print(f"| {"Вузол із максимальним ступенем посередництва":<45} | {max(betweenness_centrality, key=betweenness_centrality.get):^20} |")
print(f"| {"Вузол із мінімальним ступенем посередництва":<45} | {min(betweenness_centrality, key=betweenness_centrality.get):^20} |")
print(f"| {"Щільність графа":<45} | {density:^20.4f} |")

# Гістограма розподілу ступенів вершин
degrees = [G.degree(n) for n in G.nodes()]
plt.hist(
    degrees, bins=range(min(degrees), max(degrees) + 1), alpha=0.75, edgecolor="black"
)
plt.title("Гістограма розподілу ступенів вершин")
plt.xlabel("Ступінь")
plt.ylabel("Кількість вершин")
plt.grid(axis="y", linestyle="--")
plt.show()

print("\nПошук шляху між двома вершинами за допомогою пошуку в глибину:")
find_way_dfs(G, "парк ім. Тараса Шевченко", "Палац Спорту")
print("\nПошук шляху між двома вершинами за допомогою пошуку в ширину:")
find_way_bfs(G, "парк ім. Тараса Шевченко", "Палац Спорту")
