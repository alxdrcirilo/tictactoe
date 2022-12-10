import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv(filepath_or_buffer="tournament.csv")

# General statistics
p = sns.catplot(
    data=data,
    kind="bar",
    x="result",
    y="value",
    row="depth",
    col="size",
    hue="mode",
)
p.savefig("stats.png", dpi=200)

# Runtimes
fig, ax = plt.subplots(figsize=(8, 4))
sns.scatterplot(
    data=data,
    x="size",
    y="runtime",
    hue="depth",
    style="mode",
    palette="Set1",
    ax=ax,
)
sns.lineplot(
    data=data,
    x="size",
    y="runtime",
    hue="depth",
    style="mode",
    palette="Set1",
    linewidth=0.5,
    legend="",
    ax=ax,
)
fig.savefig("runtimes.png", dpi=200)
