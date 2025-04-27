import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("ida_stats.csv")

sns.barplot(data=df, x="name", y="explored_states", hue="method", palette="pastel")
plt.title("Explored states beam search")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
