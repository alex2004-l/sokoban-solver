import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("stats/combined.csv")

df = df[df["method"] == "ida_star"]
df = df[df["heuristic"] == "best"]
df = df[df["no_pulls"] == True]

palette = {
    True : "purple",
    False : "pink"
}

sns.barplot(data=df, x="name", y="time", hue="caching", palette=palette)
plt.title("IDA* caching the heuristic")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
