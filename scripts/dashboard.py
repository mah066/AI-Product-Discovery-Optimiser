import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/final_metrics.csv")

plt.figure(figsize=(8, 5))
plt.bar(df["phase"], df["avg_query_match_percent"], color=["#9ca3af", "#2563eb"])
plt.title("Query Match Rate: Baseline vs Optimised")
plt.ylabel("Query Match (%)")
plt.xlabel("Phase")
plt.tight_layout()
plt.savefig("data/query_match_chart.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(df["phase"], df["avg_recommendation_score"], color=["#9ca3af", "#16a34a"])
plt.title("Average Recommendation Score")
plt.ylabel("Score")
plt.xlabel("Phase")
plt.tight_layout()
plt.savefig("data/recommendation_score_chart.png")
plt.close()