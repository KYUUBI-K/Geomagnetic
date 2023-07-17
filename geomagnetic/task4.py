import numpy as np
import matplotlib.pyplot as plt
from dataset import get_data
def exercise4(column, start_year=2018, end_year=2021):
    data = get_data()

    subset = data[[column, "Date"]].set_index("Date")[f"{start_year}":f"{end_year}":]
    count = subset.value_counts().sort_index()

    x = np.fromiter(map(lambda _: _[0], count.index), dtype=int)
    y = count.values
    probs = y / y.sum()

    median = (probs * x).sum()

    fig, ax = plt.subplots(1, 2)
    ax[0].bar(x, y, width=3)
    ax[0].set_ylabel("Number of observations")
    ax[1].bar(x, probs, width=3)
    ax[1].set_ylabel("Probability")
    ax[1].axvline(median, ls="--", c="k")
    plt.text(median + 1, probs.min(), 'μ')
    fig.suptitle(column)

    plt.show()
exercise4("DST")
exercise4("Velocity")
exercise4("Density")
