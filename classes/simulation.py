import pandas as pd
import math


class Simulation:

    def __init__(self, parameters,data):
        self.shares = [0 for i in range(len(data.assets))]
        self.valuation = [0 for i in range(len(data.assets))]
        self.portfolio_value = parameters.investment
        self.portfolio_values = pd.DataFrame(columns=['Portfolio Value'])

    def calculate_portfolio_value(self, prices):

        self.portfolio_value = 0

        for shares_per_asset, price in zip(self.shares,prices):

            self.portfolio_value += shares_per_asset*price 
        
        return self.portfolio_value
    
    def backtest_portfolio(self, weights, prices):

        #print(prices)
        amount_per_asset = []
        for weight in weights.values():
            #print(weight)
            money_availble_per_asset = (self.portfolio_value)*(weight)
            #print(money_availble)
            amount_per_asset.append(money_availble_per_asset)

        #print(amount_per_asset)
        i = 0 
        for value in amount_per_asset:
            shares_per_asset = value/prices.iloc[0][i]
            self.shares[i] = shares_per_asset
            i +=1
            #shares = math.floor(shares)
        
    

        for index, row in prices.iterrows():
            #row_dict = row.to_dict()
            current_portfolio_value = self.calculate_portfolio_value(row)
            print(f'{index}   {current_portfolio_value} \n')
            #self.portfolio_values.append(current_portfolio_value)
            self.portfolio_values.loc[index] = current_portfolio_value

        return self.portfolio_values
    

    # Considerar ações fracionárias