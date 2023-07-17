import pandas as pd
def get_data():
    data = pd.read_csv('data.txt', sep=" ")

    column_names = ["Year", "Day", "Hour", "Density", "Velocity", "Kp", "DST", "SSN", "f10", "Date", "Time"]
    data.columns = column_names
    data.Date = pd.to_datetime(data.Date)
    data.Time = pd.to_timedelta(data.Time)
    data["DateTime"] = data.Date + data.Time

    return data