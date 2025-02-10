import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Load Data
network_data = pd.read_csv("networks_assignment.csv")

G = nx.Graph()
central_nodes = ["D", "F", "I", "N", "S"]
blue_nodes = central_nodes
green_nodes = ['BIH', 'GEO', 'ISR', 'MNE', 'SRB', 'CHE', 'TUR', 'UKR', 'GBR', 'AUS', 'HKG', 'USA']
yellow_nodes = ['AUT', 'BEL', 'BGR', 'HRV', 'CZE', 'EST', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LUX', 'NLD', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP']

node_colors = {n: "blue" for n in blue_nodes}
node_colors.update({n: "green" for n in green_nodes})
node_colors.update({n: "yellow" for n in yellow_nodes})

# Create edges
for col in network_data.columns[1:]:
    for index, row in network_data.iterrows():
        if row[col] > 0:
            G.add_edge(row["LABELS"], col)

plt.figure(figsize=(10, 10))
pos = nx.shell_layout(G, nlist=[central_nodes, list(G.nodes - set(central_nodes))])
nx.draw(G, pos, with_labels=True, node_color=[node_colors.get(n, "gray") for n in G.nodes], edge_color="gray", node_size=500)

# Save and show
plt.savefig("network_graph.png")
plt.show()
print("Network graph generated!")
