import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("beam_stats.csv")

sns.barplot(data=df, x="name", y="time", hue="method")
plt.title("Explored States per Map and Method")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
