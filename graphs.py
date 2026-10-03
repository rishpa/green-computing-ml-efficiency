import pandas as pd
import matplotlib.pyplot as plt

# Load comparison results
df = pd.read_csv("comparison_results.csv")

labels = [
    "Neuroblastoma",
    "Sepsis",
    "Depression",
    "Brain Tumor",
    "Colorectal Cancer"
]

# Create runtime comparison graph
plt.figure(figsize=(10,6))

plt.bar(
     labels,
     df["Runtime_seconds_baseline"],
     label="Baseline"
)

plt.bar(
     labels,
     df["Runtime_seconds_optimized"],
     label="Optimized"
)

plt.xlabel("Datasets")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime Comparison Between Baseline and Optimized Models")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("runtime_comparison.png")

print("Graph saved successfully!")

# Create CO2 comparison line graph
plt.figure(figsize=(10,6))

plt.plot(
    labels,
    df["CO2_kg_baseline"],
    marker="o",
    label="Baseline"
)

plt.plot(
    labels,
    df["CO2_kg_optimized"],
    marker="o",
    label="Optimized"
)

plt.xlabel("Datasets")
plt.ylabel("CO2-equivalent Emissions (kg)")
plt.title("CO2 Emission Comparison Between Baseline and Optimized Models")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("co2_comparison.png")

print("CO2 graph saved successfully!")
