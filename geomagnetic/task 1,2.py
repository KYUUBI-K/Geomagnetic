import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
from dataset import get_data


data = get_data()

subset = data[["SSN", "DateTime"]].set_index("DateTime")

monthly_avg = subset.resample("M").mean()
hourly_avg = subset.resample("H").mean()
years = pd.date_range(subset.index.min(), date.today(), freq="Y")

years_span = 2
start_year = 2010
rolling_mean = subset.rolling(window=years_span * 365).mean()[f"{start_year}"::]

min_window_year = rolling_mean.idxmin().dt.year[0]

l, r = pd.date_range(start=f"{min_window_year- years_span}-12-31", end=f"{min_window_year + years_span}-12-31", periods=2)

plt.grid()
plt.scatter(hourly_avg.index, hourly_avg.SSN, s=0.1, c='b')
plt.plot(monthly_avg.index, monthly_avg.SSN, c='b')
plt.axvline(l, c="black", ls="--")
plt.axvline(r, c="black", ls="--")
plt.xlabel("years")
plt.ylabel("SSN")
plt.legend(["hourly average", "monthly average"])
plt.xticks(years, rotation=45)
plt.show()
