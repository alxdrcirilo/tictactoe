import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv(filepath_or_buffer="tournament.csv")

# General statistics
with sns.plotting_context("notebook", font_scale=1.5):
    p = sns.catplot(
        data=data,
        kind="bar",
        x="result",
        y="value",
        row="depth",
        col="size",
        hue="mode",
        height=4,
        aspect=1.5,
    )
    p.savefig("stats.png")

# Runtimes
fig, ax = plt.subplots(figsize=(8, 4))
data["size"] = data["size"].astype(int)
p = sns.scatterplot(
    data=data,
    x="size",
    y="runtime",
    hue="mode",
    style="depth",
    palette="Set1",
    ax=ax,
)
p = sns.lineplot(
    data=data,
    x="size",
    y="runtime",
    hue="mode",
    style="depth",
    palette="Set1",
    legend="",
    ax=ax,
)
p.set(xticks=data["size"].unique())
sns.despine()
fig.savefig("runtimes.png")
