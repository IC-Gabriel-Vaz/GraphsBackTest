import pandas as pd
import sys
sys.path.append("../classes")
sys.path.append('../dbUtils')


from admin import Admin
from get_assets_prices import get_prices 


def calculate_portfolio_value(weights, prices):

    portfolio_value = 0

    for asset, weight in weights.items():
        asset_price = prices[asset]
        asset_value = asset_price * weight
        portfolio_value += asset_value
    
    return portfolio_value

def backtest(weights, prices, investment):

    portfolio_values = [investment]

    for index, row in prices.iterrows():
        current_portfolio_value = calculate_portfolio_value(weights , row)
        portfolio_values.append(current_portfolio_value)

    portfolio_df = pd.DataFrame(portfolio_values, columns=['Portfolio_value'])

    return portfolio_df

if __name__ == '__main__':

    prices = get_prices('IBOV')

    weights = {}

    for asset in prices.columns:

        i = 1/len(prices.columns)

        weights[asset] = i


    backtest_result = backtest(weights, prices, 10000000)

    print(backtest_result)



