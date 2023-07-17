import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

from dataset import get_data


def exercise7(columns, start_year=2018, end_year=2021, hours=70):
    data = get_data()
    c1 = data[[columns[0], "DateTime"]].set_index("DateTime")[f"{start_year}":f"{end_year}":]
    c2 = data[[columns[1], "DateTime"]].set_index("DateTime")[f"{start_year}":f"{end_year}":]

    corr_hours = sm.tsa.ccf(c1[:hours:], c2[:hours:])

    plt.plot(np.arange(corr_hours.size), corr_hours)
    plt.xlabel("hours")
    plt.ylabel(f"cov({columns[0]}, {columns[1]})")

    plt.show()


exercise7(["Density", "DST"])

exercise7(["Velocity", "DST"])