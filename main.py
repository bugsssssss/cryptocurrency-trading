import pandas as pd

# ? Reading Trades


def read_trades_csv(file_path):
    df = pd.read_csv(file_path)
    return df


trades_data = read_trades_csv("prices.csv")
print("Data:\n", trades_data.head(), "\n\n")


# ? Aggregate trades into candlesticks
def aggregate_into_candlesticks(trades_data, interval):
    trades_data['TS'] = pd.to_datetime(trades_data['TS'])
    trades_data.set_index('TS', inplace=True)
    candlesticks = trades_data['PRICE'].resample(interval).ohlc()
    return candlesticks


candlesticks = aggregate_into_candlesticks(
    trades_data, '5T')  # 5-minute interval as test
print("Candlesticks:\n", candlesticks.head(), "\n\n")


# ? Calculating EMA
def calculate_ema(data, length):
    ema = data.rolling(window=length).mean()
    return ema


candlesticks['Close'] = (candlesticks['close']).astype(
    float)  # Converting to float if its not float already
candlesticks['EMA_14'] = calculate_ema(candlesticks['Close'], length=14)
print("EMA:\n", candlesticks.head())
