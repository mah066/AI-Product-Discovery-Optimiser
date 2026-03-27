import pandas as pd

before = pd.read_csv("data/results_baseline.csv")
after = pd.read_csv("data/results_after.csv")

def summarise(df, label):
    total = len(df)
    visible = df["appears"].sum()
    visibility_rate = round((visible / total) * 100, 2) if total else 0
    avg_position = round(df["position"].mean(), 2) if total else 0
    avg_query_match = round(df["query_match"].mean() * 100, 2) if total else 0
    avg_quality = round(df["recommendation_score"].mean(), 2) if total else 0

    return pd.DataFrame([{
        "phase": label,
        "tests": total,
        "visibility_rate": visibility_rate,
        "avg_position": avg_position,
        "avg_query_match_percent": avg_query_match,
        "avg_recommendation_score": avg_quality
    }])

summary = pd.concat([
    summarise(before, "baseline"),
    summarise(after, "optimised")
], ignore_index=True)

summary["visibility_change"] = summary["visibility_rate"].diff()
summary["query_match_change"] = summary["avg_query_match_percent"].diff()
summary["quality_change"] = summary["avg_recommendation_score"].diff()

summary.to_csv("data/final_metrics.csv", index=False)
print(summary)