import pandas as pd

df = pd.read_csv (r'./Data/BTCUSDT_1d_data.csv')

# DATE ,open, high/open, low/open, volume/open
# 10d avarage/open, 20d avarage/open, last 30d avarage/open, need more

data = []
big_dad = -1
sum = [0, 0, 0]

for index, row in df.iterrows():
    day = (index + 1) % 30

    #for avarage
    if (index > 29):
        sum[2] = sum[2] - df.iloc[index - 30].Open + row.Open
        sum[1] = sum[1] - df.iloc[index - 20].Open + row.Open
        sum[0] = sum[0] - df.iloc[index - 10].Open + row.Open
    else:
        if (day > 20 or day == 0):
            sum[0] += row.Open
        if (day > 10 or day == 0):
            sum[1] += row.Open
        sum[2] += row.Open

    if (index > 29):
        big_dad += 1
        data.append([])

        price = row.Open
        data[big_dad].append(row.Date)
        data[big_dad].append(price)
        data[big_dad].append(row.High / price)
        data[big_dad].append(row.Low / price)
        data[big_dad].append(row.Volume / price)

        data[big_dad].append((sum[0] / 10) / price)
        data[big_dad].append((sum[1] / 20) / price)
        data[big_dad].append((sum[2] / 30) / price)



save = pd.DataFrame(data=data, columns=["Date", "Price",  "HighR", "LowR", "VolumeR", "Avg10", "Avg20", "Avg30"])  # 1st row as the column names

save.to_csv("./Data/BTC_daily.csv")

