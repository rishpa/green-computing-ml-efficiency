import pandas as pd 

baseline = pd.read_csv("baseline_results.csv")
optimized = pd.read_csv("optimized_results.csv")

comparison = baseline.merge(
          optimized, 
          on="Dataset",
          suffixes=("_baseline", "_optimized")
)

print(comparison)

comparison.to_csv("comparison_results.csv", index=False)

print("Comparison file saved!")
