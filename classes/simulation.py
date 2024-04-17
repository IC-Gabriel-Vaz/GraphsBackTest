import pandas as pd
import math


class Simulation:

    def __init__(self, inicial_investment):
        self.portfolio_value = inicial_investment
        self.portfolio_values = pd.DataFrame(columns=['Portfolio Value'])

    def calculate_portfolio_value(self, shares_per_asset , prices):

        self.portfolio_value = 0

        for shares, price in zip(shares_per_asset,prices):

            self.portfolio_value += shares*price 
        
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
        shares_per_asset = []
        i = 0 
        for value in amount_per_asset:
            shares = value/prices.iloc[0][i]
            i +=1
            #shares = math.floor(shares)
            shares_per_asset.append(shares)
        
        #print(shares_per_asset)

        for index, row in prices.iterrows():
            #row_dict = row.to_dict()
            current_portfolio_value = self.calculate_portfolio_value(shares_per_asset, row)
            print(f'{current_portfolio_value} \n')
            #self.portfolio_values.append(current_portfolio_value)
            self.portfolio_values.loc[index] = current_portfolio_value

        return self.portfolio_values
    

    # Considerar ações fracionárias