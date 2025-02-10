import pandas as pd
import matplotlib.pyplot as plt

# Load Data
bar_data = pd.read_csv("bar_assignment.csv")

# Update font settings
plt.rcParams.update({"font.family": "Arial", "font.size": 16})

# Process data
bar_data["COUNT"] = bar_data["COUNT"].map({1: "Yes", 0: "No"})
pivot_table = bar_data.pivot_table(index="LABEL", columns="COUNT", aggfunc="size", fill_value=0)

# Extract counts
yes_counts = pivot_table["Yes"]
no_counts = pivot_table["No"]

# Plot
plt.figure(figsize=(8, 6))
bars1 = plt.barh(pivot_table.index, no_counts, color="red", label="No")
bars2 = plt.barh(pivot_table.index, yes_counts, left=no_counts, color="blue", label="Yes")

# Add labels
for bars in [bars1, bars2]:
    for bar in bars:
        width = bar.get_width()
        if width > 0:
            plt.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2, int(width),
                     ha="center", va="center", fontsize=12, fontweight="bold", color="white")

# Labels and title
plt.xlabel("Count")
plt.ylabel("Category")
plt.title("Horizontal Stacked Bar Chart")
plt.xticks([0, 2, 4, 6, 8, 10])
plt.legend(title="Response")

# Save and show
plt.savefig("bar_chart.png")
plt.show()
