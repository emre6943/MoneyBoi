import csv
import datetime
import pandas as pd


file_name = "C:\\Users\\emre_\\Desktop\\ProjectGamer\\Data"

def getPrice(file, date):
    df = pd.read_csv(file)
    date2 = date + ", 02:00:00"
    date1 = date + ", 01:00:00"
    row = df.loc[df['Date'] == date2]
    if len(row) == 0:
        row = df.loc[df['Date'] == date1]
    return row.iloc[0]["Close"]

def getMarketPerformance(fromDate, toDate):
    df = pd.read_csv(file_name + "\\BTCUSDT_1d_data.csv")
    fromDate2 = fromDate + ", 02:00:00"
    fromDate1 = fromDate + ", 01:00:00"
    toDate1 = toDate + ", 01:00:00"
    toDate2 = toDate + ", 02:00:00"
    row = df.loc[df['Date'] == fromDate2]
    if len(row) == 0:
        row = df.loc[df['Date'] == fromDate1]
    startPrice = row.iloc[0]["Close"]

    row = df.loc[df['Date'] == toDate2]
    if len(row) == 0:
        row = df.loc[df['Date'] == toDate1]
    endPrice = row.iloc[0]["Close"]
    return endPrice / startPrice

class Gamer:
    def __init__(self, initialUSD, startingDate, endDate):
        self.initialUSD = initialUSD
        self.initialBTC = initialUSD / getPrice(file_name + "\\BTCUSDT_1d_data.csv", startingDate)
        self.startingDate = startingDate
        self.endDate = endDate
        #Need to add coins to the wallet
        self.wallet = {"USD": initialUSD, "BTC": 0}

    def convert_from_USD(self, name, usd_amount, date):
        self.wallet["USD"] -= usd_amount
        price = self.getUSDPrice(name, date)
        #trade_cost
        price = price * 1.0005
        self.wallet[name] = usd_amount / price

    def rewardFunc(self):
        totalUSD = 0
        totalBTC = 0

        for item in self.wallet:
            totalUSD += self.wallet[item] * self.getUSDPrice(item, self.endDate)
            totalBTC += self.wallet[item] * self.getBTCPrice(item, self.endDate)

        upUSDPercent = totalUSD / self.initialUSD
        upBTCPercent = totalBTC / self.initialBTC
        marketGain = getMarketPerformance(self.startingDate, self.endDate)

        return 10 * (upUSDPercent / marketGain) + 5 * upBTCPercent + 3 * upUSDPercent

    def USDtoBTC(self, usd, date):
        return usd / getPrice(file_name + "\\BTCUSDT_1d_data.csv", date)

    def getUSDPrice(self, name, date):
        if (name == "BTC"):
            return getPrice(file_name + "\\BTCUSDT_1d_data.csv", date)
        elif (name == "ETH"):
            return getPrice(file_name + "\\ETHUSDT_1d_data.csv", date)
        elif (name == "ADA"):
            return getPrice(file_name + "\\ADAUSDT_1d_data.csv", date)
        else:
            return 1

    def getBTCPrice(self, name, date):
        if (name == "USD"):
            return 1 / getPrice(file_name + "\\BTCUSDT_1d_data.csv", date)
        elif (name == "ETH"):
            return self.USDtoBTC(getPrice(file_name + "\\ETHUSDT_1d_data.csv", date), date)
        elif (name == "ADA"):
            return self.USDtoBTC(getPrice(file_name + "\\ADAUSDT_1d_data.csv", date), date)
        else:
            return 1

    def get_wallet_USD_value(self, date):
        return self.wallet["USD"] + (self.getUSDPrice("BTC", date) * self.wallet["BTC"]) #+ self.getUSDPrice("ETH", date) * self.wallet["ETH"] + self.getUSDPrice("ADA", date) * self.wallet["ADA"]

    #This method might need changes
    def translate_brain_to_action(self, arr, date):
        totalUSD = self.get_wallet_USD_value(date)
        #move all to usd NEED TO CHANGE FOR ETH
        self.wallet = {"USD": totalUSD, "BTC": 0}
        self.convert_from_USD("BTC", totalUSD * arr[0], date)

    def translate_model_to_action(self, arr, date):
        totalUSD = self.get_wallet_USD_value(date)
        #move all to usd NEED TO CHANGE FOR ETH
        self.wallet = {"USD": totalUSD, "BTC": 0}
        if(arr[0][0] > 0.5):
            self.convert_from_USD("BTC", totalUSD * 1, date)

    def get_data_for_choice(self, date):
        df = pd.read_csv(file_name + "\\BTC_daily.csv")
        date2 = date + ", 02:00:00"
        date1 = date + ", 01:00:00"
        row = df.loc[df['Date'] == date2]
        if len(row) == 0:
            row = df.loc[df['Date'] == date1]
        return [row.iloc[0]["Price"], row.iloc[0]["HighR"], row.iloc[0]["LowR"], row.iloc[0]["VolumeR"], row.iloc[0]["Avg10"], row.iloc[0]["Avg20"], row.iloc[0]["Avg30"]]



# ai = Gamer(1000, datetime.datetime.strptime("16/09/2017", "%d/%m/%Y").strftime("%d/%m/%Y"), datetime.datetime.strptime("20/09/2017", "%d/%m/%Y").strftime("%d/%m/%Y"))
# print(ai.wallet)
# ai.translate_brain_to_action([0.5, 0], (datetime.datetime.strptime("16/09/2017", "%d/%m/%Y") + datetime.timedelta(days=1)).strftime("%d/%m/%Y"))
# print(ai.wallet)
# reward = ai.rewardFunc()
# print(reward)



