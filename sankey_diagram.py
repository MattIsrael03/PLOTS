import pandas as pd
import plotly.graph_objects as go

# Load Data
sankey_data = pd.read_csv("sankey_assignment.csv")

# Define layers
first_layer_sources = ["PS", "OMP", "CNP", "NRP", "NMCCC", "PEC", "NCDM", "RGS"]
final_layer_targets = ["Reg", "Aca", "Oth"]

source, target, value = [], [], []

# Unique node labels
all_nodes = list(sankey_data["LABEL"]) + first_layer_sources + final_layer_targets
node_indices = {node: i for i, node in enumerate(all_nodes)}

# First-layer connections (S, F, D, N, I → PS, OMP, etc.)
for i, label in enumerate(sankey_data["LABEL"]):
    for src in first_layer_sources:
        if src in sankey_data.columns and sankey_data[src][i] > 0:
            source.append(node_indices[label])
            target.append(node_indices[src])
            value.append(sankey_data[src][i])

# Second-layer connections (PS, OMP, etc. → Reg, Aca, Oth)
for i, label in enumerate(sankey_data["LABEL"]):
    for tgt in final_layer_targets:
        if tgt in sankey_data.columns and sankey_data[tgt][i] > 0:
            source.append(node_indices[label])
            target.append(node_indices[tgt])
            value.append(sankey_data[tgt][i])

# Create Sankey diagram
sankey = go.Figure(go.Sankey(
    node=dict(
        pad=15, thickness=20, line=dict(color="black", width=0.5),
        label=all_nodes,
        color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"] * 2
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color="rgba(150,150,150,0.4)"
    )
))

# Show
sankey.show(renderer="browser")
