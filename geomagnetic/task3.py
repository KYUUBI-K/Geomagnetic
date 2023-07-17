import matplotlib.pyplot as plt
from dataset import get_data

data = get_data()
subset = data[["DST", "Density","Velocity","Date"]].set_index("Date")[f"{2018}":f"{2021}":]
hourly_avg = subset.resample("H").mean()
daily_avg = subset.resample("D").mean()
plt.grid()
plt.scatter(hourly_avg.index, hourly_avg.DST, s=0.1, c='black')
plt.plot(daily_avg.index, daily_avg.DST, c='b',  alpha=0.4)
plt.xlabel("years")
plt.ylabel("DST")
plt.legend(["hourly average", "daily average"])
plt.show()
