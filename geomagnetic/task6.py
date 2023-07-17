
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import pandas as pd

from dataset import get_data


def exercise6(column):
    data = get_data()

    subset = data[[column, "Date"]].set_index("Date")[f"{2018}":f"{2021}":]
    daily_avg = subset.resample("D").mean()

    corr_hours = sm.tsa.acf(subset)
    corr_days = sm.tsa.acf(daily_avg)
    plt.subplot(1, 2, 1)
    plt.plot(np.arange(corr_hours.size), corr_hours)
    plt.xlabel("hours")
    plt.ylabel(f"cov({column})")
    plt.subplot(1, 2, 2)
    plt.axvline(x=27, color='black', linestyle='--', label='Sun rotation period')
    plt.legend(["sun rotation period"])
    plt.plot(np.arange(corr_days.size), corr_days)
    plt.xlabel("days")
    plt.ylabel(f"cov({column})")

    plt.show()
exercise6("DST")
exercise6("Velocity")
exercise6("Density")