import pandas as pd



class Simulation:

    def __init__(self):
        pass

    def calculate_portfolio_value(self,weights, prices):

        self.portfolio_value = 0
        for asset, weight in weights.items():
            asset_price = prices[asset][-1]
            asset_value = asset_price * weight
            portfolio_value += asset_value
        
        return self.portfolio_value
    
    def backtest_portfolio(self, weights, prices, initial_portfolio_value):

        portfolio_values = [initial_portfolio_value]

        for index, row in prices.iterrows():
            current_portfolio_value = self.calculate_portfolio_value(weights, row)

            portfolio_values.append(current_portfolio_value)

        portfolio_df = pd.DataFrame(portfolio_values, columns = ['Portfolio Value'])

        return portfolio_df